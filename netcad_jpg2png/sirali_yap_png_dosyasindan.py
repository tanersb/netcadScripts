import os
from PIL import Image
from pytesseract import *
import shutil

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def siraliBirSekildeYap():
    for pngs in os.listdir('PNG'):
        img = Image.open('PNG\\'+pngs)
        output = pytesseract.image_to_string(img)
        print(output)
        name = pngs.replace('.png','.txt')
        file = open(name,'w')

        file.write(output)



siraliBirSekildeYap()



'''
print(os.listdir('PNG'))

print(len(os.listdir('PNG')))

'''
