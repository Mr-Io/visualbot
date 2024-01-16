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
import pyautogui

from base import xs_wait, m_wait, X_PAD, Y_PAD

MENU_OVERVIEW = "menu_overview.png"
MENU_SHIPYARD = "menu_shipyard.png"
MENU_DEFENCE = "menu_defence.png"
MENU_FLEET = "menu_fleet.png"
MENU_GALAXY = "menu_galaxy.png"

planet_location = (0, False)

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