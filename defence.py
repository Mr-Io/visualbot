import pyautogui

import menu

from base import xs_wait, m_wait, enter, copy

ROCKET_LAUNCHER = "rocket_launcher"
LIGHT_LASER = "light_laser"
HEAVY_LASER = "heavy_laser"
GAUSS_CANNON = "gauss_cannon"
PLASMA_TURRET = "plasma_turret"
SMALL_SHIELD = "small_shield" 
LARGE_SHIELD = "small_shield" # change
ANTIBALLISTIC_MISSILE = "antiballistic_missile"

defences = [ROCKET_LAUNCHER, LIGHT_LASER, HEAVY_LASER, GAUSS_CANNON, PLASMA_TURRET, SMALL_SHIELD, LARGE_SHIELD, ANTIBALLISTIC_MISSILE]

ROCKET_LAUNCHER_GREY = "rocket_launcher_grey"
LIGHT_LASER_GREY = "light_laser_grey"
HEAVY_LASER_GREY = "heavy_laser_grey"
GAUSS_CANNON_GREY = "gauss_cannon_grey"
PLASMA_TURRET_GREY = "plasma_turret_grey"
SMALL_SHIELD_GREY = "small_shield_grey"
LARGE_SHIELD_GREY = "large_shield_grey"
ANTIBALLISTIC_MISSILE_GREY = "antiballistic_missile_grey"

@menu.menu(menu.DEFENCE)
def build(item=None, n=1, commit=True):
    if item is None:
        return
    try:
        x, y = pyautogui.locateCenterOnScreen(f"images/{item}.png")
    except pyautogui.ImageNotFoundException:
        print(f"{item} not available")
        return
    pyautogui.moveTo(x, y, 0.2+xs_wait(wait=False))
    pyautogui.click()
    m_wait()
    xmax, ymax = pyautogui.locateCenterOnScreen("images/max.png", confidence=0.9)
    if n == 0:
        pyautogui.moveTo(xmax, ymax, xs_wait(wait=False))
        pyautogui.click()
    elif n > 1:
        pyautogui.moveTo(xmax+30, ymax-30, xs_wait(wait=False))
        pyautogui.doubleClick()
        pyautogui.typewrite(f"{n}")
    xs_wait(wait=True)
    if commit:
        enter()
    m_wait()


@menu.menu(menu.DEFENCE)
def _number(item):
    try:
        x, y = pyautogui.locateCenterOnScreen(f"images/{item}.png")
    except pyautogui.ImageNotFoundException:
        print(f"{item} not available")
        return -1
    pyautogui.moveTo(x, y, xs_wait(wait=False))
    pyautogui.click()
    m_wait()
    xn, yn = pyautogui.locateCenterOnScreen("images/defence_x.png")
    pyautogui.moveTo(xn-16, yn, xs_wait(wait=False))
    pyautogui.doubleClick()
    return int(copy())

def get():
    res = {}
    for d in defences:
        res[d] = _number(d)
        if res[d] < 0:
            res[d] = _number(d + "_grey")
    return res