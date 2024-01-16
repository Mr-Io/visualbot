import pyautogui

from base import enter, xs_wait, s_wait, m_wait, copy
from menu import menu, MENU_SHIPYARD

BATTLECRUISER = "battlecruiser.png"
BATTLESHIP = "battleship.png"
BOMBER = "bomber.png"
COLONYSER = "colonyser.png"
CRUISER = "cruiser.png"
DESTROYER = "destroyer.png"
ESP_PROBE = "esp_probe.png" # problem with fleets...
HEAVY_FIGHER = "heavy_fighter.png"
LARGE_CARGO = "large_cargo.png"
LIGHT_FIGHTER = "light_fighter.png"
RECYCLER = "recycler.png"
RIP = "rip.png"
SMALL_CARGO = "small_cargo.png"

@menu(MENU_SHIPYARD)
def build(item=None, n=1, commit=True):
    if item is None:
        return
    try:
        x, y = pyautogui.locateCenterOnScreen(f"images/{item}", confidence=0.95)
    except pyautogui.ImageNotFoundException:
        print(f"Error: unable to build '{item}' (not available)")
        return
    pyautogui.moveTo(x, y, xs_wait(wait=False))
    pyautogui.click()
    s_wait()
    mx, my = pyautogui.locateCenterOnScreen("images/max.png", confidence=0.9)
    if n == 0:
        pyautogui.moveTo(mx, my, xs_wait(wait=False))
        pyautogui.click()
    elif n > 1:
        pyautogui.moveTo(mx+30, my-30, xs_wait(wait=False))
        pyautogui.click()
        pyautogui.typewrite(f"{n}")
    try:
        buildb = pyautogui.locateCenterOnScreen("images/build.png")
    except pyautogui.ImageNotFoundException:
        if commit:
            print(f"Error: {item} cannot be build")
        return
    if commit:
        enter()
    m_wait()

def number(item):
    build(item, commit=False)
    x, y = pyautogui.locateCenterOnScreen("images/number.png", confidence=0.9)
    pyautogui.moveTo(x+28, y)
    pyautogui.doubleClick()
    return int(copy())



