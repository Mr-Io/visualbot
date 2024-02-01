"""


All coordinates assume a screen resolution of 5760x1080 (3 monitors)
and firefox maximized at 100% resolution in the 2nd monitor with  
the Bookmarks Toolbar enabled.

It uses pyautogui to move the coursor:
pos = pyautogui.position()
pyautogui.moveTo(100, 100, duration=1)
pyautogui.click(100, 100)
pyautogui.scroll(-4)
pyautogui.typewrite("hi there")
pyautogui.typewrite(["a", "left", "ctrlleft"])
pyautogui.hotkey("ctrlleft", "a")
"""
import re

import pyautogui

from base import xs_wait, s_wait, m_wait, l_wait, X_PAD, Y_PAD, copy, reset_mouse
from proc import get_code
from prod import Resource

OVERVIEW = "menu_overview.png"
SHIPYARD = "menu_shipyard.png"
DEFENCE = "menu_defence.png"
FLEET = "menu_fleet.png"
GALAXY = "menu_galaxy.png"
MSSG = "menu_mssg.png"

planet_location = (0, False)

def go(menu):
    try:
        x, y = pyautogui.locateCenterOnScreen(f"images/{menu}")
    except pyautogui.ImageNotFoundException:
        print(f"{menu} not available")
    else:
        pyautogui.moveTo(x, y, xs_wait(wait=False))
        pyautogui.click()
        m_wait()


def menu(menu):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                x, y = pyautogui.locateCenterOnScreen(f"images/{menu}")
            except pyautogui.ImageNotFoundException:
                pass
            else:
                pyautogui.moveTo(x, y, xs_wait(wait=False))
                pyautogui.click()
                m_wait()
            return func(*args, **kwargs)
        return wrapper
    return decorator

def planet(number=1, moon=False, forced=False):
    global planet_location
    if not (planet_location[0]==number and planet_location[1]==moon) or forced:
        planet_location = (number, moon)
        x = 1280 if not moon else 1440
        pyautogui.moveTo(X_PAD+x, Y_PAD+121+number*45, xs_wait(wait=False))
        pyautogui.click()
        m_wait()
        reset_mouse()
    
def resources():
    html_text = get_code()
    res = Resource()
    for i in ["metal", "crystal", "deuterium"]:
        m = re.search(f'<span id="resources_{i}" data-raw="(\d+)"', html_text)
        n = int(m.groups()[0])
        setattr(res, i, n)
    xs_wait(wait=True)
    return res

    
