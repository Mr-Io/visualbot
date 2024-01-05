import time
import random
import math

import pyautogui
from pyautogui import ImageNotFoundException

from base import X_PAD, Y_PAD, screen_grab, back
from mssg import messages

def galaxy():
    """go to galaxy"""
    pyautogui.moveTo(X_PAD+455, Y_PAD+532, 0.4)
    pyautogui.click()
    time.sleep(5)

def galaxy__system_up(go=1):
    if go == 1:
        pyautogui.moveTo(X_PAD+760, Y_PAD+300, 0.4)
    else:
        pyautogui.moveTo(X_PAD+700, Y_PAD+300, 0.4)
    pyautogui.click()

def galaxy__go(galaxy, system):
    if not galaxy or not system:
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

def galaxy_system__spy(planet):
    tries = 0
    while (tries<6):
        pyautogui.moveTo(X_PAD+1155, Y_PAD+350 + planet*35, 0.2 + random.random())
        pyautogui.click()
        time.sleep(0.2 + random.random())
        if galaxy_system__check(planet, "SPY_SUCCESS", 0.6):
            return 0
        tries += 1
        rt = random.randrange(math.pow(2, tries), math.pow(3, tries))
        if rt > 8:
            messages()
        print(f"spy on planet {planet} failed, waiting {rt} s before try nº:{tries})")
        time.sleep(rt)
        if rt > 8:
            back()
        time.sleep(1 + random.random())
    return -1
    

def galaxy_system__check(planet, check, confidence=1):
    x_start = X_PAD + 565
    x_len = 660
    y_start = Y_PAD + 335 + planet*35
    y_len = 38
    try:
        return pyautogui.locateOnScreen(f"images/{check}.png", 
                                        confidence=confidence, 
                                        region=(x_start, y_start, x_len, y_len),
                                        )
    except ImageNotFoundException:
        return False
    
    




