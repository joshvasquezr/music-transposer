from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# Path to the SongSelect PDF file
pdf_path = '../data/song_A.pdf'

# Convert PDF to images (one image per page)
pages = convert_from_path(pdf_path)

# Save the first page as an image
pages[0].save('chart.png', 'PNG')


# Path to your Tesseract executable if not in PATH (for Windows users)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image from file (replace 'chart.png' with your file's path)
image_path = 'chart.png'
img = Image.open(image_path)

# Perform OCR on the image
text = pytesseract.image_to_string(img)

# Output the extracted text
print("Extracted Text:")
print(text)



