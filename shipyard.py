import pyautogui

import base

MENU_SHIPYARD = "MENU_SHIPYARD"

RECYCLER = (980, 695)


def _select():
    if base.menu_location != MENU_SHIPYARD:
        base.menu_location = MENU_SHIPYARD 
        pyautogui.moveTo(base.X_PAD+455, base.Y_PAD+457, 0.4)
        pyautogui.click()
        base.m_wait()

def build(item=None, n=1, commit=True):
    _select()
    if item is None:
        return
    pyautogui.moveTo(base.X_PAD+item[0], base.Y_PAD+item[1], 0.4)
    pyautogui.click()
    base.s_wait()
    if n == 0:
        pyautogui.moveTo(base.X_PAD+1150, base.Y_PAD+480, 0.4)
        pyautogui.click()
    elif n > 1:
        pyautogui.moveTo(base.X_PAD+1163,base.Y_PAD+450, 0.2)
        pyautogui.click()
        pyautogui.typewrite(f"{n}")
    pyautogui.moveTo(base.X_PAD+1165, base.Y_PAD+355, 0.4)
    if commit:
        pyautogui.click()
        base.m_wait()




