from PIL import Image
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

print(pytesseract.image_to_data(Image.open("text.png"), output_type=Output.DICT))

print("\n==========================================================\n")

print(pytesseract.image_to_data(Image.open("text.png"), output_type=Output.BYTES))
