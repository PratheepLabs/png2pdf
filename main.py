import os
import img2pdf

def png_to_pdf(input_dir, output_pdf):
    valid_extensions = ('.png',)
    files = [f for f in os.listdir(input_dir) if f.lower().endswith(valid_extensions)]
    if not files:
        print(f"No PNG files found in the directory: {input_dir}")
        return

    files.sort()
    file_paths = [os.path.join(input_dir, f) for f in files]
    print(f"Found {len(files)} PNG files. Processing...")

    with open(output_pdf, 'wb') as f:
        f.write(img2pdf.convert(file_paths))

    print(f"Success! PDF saved to: {output_pdf}")


DIRECTORY_PATH = '/home/pratheep/Downloads/Quiz-20260608T113458Z-3-001/Quiz'
OUTPUT_FILE = 'merged_output.pdf'

if __name__ == "__main__":
    png_to_pdf(DIRECTORY_PATH, OUTPUT_FILE)