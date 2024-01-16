import time
import random
import math

import pyautogui

from base import X_PAD, Y_PAD, xs_wait, s_wait, screen_grab
from menu import menu, MENU_GALAXY

TARGET_BLUE = ((30, 100, 90), 
               (35, 120, 110))
TARGET_PURPLE = ((100, 30, 115), 
                 (115, 35, 150))
TARGET_SPYSUCCESS = ((225, 0, 15), 
                     (250, 10, 25))

def _is_target(target, tcomp):
    for x, pmin, pmax in zip(target, tcomp[0], tcomp[1]):
        if pmin > x or pmax < x:
            return False
    return True

@menu(MENU_GALAXY)
def system_up(go=1):
    if go == 1:
        pyautogui.moveTo(X_PAD+760, Y_PAD+156, xs_wait(wait=False))
    else:
        pyautogui.moveTo(X_PAD+700, Y_PAD+156, xs_wait(wait=False))
    pyautogui.click()

@menu(MENU_GALAXY)
def _select(galaxy=None, system=None):
    if galaxy is None or system is None:
        return
    # change galaxy
    pyautogui.moveTo(X_PAD+630, Y_PAD+156, xs_wait(wait=False))
    pyautogui.click()
    pyautogui.typewrite(f"{galaxy}")
    # change system
    pyautogui.moveTo(X_PAD+735, Y_PAD+156, xs_wait(wait=False))
    pyautogui.click()
    pyautogui.typewrite(f"{system}")
    # click go
    pyautogui.moveTo(X_PAD+790, Y_PAD+156, xs_wait(wait=False))
    pyautogui.click()

@menu(MENU_GALAXY)
def spy_all(commit=True):
    tries = 0
    while (tries < 6):
        _spy_all(commit=commit)
        s_wait()
        n_targets = _spy_all(commit=False, count=True)
        if n_targets == 0 or not commit:
            return
        tries += 1
        rt = math.pow(3, tries) + random.randrange(1, tries*2)
        #print(f"some spy attempt failed, waiting {rt} s before trying again (nº of tries:{tries})")
        time.sleep(rt)
    
def _spy_all(image=None, commit=True, count=False):
    if image is None:
        image = screen_grab()
    spied_number = 0
    for i in range(1, 16):
        tc = _targetcolor(i, image)
        #print(i, tc)
        if _is_target(tc, TARGET_BLUE) or _is_target(tc, TARGET_PURPLE):
            px = image.getpixel((615, 216+i*35))
            if not _is_target(px, TARGET_SPYSUCCESS):
                spied_number += 1
                if not count:
                    pyautogui.moveTo(X_PAD+1155, Y_PAD+206+i*35, xs_wait(wait=False))
                    if commit:
                        pyautogui.click()
    return spied_number
 
def _targetcolor(planet, image=None):
    if not image:
        image = screen_grab()
    px = image.getpixel((1050, 206+planet*35))
    return px
