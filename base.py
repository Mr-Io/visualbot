"""


All coordinates assume a screen resolution of 5760x1080 (3 monitors)
and firefox maximized at 100% resolution in the 2nd monitor with  
the Bookmarks Toolbar enabled.

It uses pyautogui to move the coursor:
pos = pyautogui.position()
pyautogui.moveTo(100, 100, duration=1)
pyautogui.click(100, 100)
pyautogui.scroll(-4)
pyautogui.typewrite("hi there")
pyautogui.typewrite(["a", "left", "ctrlleft"])
pyautogui.hotkey("ctrlleft", "a")
"""
import os
import random
import time

from PIL import ImageGrab
import pyautogui

X_PAD = 1920 #2560
Y_PAD = 0


menu_location = None
planet_location = (0, False)

def planet(number=1, moon=False):
    global planet_location
    if not (planet_location[0]==number and planet_location[1]==moon):
        planet_location = (number, moon)
        x = 1280 if not moon else 1440
        pyautogui.moveTo(X_PAD+x, Y_PAD+265+number*45, xs_wait(wait=False))
        pyautogui.click()
        m_wait()

def l_wait():
    return time.sleep(8+2*random.random())

def m_wait():
    return time.sleep(3 + random.random())

def s_wait():
    return time.sleep(1 + random.random()/2)

def xs_wait(wait=False):
    r = 0.1 + random.random()/10
    if wait:
        time.sleep(r)
    return r

def screen_grab(x=1920, y=1080, save=False, padding=True, allscreen=False):
    box = (X_PAD, Y_PAD, X_PAD+x, Y_PAD+y) if padding else (0, 0, x, y)
    im = ImageGrab.grab(box) if not allscreen else ImageGrab.grab() 
    if save:
        im.save(f"{os.getcwd()}/full_snap__{str(int(time.time()))}.png", "PNG")
    return im

def back():
    pyautogui.hotkey('alt', 'left')
    m_wait()

def reload():
    pyautogui.hotkey('ctrl', 'r')
    m_wait()
