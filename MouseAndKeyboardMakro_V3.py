#Button.x2
import pyautogui
import pyperclip
import keyboard
import os
import time
import re
import ctypes
from pynput import mouse
from pynput.keyboard import Key, Listener
import pynput
from pynput import mouse
from plyer import notification
##from findimage import *
import cv2
import numpy as np
from PIL import ImageGrab
import tkinter as tk
from tkinter import messagebox


def alert(text, title='Alert'):
    root = tk.Tk()
    root.withdraw()  # Pencereyi gizle
    messagebox.showinfo(title, text)
    root.destroy()

#makro tuşlarına alt 1 basınca mesela kopyalananların count olarak saysın bildirim atsın

#alert(text='Mouse Macro programı açılacaktır!', title='Mouse Macro Maker  Created by TanerSB')

dortislem = ''
keys = []
key_count = 0
mouse_count = 0
screenSize = pyautogui.size()

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_MAXIMIZE = 3
SW_SHOWNORMAL = 1

hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_SHOWNORMAL)
user32.SetWindowPos(hWnd, 0, 0, 0, 380, 500, 0)
kernel32.SetConsoleTitleW("Mouse Makro Maker      by TanerSB")

def notificationApp(MakroMessageTitle,MakroMessage):
    notification.notify(title=f"{MakroMessageTitle}",
        message=f"{MakroMessage}",app_name="Mouse Makro")

def paste():
    ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)
    ctypes.windll.user32.keybd_event(0x56, 0, 0, 0)
    ctypes.windll.user32.keybd_event(0x11, 0, 0x0002, 0)
    ctypes.windll.user32.keybd_event(0x56, 0, 0x0002, 0)

def on_scroll(x, y, dx, dy):
    if dy < 0:print(f"Scrolled up")
    elif dy > 0:print(f"Scrolled down")


IOPIIPIUPUIPIU
def on_click(x, y, button, pressed):
    global mouse_count
    mouse_count += 1
    if button == mouse.Button.left and pressed:
        print (f'{(x, y)} Left Click')
        #f.write('left\n')

    if button == mouse.Button.right and pressed:
        #key_listener.stop()
        print (f'{(x, y)} Right Click')
        #f.write('right\n')

    if button == mouse.Button.middle and pressed:
        print (f'{(x, y)} Middle Click')
        #f.write('middle\n')
        text = pyperclip.paste()
        try:
            if '-' in text:
                text = text.replace('-','')
                pyperclip.copy(text)
                print("Text replaced - to blank", text)  
        except:
            pass

    if button == mouse.Button.x2 and pressed:
        makroUpperCase()

def on_press(key):
    global key_count
    global dortislem
    key_count += 1
    try:
        if 'Key.' in str(key): 
            key = str(key)
            key = key.replace("Key.","")
            #print(f"{key} press")
    except:pass

    if str(key) == '<96>':
        key = '0'
        print(f"'0' press")
        keys.append("'0'")
    elif str(key) == '<97>':
        key = '1'
        print(f"'1' press")
        keys.append("'1'")
    elif str(key) == '<98>':
        key = '2'
        print(f"'2' press")
        keys.append("'2'")
    elif str(key) == '<99>':
        key = '3'
        print(f"'3' press")
        keys.append("'3'")
    elif str(key) == '<100>':
        key = '4'
        print(f"'4' press")
        keys.append("'4'")
    elif str(key) == '<101>':
        key = '5'
        print(f"'5' press")
        keys.append("'5'")
    elif str(key) == '<102>':
        key = '6'
        print(f"'6' press")
        keys.append("'6'")
    elif str(key) == '<103>':
        key = '7'
        print(f"'7' press")
        keys.append("'7'")
    elif str(key) == '<104>':
        key = '8'
        print(f"'8' press")
        keys.append("'8'")
    elif str(key) == '<105>':
        key = '9'
        print(f"'9' press")
        keys.append("'9'")
    elif str(key) == '<110>':
        key = ','
        print(f"',' press")
        keys.append("','")
    elif str(key) == "'\\x03'":print(f"Ctrl + C ")
    elif str(key) == "'\\x16'":print(f"Ctrl + V ")
    elif str(key) == "'\\x13'":print(f"Ctrl + S ")
    elif str(key) == "'\\x18'":print(f"Ctrl + X ")
    elif str(key) == "'\\x01'":print(f"Ctrl + A ")
    elif str(key) == "'\\x11'":print(f"Ctrl + Q ")
    elif str(key) == "'\\x17'":print(f"Ctrl + W ")
    elif str(key) == "'\\x05'":print(f"Ctrl + E ")
    elif str(key) == "'\\x12'":print(f"Ctrl + R ")
    elif str(key) == "'\\x0e'":print(f"Ctrl + N ")
    elif str(key) == "'\\x02'":print(f"Ctrl + B ")
    elif str(key) == "'\\x14'":print(f"Ctrl + T ")
    elif str(key) == "'\\x19'":print(f"Ctrl + Y ")
    elif str(key) == "'\\x15'":print(f"Ctrl + U ")
    elif str(key) == "'\\t'":  print(f"Ctrl + I ")
    elif str(key) == "'\\x0f'":print(f"Ctrl + O ")
    elif str(key) == "'\\x10'":print(f"Ctrl + P ")
    elif str(key) == "'\\x1a'":print(f"Ctrl + Z ")
    elif str(key) == "'\\x0c'":print(f"Ctrl + L ")
    elif str(key) == "'\\x1b'":print(f"Ctrl + Ğ ")
    elif str(key) == "'\\x1d'":print(f"Ctrl + Ü ")
    elif str(key) == "'\\x04'":print(f"Ctrl + D ")
    elif str(key) == "'\\x06'":print(f"Ctrl + F ")
    elif str(key) == "'\\x07'":print(f"Ctrl + G ")
    elif str(key) == "'\\x08'":print(f"Ctrl + H ")
    elif str(key) == "'\\x0b'":print(f"Ctrl + K ")
    elif str(key) == '<186>':  print(f"Ctrl + Ş ")
    elif str(key) == '<222>':  print(f"Ctrl + İ ")
    elif str(key) == '<191>':  print(f"Ctrl + Ö ")
    elif str(key) == '<220>':  print(f"Ctrl + Ç ")
    elif str(key) == '<190>':print(f"Ctrl + . ")
    elif str(key) == "'\\x1c'":print(f"Ctrl + , ")
    else:
        key = str(key)
        print(f"{key} press")
        keys.append(key)

    try:
        islemKey = key.replace("'","")
        if islemKey.isdigit():
            dortislem += islemKey
        if islemKey == '-' or islemKey == '+' or islemKey == '*' or islemKey == '/' or islemKey == '.' or islemKey == ',':
            try: islemKey = islemKey.replace(",",".")
            except:pass
            dortislem += islemKey
            print(f"{dortislem}")
    except:pass

    try:
        if key == "'='" and dortislem != '':
            notificationApp(f'{dortislem}', f'{eval(dortislem)}')
            dortislem = ''
            #print(eval(dortislem))
    except:notificationApp(f'Dört İşlem Hatası', f'Dört İşlem Hatası')

    if key_count >= 10:
        write_ff(keys)
        #pass
    waitMacro(keys)


def write_ff(keys):

    with open("log.txt", "w" ,encoding= 'utf-8') as f:
        #print(keys)
        for key in keys:
            if key == 'space':f.write(" ")
            elif key == 'ctrl_l':f.write("(Ctrll)")
            elif key == 'ctrl_r':f.write("(Ctrlr)")
            elif key == 'alt_l' or key == 'alt':f.write("(Altl)")
            elif key == 'alt_gr':f.write("(Altgr)")
            elif key == 'caps_lock':f.write("(CapsLock)")
            elif key == 'backspace':f.write("(BackSpace)")
            elif key == 'tab':f.write("(Tab)")
            elif key == 'shift' or key == 'shift_l':f.write("(Shiftl)")
            elif key == 'shift_r':f.write("(Shiftr)")
            elif key == 'esc':f.write("(Esc)")
            
            else:
                text = key.strip("'")
                f.write(f"{text}")

        #print(text)

def sayısallastırNCN():
    notificationApp(f'NCN Sayısallastır','Active')
    input_str = pyperclip.paste()
    output_str = ""
    for line in input_str.split("\n"):
        line = line.strip()
        if line:
            output_str += line[:7] + " " + line[8:18] + " " + line[19:] + "\n"

    print(output_str)
    pyperclip.copy(output_str)

def waitMacro(keys):

    makroKey = keys[-2:] #tersten son iki
    
    if len(makroKey) > 1:
        #print(makroKey)
        if str(makroKey[0]) == "alt_l":
            if str(makroKey[1]) == "','":makroCommaToDot()
            if str(makroKey[1]) == "'ü'":makroUpperCase()
            if str(makroKey[1]) == "'.'":makroDotToComma()
            if str(makroKey[1]) == "'0'":makroSpliteEnter()
            if str(makroKey[1]) == "'1'":makroUpperCase()
            if str(makroKey[1]) == "'2'":makroLowerCase()
            if str(makroKey[1]) == "'3'":makroCountText()
            if str(makroKey[1]) == "'4'":makroCommaToDot()
            if str(makroKey[1]) == "'5'":pass
            if str(makroKey[1]) == "'6'":pass
            if str(makroKey[1]) == "'7'":pass
            if str(makroKey[1]) == "'8'":pass
            if str(makroKey[1]) == "'9'":sayısallastırNCN()

        if makroKey[0] == "alt_gr":print(makroKey)

    if keys[-1] == "media_next":makroUpperCase()
        
    if keys[-1] == "f7":
        #clickSim(686, 602) #görüntüden yapacağım
        mouse_x, mouse_y = pyautogui.position()
        ekranda_ara_ve_tıkla('images/Nc32_Tamam_4kyDUFfh6m.png')

    if keys[-1] == "f8":
        #clickSim(686, 602) #görüntüden yapacağım
        mouse_x, mouse_y = pyautogui.position()
        ekranda_ara_ve_tıkla('images/Nc32_Y7ju4cEScV.png')
    
    if keys[-1] == "f9":
        #clickSim(686, 602) #görüntüden yapacağım
        mouse_x, mouse_y = pyautogui.position()
        ekranda_ara_ve_tıkla('images/Nc32_Tamam2.png')

def clickSim(coordinatesX, coordinatesY):
    mouse_x, mouse_y = pyautogui.position()
    pyautogui.click(coordinatesX,coordinatesY)

def makroCommaToDot():
    text = pyperclip.paste()
    try:
        if ',' in text:
            text = text.replace(',','.')
            pyperclip.copy(text)
            if len(text) < 256:notificationApp(f'Comma To Dot Active',f'{text}')
            else:notificationApp(f'Comma To Dot Active', f' Replaced ( , ) to ( . )')
        else:notificationApp(f'Comma To Dot Active', f'You dont have ( , ) in your text')
    except:
        if len(text) < 256:notificationApp(f'Comma To Dot Working', f'{text}')
        else:notificationApp(f'Comma To Dot Working', f' Replaced ( , ) to ( . )')

def makroDotToComma():
    text = pyperclip.paste()
    try:
        if '.' in text:
            text = text.replace('.',',')
            pyperclip.copy(text)
            if len(text) < 256:notificationApp(f'Comma To Dot Active',f'{text}')
            else:notificationApp(f'Comma To Dot Active', f' Replaced ( . ) to ( , )')
        else:notificationApp(f'Comma To Dot Active', f'You dont have ( . ) in your text')
    except:
        if len(text) < 256:notificationApp(f'Comma To Dot Working', f'{text}')
        else:notificationApp(f'Comma To Dot Working', f' Replaced ( . ) to ( , )')


def makroCountText():
    text = pyperclip.paste()
    countText = len(text)
    notificationApp(f'Counter Active-Count:{countText}',f'{text}')

def get_location_image(template_filename):
    control = control_image(template_filename)
    if (control != False):return (control[0], control[1])
    else:return False

def control_image(template_filename):
    pyautogui.screenshot('current_screen.png')
    screen = cv2.imread('current_screen.png', cv2.IMREAD_GRAYSCALE)
    template = cv2.imread(template_filename, cv2.IMREAD_GRAYSCALE)
    if template is None:
        #print("failed to load template.")
        return False
    w, h = template.shape[::-1]
    method = 'cv2.TM_CCOEFF_NORMED'
    meth = eval(method)
    res = cv2.matchTemplate(screen, template, meth)
    threshold = 0.8
    loc = np.where(res >= threshold)
    x, y = loc[::-1]
    if len(x) > 0 and len(y) > 0:return (x[0], y[0], w, h)
    else:return False
    
def click_image(template_filename, button="left", clicks=1, interval=0.25) -> object:
    control = control_image(template_filename)
    mouse_x, mouse_y = pyautogui.position()
    if (control != False):
        w = control[2]
        h = control[3]
        top_left = control
        bottom_right = (top_left[0] + w, top_left[1] + h)
        center = ((top_left[0] + bottom_right[0]) / 2, (top_left[1] + bottom_right[1]) / 2)
        pyautogui.moveTo(center)
        pyautogui.click(center, button=button, clicks=clicks, interval=interval)
        pyautogui.moveTo(mouse_x, mouse_y, duration=0)
        print(f"{template_filename} Tıklandı.")
        return True
    else:
        print(f"{template_filename} Bulunmadı.")
        return False

def ekranda_ara_ve_tıkla(aranacak):
    for i in range(5):
        if get_location_image(aranacak) == False:
            print(f'{aranacak} aranıyor.')
        elif keys[-1] == "f9" or "f8" or "f7":
            break
        else:
            print(f'{aranacak} bulundu.')
            break
    click_image(aranacak)

def makroSpliteEnter():
    text = pyperclip.paste()
    try:
        text = str(text)
        if '\r' in text:
            text = text.replace('\r','')
        text= text.split('\n')
        #pyperclip.copy(text)
        notificationApp(f'Split Working',f'{text}')
    except:
        notificationApp(f'Split Not Working',f'{text}')
        print(text)

def makroUpperCase():
    text = pyperclip.paste()
    text = text.upper()
    pyperclip.copy(text)
    notificationApp("Changed to uppercase and pasted",f"{text}")
    #print("Copied text changed to uppercase", text)
    paste()

def makroLowerCase():
    text = pyperclip.paste()
    text = text.lower()
    pyperclip.copy(text)
    notificationApp("Changed to lowercase and pasted",f"{text}")
    #print("Copied text changed to uppercase", text)
    paste()

def listen():
    with mouse.Listener(on_click=on_click,on_scroll=on_scroll,) as mouse_listener:
        with Listener(on_press=on_press) as keyboard_listener:
            mouse_listener.join()
            keyboard_listener.join()

listen()

        


