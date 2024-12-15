#Button.x2
import pyperclip
import keyboard
import os
import time
import re
import ctypes
from pynput import mouse
from pynput.keyboard import Key, Listener


def paste():
    ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)
    ctypes.windll.user32.keybd_event(0x56, 0, 0, 0)
    ctypes.windll.user32.keybd_event(0x11, 0, 0x0002, 0)
    ctypes.windll.user32.keybd_event(0x56, 0, 0x0002, 0)



def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        print ('Left')
        #f.write('left\n')

    if button == mouse.Button.right and pressed:
        #key_listener.stop()
        print ('Right')
        #f.write('right\n')
        
    if button == mouse.Button.middle and pressed:
        print ('Middle')
        #f.write('middle\n')
        text = pyperclip.paste()
        try:
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


with mouse.Listener(on_click=on_click) as listener:
    try:
        listener.join()
    except:
        print('Done')
