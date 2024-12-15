#Button.x2
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

keys = []
key_count = 0
mouse_count = 0

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_MAXIMIZE = 3
SW_SHOWNORMAL = 1

hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_SHOWNORMAL)
user32.SetWindowPos(hWnd, 0, 0, 0, 380, 500, 0)
kernel32.SetConsoleTitleW("Mouse Makro Maker      by TanerSB")

def paste():
    ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)
    ctypes.windll.user32.keybd_event(0x56, 0, 0, 0)
    ctypes.windll.user32.keybd_event(0x11, 0, 0x0002, 0)
    ctypes.windll.user32.keybd_event(0x56, 0, 0x0002, 0)

def on_scroll(x, y, dx, dy):
    if dy < 0:
        print("Scrolled up")
    elif dy > 0:
        print("Scrolled down")

def on_click(x, y, button, pressed):
    global mouse_count
    mouse_count += 1
    if button == mouse.Button.left and pressed:
        print ('Left Click')
        #f.write('left\n')

    if button == mouse.Button.right and pressed:
        #key_listener.stop()
        print ('Right Click')
        #f.write('right\n')
        
    if button == mouse.Button.middle and pressed:
        print ('Middle Click')
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
        text = pyperclip.paste()
        text = text.upper()
        pyperclip.copy(text)
        print("Copied text changed to uppercase", text)

        paste()

    #print(button,pressed)

def on_press(key):
    global key_count
    key_count += 1
    try:
        if 'Key.' in str(key): 
            key = str(key)
            key = key.replace("Key.","")
            #print(f"{key} press")
    except:pass
    if str(key) == '<96>':
        print(f"'0' press")
        keys.append("'0'")  
    elif str(key) == '<97>':
        print(f"'1' press")
        keys.append("'1'")  
    elif str(key) == '<98>':
        print(f"'2' press")
        keys.append("'2'")  
    elif str(key) == '<99>':
        print(f"'3' press")   
        keys.append("'3'")          
    elif str(key) == '<100>':
        print(f"'4' press")    
        keys.append("'4'")          
    elif str(key) == '<101>':
        print(f"'5' press")   
        keys.append("'5'")          
    elif str(key) == '<102>':
        print(f"'6' press")   
        keys.append("'6'")          
    elif str(key) == '<103>':
        print(f"'7' press")    
        keys.append("'7'")          
    elif str(key) == '<104>':
        print(f"'8' press")    
        keys.append("'8'")          
    elif str(key) == '<105>':
        print(f"'9' press")   
        keys.append("'9'")        
    elif str(key) == '<110>':
        print(f"',' press")
        keys.append("','")
    elif str(key) == "'\\x03'":
        print(f"Ctrl + C ")
        #keys.append("Ctrl + C")
    elif str(key) == "'\\x16'":
        print(f"Ctrl + V ")
        #keys.append("Ctrl + V")
    elif str(key) == "'\\x13'":
        print(f"Ctrl + S ")
        #keys.append("Ctrl + S")
    elif str(key) == "'\\x18'":
        print(f"Ctrl + X ")
        #keys.append("Ctrl + X") 
    elif str(key) == "'\\x01'":
        print(f"Ctrl + A ")
        #keys.append("Ctrl + A")
    elif str(key) == "'\\x11'":
        print(f"Ctrl + Q ")
        #keys.append("Ctrl + Q")
    elif str(key) == "'\\x17'":
        print(f"Ctrl + W ")
        #keys.append("Ctrl + W")
    elif str(key) == "'\\x05'":
        print(f"Ctrl + E ")
        #keys.append("Ctrl + E")
    elif str(key) == "'\\x12'":
        print(f"Ctrl + R ")
        #keys.append("Ctrl + R")
    elif str(key) == "'\\x0e'":
        print(f"Ctrl + N ")
        #keys.append("Ctrl + N")
    elif str(key) == "'\\x02'":
        print(f"Ctrl + B ")
        #keys.append("Ctrl + B")
    elif str(key) == "'\\x14'":
        print(f"Ctrl + T ")
        #keys.append("Ctrl + T")
    elif str(key) == "'\\x19'":
        print(f"Ctrl + Y ")
        #keys.append("Ctrl + Y")
    elif str(key) == "'\\x15'":
        print(f"Ctrl + U ")
        #keys.append("Ctrl + U")
    elif str(key) == "'\\t'":
        print(f"Ctrl + I ")
        #keys.append("Ctrl + I")
    elif str(key) == "'\\x0f'":
        print(f"Ctrl + O ")
        #keys.append("Ctrl + O")
    elif str(key) == "'\\x10'":
        print(f"Ctrl + P ")
        #keys.append("Ctrl + P")
    elif str(key) == "'\\x1a'":
        print(f"Ctrl + Z ")
        #keys.append("Ctrl + Z")
    elif str(key) == "'\\x0c'":
        print(f"Ctrl + L ")
        #keys.append("Ctrl + L")
    else:
        print(f"{key} press")
        keys.append(key)
    if key_count >= 10:
        write_f(keys)
    waitMacro(keys)

def write_f(keys):
    with open("log.txt", "w" ,encoding= 'utf-8') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find('Key') == -1:
                f.write(k)
            elif k.find('enter') > 0:
                f.write("\n")


def waitMacro(keys):
    makroKey = keys[-2:] #tersten son iki
    
    if len(makroKey) > 1:
        #print(makroKey)
        if str(makroKey[0]) == "alt_l":
            if str(makroKey[1]) == "'s'":
                makro1()
        if makroKey[0] == "alt_gr":
            print(makroKey)


def makro1():
    print("Makro 1 Active --- (,) to (.) ")
    text = pyperclip.paste()
    try:
        if ',' in text:
            text = text.replace(',','.')
            pyperclip.copy(text)
    except:
        pass
    

    
    
def listen():
    with mouse.Listener(on_click=on_click,on_scroll=on_scroll,) as mouse_listener:
        with Listener(on_press=on_press) as keyboard_listener:
            mouse_listener.join()
            keyboard_listener.join()

listen()

        


