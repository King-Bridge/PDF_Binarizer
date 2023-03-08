# Project Name

PDF Binarizer

## Project Description

This is a Python script that takes a PDF file as input and outputs a new PDF file, where each page is the binary version (only black and white) of the input PDF's corresponding page image.

## Installation

```
git clone https://github.com/King-Bridge/PDF_Binarizer.git
pip install requirements.txt
```

## How to Use

```
python pdf_binarizer.py $your/pdf/path$
python pdf_binarizer.py $your/pdf/path$ --threshold=[the threshold you want]
python pdf_binarizer.py $your/pdf/path$ --output_path=$the/output/path/you/want$
python pdf_binarizer.py $your/pdf/path$ --threshold=[the threshold you want] --output_path=$the/output/path/you/want$
```

- Threshold should be a float number between 0 and 1; 0 means totally black and 1 means totally white.
- The default threshold is 0.5.
- The default output path is in this dir with file name "output.pdf"

Example input and output is "input.pdf" and "output.pdf" which can be found in dir "example".

```
python pdf_binarizer.py example/input.pdf --output_path=example/output.pdf
```

## Connect me

qy_lation@outlook.com
