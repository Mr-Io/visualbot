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
import time

import pyautogui

from base import X_PAD, Y_PAD, screen_grab

from galaxy import *


def overview():
    """go to overview"""
    pyautogui.moveTo(X_PAD+455, Y_PAD+305, 0.2 + random.random())
    pyautogui.click()
    time.sleep(5)

def planet(number=1):
    pyautogui.moveTo(X_PAD+1280, Y_PAD+265+number*45, 0.2 + random.random())
    pyautogui.click()
    time.sleep(5)

def main():
    # check that we are in the correct tab
    # go 10 galaxies back and print witch type of target it has
    galaxy()
    srange = 21
    for p in range(1, 11):
        planet(p)
        for _ in range(0, srange):
            time.sleep(0.5 + random.random())
            im = screen_grab()
            for i in range(1, 16):
                tc = galaxy_system__targetcolor(i, im)
                print(i, tc)
                if is_target(tc, TARGET_BLUE_min, TARGET_BLUE_max) or is_target(tc, TARGET_PURPLE_min, TARGET_PURPLE_max):
                    galaxy_system__spy(i)
            galaxy__system_up()
        galaxy()
        for _ in range(0, srange):
            galaxy__system_up(-1)
            time.sleep(0.5 + random.random())
            im = screen_grab()
            for i in range(1, 16):
                tc = galaxy_system__targetcolor(i, im)
                print(i, tc)
                if is_target(tc, TARGET_BLUE_min, TARGET_BLUE_max) or is_target(tc, TARGET_PURPLE_min, TARGET_PURPLE_max):
                    galaxy_system__spy(i)


    # wait to complete load


if __name__ == "__main__":
    main()
    pass 