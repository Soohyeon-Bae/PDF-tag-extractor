# main.py
import pandas as pd
from src import extract_text_from_pdf, extract_regex_tag_matches


def main():
    # Set input file paths
    pdf_input = 'path/to/your/PDF.pdf'  # PDF file to extract text from

    # Set output file paths
    ocr_output = 'path/to/your/OCR_output.txt'  # Text file extracted from PDF
    regex_output = 'path/to/your/regex_output.xlsx'  # Excel file to save tag extraction results

    # Provide options to the user
    print("Select the step to execute:")
    print("1. Extract text from PDF")
    print("2. Extract tags from TXT file")
    choice = input("Choose (1, or 2): ")

    if choice == '1':
        # Step 1: Extract text from PDF
        extract_text_from_pdf(pdf_input, ocr_output)
        print(f"Extracted text from '{pdf_input}' to '{ocr_output}'.")

    elif choice == '2':
        # Step 2: Extract tags from TXT file
        regex_results_df = extract_regex_tag_matches(ocr_output)
        # Check if the results are empty
        if regex_results_df.empty:
            print("No data to save to Excel.")
        else:
            # Save results in multiple sheets
            max_rows_per_sheet = 1000000
            with pd.ExcelWriter(regex_output) as writer:
                for i in range(0, len(regex_results_df), max_rows_per_sheet):
                    df_chunk = regex_results_df.iloc[i:i + max_rows_per_sheet]
                    df_chunk.to_excel(writer, sheet_name=f'Sheet_{i // max_rows_per_sheet + 1}', index=False)

            print(f"Regular expression match results have been saved to '{regex_output}'.")


if __name__ == "__main__":
    main()
