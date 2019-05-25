from PIL import Image
import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image1 = Image.open("spreedsheet1.png")

text1 = pytesseract.image_to_string(image1, lang='eng')

print(text1)



