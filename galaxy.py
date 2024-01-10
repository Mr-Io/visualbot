import time
import random
import math

import pyautogui

import base
from mssg import messages

MENU_GALAXY = "MENU_GALAXY"

TARGET_GREY = (92, 92, 92)
TARGET_BLUE_min = (30, 110, 100)
TARGET_BLUE_max = (35, 120, 110)
TARGET_PURPLE_min = (105, 30, 115)
TARGET_PURPLE_max = (115, 35, 150)
TARGET_SPYSUCCESS_min = (225, 0, 15)
TARGET_SPYSUCCESS_max = (250, 10, 25)

def _is_target(target, tmin, tmax):
    for x, pmin, pmax in zip(target, tmin, tmax):
        if pmin > x or pmax < x:
            return False
    return True

def system_up(go=1):
    _select()
    if go == 1:
        pyautogui.moveTo(base.X_PAD+760, base.Y_PAD+300, 0.4)
    else:
        pyautogui.moveTo(base.X_PAD+700, base.Y_PAD+300, 0.4)
    pyautogui.click()

def _select(galaxy=None, system=None):
    if base.menu_location != MENU_GALAXY:
        base.menu_location = MENU_GALAXY 
        pyautogui.moveTo(base.X_PAD+455, base.Y_PAD+532, 0.4)
        pyautogui.click()
        #print("change menu to Galaxy")
        base.m_wait()
    if galaxy is None or system is None:
        return
    # change galaxy
    pyautogui.moveTo(base.X_PAD+630, base.Y_PAD+300, 1)
    pyautogui.click()
    pyautogui.typewrite(f"{galaxy}")
    # change system
    pyautogui.moveTo(base.X_PAD+735, base.Y_PAD+300, 1)
    pyautogui.click()
    pyautogui.typewrite(f"{system}")
    # click go
    pyautogui.moveTo(base.X_PAD+790, base.Y_PAD+300, 1)
    pyautogui.click()

def spy_all(commit=True):
    _select()
    tries = 0
    while (tries < 6):
        _spy_all(commit=commit)
        base.s_wait()
        n_targets = _spy_all(commit=False, count=True)
        if n_targets == 0 or not commit:
            return
        tries += 1
        rt = math.pow(3, tries) + random.randrange(1, tries*2)
        print(f"some spy attempt failed, waiting {rt} s before trying again (nº of tries:{tries})")
        time.sleep(rt)
    
def _spy_all(image=None, commit=True, count=False):
    if image is None:
        image = base.screen_grab()
    spied_number = 0
    for i in range(1, 16):
        tc = _targetcolor(i, image)
        print(i, tc)
        if _is_target(tc, TARGET_BLUE_min, TARGET_BLUE_max) or _is_target(tc, TARGET_PURPLE_min, TARGET_PURPLE_max):
            px = image.getpixel((615, 360+i*35))
            if not _is_target(px, TARGET_SPYSUCCESS_min, TARGET_SPYSUCCESS_max):
                spied_number += 1
                if not count:
                    pyautogui.moveTo(base.X_PAD+1155, base.Y_PAD+350 + i*35, 0.1 + random.random()/2)
                    if commit:
                        pyautogui.click()
    return spied_number
 
def _targetcolor(planet, image=None):
    if not image:
        image = base.screen_grab()
    px = image.getpixel((1050, 350+planet*35))
    return px




