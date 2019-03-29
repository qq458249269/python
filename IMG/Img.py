import pytesseract
from PIL import Image

img_path = '1.jpg'

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open(img_path),lang='chi_sim')
print(text)