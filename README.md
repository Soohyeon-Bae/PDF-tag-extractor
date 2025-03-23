# PDF Text Extraction 

This repository provides a framework for extracting text from PDF documents and processing the extracted text with regular expressions to filter out unwanted information.
 
## Overview 
 
The main goal of this project is to extract meaningful text from PDF files using OCR methods and to refine that text using regular expressions. The process includes:

1. **Text Extraction**: Using OCR libraries to extract text from PDF files.
2. **Text Processing**: Applying regular expressions to filter the extracted text, improving precision and recall.
 
## Project Structure
 
The repository is organized as follows:

PDF-tag-extractor/                                                                                                                                                                         
│
├── 📂 data/                                                                                                                                                  
│   ├── input/                                                                                                                                                 
│   ├── output/                                                                                                                                             
│   └── regex/                                                                                                                                 
│                                                                                                                                                                                                
├── 📂 src/                                                                                                                                                           
│   ├── pdf_extractor.py                                                                                                                                    
│   └── regex_extractor.py                                                                                                                                     
│                                                                                                                                                                                                
├── 📂 notebooks/                                                                                                                                                  
│   └── data_analysis_and_visualization.ipynb                                                                                                                                       
│                                                                                                                                                                                                
├── requirements.txt                                                                                                                                               
└── README.md                                                                                                                                                         


## Installation

To set up the project, clone the repository and install the required packages:
````
git clone https://github.com/Soohyeon-Bae/PDF-Text-Extraction.git
cd PDF-Text-Extraction
pip install -r requirements.txt
````

## Usage

1. Place your PDF files in the `data/input/` directory.
2. Run the text extraction script:
````
python src/pdf_extractor.py
````

3. The extracted text will be saved in the `data/output/` directory.
4. Use the text cleaner script to refine the extracted text:
````
python src/regex_extractor.py
````

## Preprocessing Techniques

To improve the precision and recall of the extracted text, the following preprocessing techniques can be applied:

- **Removing Unwanted Strings**: Use a predefined list of unwanted strings to filter out irrelevant content.
- **Whitespace Removal**: Trim unnecessary whitespace from the extracted text.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


updated (25.01.14) - Finding a way to improve accuracy by applying changes to the PDF processing library! By specifying the scanned area of the PDF, it’s possible to extract text in blocks from the desired section.


## License

This project is licensed under the MIT License. See the LICENSE file for more details.

