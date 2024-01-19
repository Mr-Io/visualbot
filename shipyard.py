import re

import pyautogui

import menu

from base import enter, xs_wait, s_wait, m_wait, copy
from proc import get_code
from ships import iterships


@menu.menu(menu.SHIPYARD)
def build(ship=None, n=1, commit=True):
    if ship is None:
        return
    try:
        x, y = pyautogui.locateCenterOnScreen(ship.img, confidence=0.95)
    except pyautogui.ImageNotFoundException:
        print(f"Error: unable to build '{ship}' (not available)")
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
    if commit:
        enter()
    m_wait()

@menu.menu(menu.SHIPYARD)
def update_number():
    html_text = get_code()
    for s in iterships:
        m = re.search(f'title="{s.cname} \((\d*,\d*)\)', html_text)
        n = int(m.groups()[0].replace(',', '')) if m else -1
        if m:
            s.number = n



