import pandas as pd
import re
from .utils import display_progress


def remove_unwanted_strings(text):
    """Function to remove strings that match a specific pattern"""
    unwanted_pattern = r"(your-unwanted-patterns)"
    cleaned_text = re.sub(unwanted_pattern, '', text)
    return cleaned_text.strip()


def extract_regex_tag_matches(text_file):
    """Find tags that match regex patterns in a text file and save the results to an Excel file"""
    # Read regex patterns
    regex_file = 'path/to/your/regex.xlsx'  # Excel file containing regex patterns
    regex_df = pd.read_excel(regex_file)
    raw_patterns = regex_df['regex'].tolist()  # Get the list of regex from the 'regex' column
    item_classes = regex_df['class'].tolist()  # Get the list of classes from the 'class' column
    patterns = [f"({pattern.lstrip('^')})" for pattern in raw_patterns]

    # Read the text file
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove unwanted strings
    text = remove_unwanted_strings(text)

    # List to store results
    results = []

    # Process patterns and classes together with their indices
    for idx, pattern in display_progress(list(enumerate(patterns)), desc='Extracting matches', unit='pattern'):
        matches = re.findall(pattern, text)

        # Process if there are matched results
        if matches:  # If results exist
            for match in matches:
                # If the matched result is a tuple, select only the first element
                if isinstance(match, tuple):
                    match_str = match[0]  # Select only the first string
                else:
                    match_str = match  # Use as is for single matches

                # Extract the tag using re.search
                search_result = re.search(pattern, match_str)
                if search_result:
                    search_str = search_result.group(0)  # First matched string
                else:
                    search_str = None  # If not matched, set to None

                # Get the class value for the corresponding pattern
                item_class = item_classes[idx]  # Use index to get the class

                # Add to the list (adding Tag Number and Item Class together)
                results.append((search_str, item_class))

    # Convert results to a DataFrame
    results_df = pd.DataFrame(results, columns=['Tag Number', 'Item Class'])
    return results_df
