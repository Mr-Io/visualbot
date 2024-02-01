import re
import math

import pyautogui

import menu

from base import xs_wait, m_wait, enter, copy
from proc import get_code
from defences import iterdefences

@menu.menu(menu.DEFENCE)
def build(item, n, commit=True):
    try:
        x, y = pyautogui.locateCenterOnScreen(item.img)
    except pyautogui.ImageNotFoundException:
        print(f"{item} not available")
        return
    pyautogui.moveTo(x, y, 0.2+xs_wait(wait=False))
    pyautogui.click()
    m_wait()
    xmax, ymax = pyautogui.locateCenterOnScreen("images/max.png", confidence=0.9)
    if n == math.inf:
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

def build_all(commit=True):
    res = menu.resources()
    print(f"res: {res}")
    update_number()
    for d in iterdefences:
        if d.buildable:
            nbuild = min(d.maxlim - d.number, res // d.cost)
            if nbuild <= 0:
                continue
            build(d, n=nbuild, commit=commit)
            res -= d.cost*nbuild
            print(f"building {nbuild} {d} remaining res: {res}")

@menu.menu(menu.DEFENCE)
def update_number():
    html_text = get_code()
    for d in iterdefences:
        m = re.search(f'title="{d.cname} \((.*?)\)(.)', html_text)
        d.number = int(m.groups()[0].replace(",", "")) if m else -1
        d.buildable = m.groups()[1] == "\"" if m else False
