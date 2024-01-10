import pyautogui

from base import *

SMALL_SHIELD = (625, 725)
BIG_SHIELD = (735, 725)
ANTIBALLISTIC = (840, 725)
PLASMA_TURRET = (1170, 625)
GAUSS_CANNON = (950, 625)
HEAVY_LASER = (840, 625)
ROCKET_LAUNCHER = (625, 625)

def select(item=None):
    if item is None:
        item = (455, 482)
    pyautogui.moveTo(X_PAD+item[0], Y_PAD+item[1], 0.4)
    pyautogui.click()
    s_wait()

def defense_selected__maxbuild():
    s_wait()

def build(n=1, commit=True):
    if n ==0:
        pyautogui.moveTo(X_PAD+1150, Y_PAD+480, 0.4)
        pyautogui.click()
    pyautogui.moveTo(X_PAD+1165, Y_PAD+355, 0.4)
    if commit:
        pyautogui.click()
        m_wait()




