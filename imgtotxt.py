import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd= r'C:\Users\Enzo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img= cv2.imread(r'C:\Users\Enzo\Downloads\frenchtext.jpg')
text= pytesseract.image_to_string(img)
print(text)