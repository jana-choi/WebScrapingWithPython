from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"   # tesseract.exe 존재하는 경로

image = Image.open("text.png")
# print(pytesseract.image_to_string(image))
# print(pytesseract.image_to_boxes(image))
print(pytesseract.image_to_data(image))
