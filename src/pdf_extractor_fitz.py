# src/pdf_extractor.py

import fitz  # PyMuPDF
from tqdm import tqdm


def extract_text_from_pdf(pdf_file, output_txt_file, clip=None):
    """Extract text from a PDF file and save it to a TXT file, excluding text within a specific rectangular area."""
    doc = fitz.open(pdf_file)  # Open the PDF file
    text = ""
    total_pages = len(doc)  # Total number of pages

    # Extract text from each page
    for page_num in tqdm(range(total_pages), desc='Extracting text from PDF', unit='page'):
        page = doc.load_page(page_num)  # Load the page

        # Extract text from the entire page
        blocks = page.get_text("blocks")

        # Accumulate text excluding the rectangular area
        for block in blocks:
            # Coordinates of the block
            x0, y0, x1, y1 = block[:4]

            # Only add text if the block is not within the clip area
            if clip is None or not clip.intersects(fitz.Rect(x0, y0, x1, y1)):
                if block[4].strip():  # Only add blocks that contain text
                    text += block[4] + "\n"

    # Save the text to a TXT file
    with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

    doc.close()  # Close the PDF file


if __name__ == "__main__":
    pdf_file = 'sample_1.pdf'  # Input PDF file path
    output_txt_file = 'sample_1_output.txt'  # Output TXT file path

    # Set the coordinates to exclude (e.g., (x0, y0) - (x1, y1))
    x0, y0, x1, y1 = 1850, 5, 2365, 1530  # Rectangle coordinates
    clip = fitz.Rect(x0, y0, x1, y1)  # Create a clip object

    extract_text_from_pdf(pdf_file, output_txt_file, clip)
    print(f"Text extracted to {output_txt_file}")
