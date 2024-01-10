import pyautogui

from base import *

RECYCLER = (980, 695)


def fleet():
    """go to defense"""
    pyautogui.moveTo(X_PAD+455, Y_PAD+457, 0.4)
    pyautogui.click()
    m_wait()

def shipyard__select(item):
    pyautogui.moveTo(X_PAD+item[0], Y_PAD+item[1], 0.4)
    pyautogui.click()
    s_wait()

def shipyard_selected__build(n=1, build=True):
    if n == 0:
        pyautogui.moveTo(X_PAD+1150, Y_PAD+480, 0.4)
        pyautogui.click()
    elif n > 1:
        pyautogui.moveTo(X_PAD+1163,Y_PAD+450, 0.2)
        pyautogui.click()
        pyautogui.typewrite(f"{n}")
    pyautogui.moveTo(X_PAD+1165, Y_PAD+355, 0.4)
    if build:
        pyautogui.click()
        m_wait()




