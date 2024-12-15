from PIL import Image
from pytesseract import *
import os

#to-do
#replace outputs atıyourum iki şey girliecek , . yer değişecek
#boş klasörleri silen bir şey yap

#Note: You have to change the path below to your tesseract.exe location
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#This line stores the image texttoconvert.png inside the img variable
img  = Image.open("k2.png")

output = pytesseract.image_to_string(img)



print()
def removeAnyWord(output,remove):
    if f'{remove}' in output:
        output = output.replace(f'{remove}', '')
        return output


#output = removeAnyWord(output,'-')

def removeUnwantedWord(output):
    #istenmeyecek şekiller harfler falan eklenecek
    if '~' in output:
        output = output.replace('~', '')
    if '-' in output:
        output = output.replace('-', '')
    if ',' in output:
        output = output.replace(',', '')
    if 'a' in output:
        output = output.replace('a', '')
    if 'b' in output:
        output = output.replace('b', '')
    if 'c' in output:
        output = output.replace('c', '')
    if 'd' in output:
        output = output.replace('d', '')
    if 'e' in output:
        output = output.replace('e', '')
    if 'f' in output:
        output = output.replace('f', '')
    if 'g' in output:
        output = output.replace('g', '')
    if 'h' in output:
        output = output.replace('h', '')
    if 'ı' in output:
        output = output.replace('ı', '')
    if 'i' in output:
        output = output.replace('i', '')
    if 'j' in output:
        output = output.replace('j', '')
    if 'k' in output:
        output = output.replace('k', '')
    if 'l' in output:
        output = output.replace('l', '')
    if 'm' in output:
        output = output.replace('m', '')
    if 'n' in output:
        output = output.replace('n', '')
    if 'o' in output:
        output = output.replace('o', '')
    if 'ö' in output:
        output = output.replace('ö', '')
    if 'p' in output:
        output = output.replace('p', '')
    if 'r' in output:
        output = output.replace('r', '')
    if 's' in output:
        output = output.replace('s', '')
    if 'ş' in output:
        output = output.replace('ş', '')
    if 't' in output:
        output = output.replace('t', '')
    if 'u' in output:
        output = output.replace('u', '')
    if 'ü' in output:
        output = output.replace('ü', '')
    if 'w' in output:
        output = output.replace('w', '')
    if 'v' in output:
        output = output.replace('v', '')
    if 'y' in output:
        output = output.replace('y', '')
    if 'z' in output:
        output = output.replace('z', '')
    if 'q' in output:
        output = output.replace('q', '')

    return output

output=removeUnwantedWord(output)

def giveANumber(output,counter,step=1,finale='0.000 0 "" "" ""'):
    output = output.split('\n')
    #print(output)
    newOutput = ''

    for line in output:
        if line == '':
            continue
        else:
            newOutput += str(counter) + ' ' + line + ' ' + finale + '\n'
            counter += step
    return newOutput



#output=giveANumber(output,0)


def siraliBirSekildeYap():
    for pngs in os.listdir('PNG'):
        img = Image.open('PNG\\'+pngs)
        output = pytesseract.image_to_string(img)
        print(output)
        name = pngs.replace('.png','.txt')
        file = open(name,'w')

        file.write(output)




print()
print(output)


file = open('output.NCN','w')

file.write(output)




