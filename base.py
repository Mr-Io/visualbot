"""


All coordinates assume a screen resolution of 5760x1080 (3 monitors)
and firefox maximized at 100% resolution in the 2nd monitor with  
the Bookmarks Toolbar enabled.

It uses pyautogui to:
-- move the coursor --
pos = pyautogui.position()
pyautogui.moveTo(100, 100, duration=1)
pyautogui.click(100, 100)
pyautogui.scroll(-4)
pyautogui.typewrite("hi there")
pyautogui.typewrite(["a", "left", "ctrlleft"])
pyautogui.hotkey("ctrlleft", "a")

-- grab images and check pixels --
pyautogui.screenshot(region=(x1, y2, x2, y2))

-- locate image matches --
pyautogui.locateOnScreen("image.png", region=(x,y,x2,y2), confidence=0.8) #grayscale=True, 
"""
import random
import time

import pyautogui


X_PAD = 2*1920 
Y_PAD = 0

def screen_grab(width=1920, height=1080):
    box = (X_PAD, Y_PAD, width, height)
    im = pyautogui.screenshot(region=box)
    #im.save(f"{os.getcwd()}/full_snap__{str(int(time.time()))}.png", "PNG")
    return im

def back():
    pyautogui.moveTo(X_PAD+23, Y_PAD+90, 0.2 + random.random())
    pyautogui.click()
    time.sleep(5)