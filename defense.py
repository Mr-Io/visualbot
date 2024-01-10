import pyautogui

import base

SMALL_SHIELD = (625, 725)
BIG_SHIELD = (735, 725)
ANTIBALLISTIC = (840, 725)
PLASMA_TURRET = (1170, 625)
GAUSS_CANNON = (950, 625)
HEAVY_LASER = (840, 625)
ROCKET_LAUNCHER = (625, 625)

MENU_DEFENSE = "MENU_DEFENSE"

def _select():
    if base.menu_location != MENU_DEFENSE:
        base.menu_location = MENU_DEFENSE
        pyautogui.moveTo(base.X_PAD+455, base.Y_PAD+482, 0.4)
        pyautogui.click()
        #print("change menu to Defense")
        base.m_wait()

def build(item=None, n=1, commit=True):
    _select()
    if item is None:
        return
    pyautogui.moveTo(base.X_PAD+item[0], base.Y_PAD+item[1], 0.4)
    pyautogui.click()
    base.m_wait()
    if n ==0:
        pyautogui.moveTo(base.X_PAD+1150, base.Y_PAD+480, 0.4)
        pyautogui.click()
    pyautogui.moveTo(base.X_PAD+1165, base.Y_PAD+355, 0.4)
    if commit:
        pyautogui.click()
    base.m_wait()




