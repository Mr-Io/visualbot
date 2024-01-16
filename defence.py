import pyautogui

from base import X_PAD, Y_PAD, m_wait
from menu import menu, MENU_DEFENCE

SMALL_SHIELD = (625, 580)
BIG_SHIELD = (735, 580)
ANTIBALLISTIC = (840, 580)
PLASMA_TURRET = (1170, 480)
GAUSS_CANNON = (950, 480)
HEAVY_LASER = (840, 480)
ROCKET_LAUNCHER = (625, 480)

@menu(MENU_DEFENCE)
def build(item=None, n=1, commit=True):
    if item is None:
        return
    pyautogui.moveTo(X_PAD+item[0], Y_PAD+item[1], 0.4)
    pyautogui.click()
    m_wait()
    if n ==0:
        pyautogui.moveTo(X_PAD+1150, Y_PAD+336, 0.4)
        pyautogui.click()
    elif n>1:
        pyautogui.moveTo(X_PAD+1150, Y_PAD+303, 0.4)
        pyautogui.doubleClick()
        pyautogui.typewrite(f"{n}")
    pyautogui.moveTo(X_PAD+1165, Y_PAD+211, 0.4)
    if commit:
        pyautogui.click()
    m_wait()




