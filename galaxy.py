import time
import random
import math

import pyautogui

import menu

from base import X_PAD, Y_PAD, xs_wait, s_wait, screen_grab

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
 
def _targetcolor(planet, image=None):
    if not image:
        image = screen_grab()
    px = image.getpixel((1050, 206+planet*35))
    return px

@menu.menu(menu.GALAXY)
def galaxy_up(go=1):
    arrow = "arrow_right_green" if go > 0 else "arrow_left_green"
    x, y = pyautogui.locateCenterOnScreen(f"images/{arrow}.png")
    pyautogui.moveTo(x, y, xs_wait(wait=False))
    pyautogui.click()

@menu.menu(menu.GALAXY)
def system_up(go=1):
    arrow = "arrow_right_green" if go > 0 else "arrow_left_green"
    a = pyautogui.locateAllOnScreen(f"images/{arrow}.png")
    next(a)
    x, y = pyautogui.center(next(a))
    pyautogui.moveTo(x, y, xs_wait(wait=False))
    pyautogui.click()

@menu.menu(menu.GALAXY)
def _select(galaxy=None, system=None):
    if galaxy is None or system is None:
        return
    # change galaxy
    x, y = pyautogui.locateCenterOnScreen("images/arrow_right_green.png")
    x -= 28
    pyautogui.moveTo(x, y, xs_wait(wait=False))
    pyautogui.click()
    pyautogui.typewrite(f"{galaxy}")
    # change system
    x += 100
    pyautogui.moveTo(x, y, xs_wait(wait=False))
    pyautogui.click()
    pyautogui.typewrite(f"{system}")
    # click go
    x+= 60
    pyautogui.moveTo(x, y, xs_wait(wait=False))
    pyautogui.click()

@menu.menu(menu.GALAXY)
def spy_all(commit=True):
    tries = 0
    while (tries < 6):
        _spy_all(commit=commit)
        s_wait()
        n_targets = _spy_all(commit=False, count=True)
        if n_targets == 0 or not commit:
            return
        tries += 1
        if tries > 2:
            rt = math.pow(3, tries) + random.randrange(0, tries*2)
        else:
            rt = tries*s_wait(wait=False)
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