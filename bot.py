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

from base import * 
import galaxy 
import defense
import shipyard 


def overview():
    """go to overview"""
    pyautogui.moveTo(X_PAD+455, Y_PAD+305, 0.2 + random.random())
    pyautogui.click()
    time.sleep(5)

def planet(number=1):
    pyautogui.moveTo(X_PAD+1280, Y_PAD+265+number*45, 0.2 + random.random())
    pyautogui.click()
    time.sleep(5)

def spy(planets=range(1, 11), commit=True):
    # check that we are in the correct tab
    # go 10 galaxies back and print witch type of target it has
    galaxy.select()
    srange = 21
    for p in planets:
        planet(p)
        for _ in range(0, srange):
            time.sleep(0.5 + random.random())
            im = screen_grab()
            for i in range(1, 16):
                tc = galaxy.targetcolor(i, im)
                print(i, tc)
                if galaxy.is_target(tc, galaxy.TARGET_BLUE_min, galaxy.TARGET_BLUE_max) or galaxy.is_target(tc, galaxy.TARGET_PURPLE_min, galaxy.TARGET_PURPLE_max):
                    galaxy.spy(i, commit=commit)
            galaxy.system_up()
        planet(p)
        for _ in range(0, srange):
            galaxy.system_up(-1)
            time.sleep(0.5 + random.random())
            im = screen_grab()
            for i in range(1, 16):
                tc = galaxy.targetcolor(i, im)
                print(i, tc)
                if galaxy.is_target(tc, galaxy.TARGET_BLUE_min, galaxy.TARGET_BLUE_max) or galaxy.is_target(tc, galaxy.TARGET_PURPLE_min, galaxy.TARGET_PURPLE_max):
                    galaxy.spy(i, commit=commit)


def build_defenses(planets=range(1, 11), commit=True):
    # check that we are in the correct tab
    # go 10 galaxies back and print witch type of target it has
    defense.select()
    for p in planets:
        planet(p)
        for d in [defense.SMALL_SHIELD, defense.BIG_SHIELD]:
            defense.select(d)
            defense.build(commit=commit)

        for d in [defense.ANTIBALLISTIC, defense.PLASMA_TURRET, defense.GAUSS_CANNON, defense.HEAVY_LASER, defense.ROCKET_LAUNCHER]:
            defense.select(d)
            defense.build(n=0, commit=commit)
            reload()


def fleetsave(planets=range(1, 11)):
    for p in planets:
        planet(p)
        shipyard.select()
        shipyard.select(shipyard.RECYCLER)
        shipyard.build(10, build=False)




# wait to complete load


if __name__ == "__main__":
    screen_grab(save=True)
    spy(commit=False)
    fleetsave()
    pass 