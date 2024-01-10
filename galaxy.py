import time
import random
import math

import pyautogui

from base import *
from mssg import messages

GALAXY_MENU = "GALAXY"

TARGET_GREY = (92, 92, 92)
TARGET_BLUE_min = (30, 110, 100)
TARGET_BLUE_max = (35, 120, 110)
TARGET_PURPLE_min = (105, 30, 115)
TARGET_PURPLE_max = (115, 35, 150)
TARGET_SPYSUCCESS_min = (225, 0, 15)
TARGET_SPYSUCCESS_max = (250, 10, 25)

def is_target(target, tmin, tmax):
    for x, pmin, pmax in zip(target, tmin, tmax):
        if pmin > x or pmax < x:
            return False
    return True

def system_up(go=1):
    if go == 1:
        pyautogui.moveTo(X_PAD+760, Y_PAD+300, 0.4)
    else:
        pyautogui.moveTo(X_PAD+700, Y_PAD+300, 0.4)
    pyautogui.click()

def select(galaxy=None, system=None):
    global menu_location
    if menu_location != GALAXY_MENU:
        menu_location = GALAXY_MENU
        pyautogui.moveTo(X_PAD+455, Y_PAD+532, 0.4)
        pyautogui.click()
        time.sleep(5)
    if galaxy is None or system is None:
        return
    # change galaxy
    pyautogui.moveTo(X_PAD+630, Y_PAD+300, 1)
    pyautogui.click()
    pyautogui.typewrite(f"{galaxy}")
    # change system
    pyautogui.moveTo(X_PAD+735, Y_PAD+300, 1)
    pyautogui.click()
    pyautogui.typewrite(f"{system}")
    # click go
    pyautogui.moveTo(X_PAD+790, Y_PAD+300, 1)
    pyautogui.click()

def spy(planet, commit=True):
    tries = 0
    px = (0,0,0)
    while (tries<6):
        pyautogui.moveTo(X_PAD+1155, Y_PAD+350 + planet*35, 0.2 + random.random())
        if not commit:
            time.sleep(0.2 + random.random())
            return
        pyautogui.click()
        time.sleep(0.2 + random.random())
        im = screen_grab()
        px = im.getpixel((615, 360+planet*35))
        print(px)
        if is_target(px, TARGET_SPYSUCCESS_min, TARGET_SPYSUCCESS_max):
            return 0
        tries += 1
        rt = random.randrange(math.pow(2, tries), math.pow(3, tries))
        print(f"spy on planet {planet} failed, waiting {rt} s before try nº:{tries})")
        if rt > 8:
            messages()
            time.sleep(rt)
            back()
        else:
            time.sleep(rt)
        time.sleep(1 + random.random())
    return -1
    

def targetcolor(planet, image=None):
    if not image:
        image = screen_grab()
    px = image.getpixel((1050, 350+planet*35))
    return px




