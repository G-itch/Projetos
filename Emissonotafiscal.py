import cv2
import pytesseract
import numpy as np
from matplotlib import pyplot as plt
pytesseract.pytesseract.tesseract_cmd= r'C:\Users\Enzo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img= cv2.imread(r'C:\Users\Enzo\Downloads\nota2.jpg',0)

# img = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2GRAY)
# img = cv2.medianBlur(img,5)
# img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv2.THRESH_BINARY,11,2)

plt.imshow(img,"gray")
text= pytesseract.image_to_string(img)
print(text)
plt.show()