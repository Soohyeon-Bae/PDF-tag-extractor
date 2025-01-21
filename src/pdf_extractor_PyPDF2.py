# src/pdf_extractor.py

import PyPDF2
from .utils import display_progress


def extract_text_from_pdf(pdf_file, output_txt_file):
    """Extract text from a PDF file and save it to a TXT file"""
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        total_pages = len(reader.pages)  # Total number of pages

        # Extract text from each page
        for page_num in display_progress(range(total_pages), desc='Extracting text from PDF', unit='page'):
            page = reader.pages[page_num]
            text += page.extract_text() + "\n"  # Append the text of each page

    # Save the text to a TXT file
    with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)


if __name__ == "__main__":
    pdf_file = 'path/to/your/input.pdf'  # Path to the input PDF file
    output_txt_file = 'path/to/your/output.txt'  # Path to the output TXT file

    extract_text_from_pdf(pdf_file, output_txt_file)
    print(f"Text extracted to {output_txt_file}")
