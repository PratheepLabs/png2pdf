# png2pdf

Merge all PNG images from a directory into a single PDF using Python and img2pdf.

## Overview

This small utility provides a `png_to_pdf` function (in `main.py`) that finds all `.png` files in a directory, sorts them alphabetically, and merges them into a single PDF using the `img2pdf` library.

## Requirements

- Python 3.8 or newer
- `img2pdf` Python package

## Installation

Install the dependency with pip:

```bash
pip install img2pdf
```

## Usage

There are two simple ways to use this project:

- Edit the `DIRECTORY_PATH` and `OUTPUT_FILE` variables in [main.py](main.py) and run:

```bash
python3 main.py
```

- Or import the function in your own script or an interactive session:

```python
from main import png_to_pdf
png_to_pdf('path/to/pngs', 'output.pdf')
```

The script will print status messages and confirm when the PDF has been written.

## Notes

- Input files are filtered by the `.png` extension (case-insensitive) and sorted alphabetically before merging.
- If no PNG files are found in the directory, the script prints a message and exits without creating a PDF.

## Example

Assuming your images are in `./images`:

```python
from main import png_to_pdf
png_to_pdf('./images', 'merged_output.pdf')
```

## Contribution

Feel free to open issues or submit pull requests for feature requests (for example, adding CLI argument support).
