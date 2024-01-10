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
import datetime
import time
import random

import pyautogui

import base 
import proc
import galaxy 
import defense
import shipyard 
import fleet

MENU_OVERVIEW = "MENU_OVERVIEW"

def overview():
    if base.menu_location != MENU_OVERVIEW:
        base.menu_location = MENU_OVERVIEW
        pyautogui.moveTo(base.X_PAD+455, base.Y_PAD+305, base.xs_wait())
        pyautogui.click()
        base.m_wait()

def spy(planets=range(1, 11), commit=True):
    srange = 21
    for p in planets:
        base.planet(p)
        galaxy.spy_all(commit=commit)
        for _ in range(0, srange):
            galaxy.system_up()
            time.sleep(1 + random.random()/2)
            galaxy.spy_all(commit=commit)
        base.planet(p)
        for _ in range(0, srange):
            galaxy.system_up(-1)
            time.sleep(0.5 + random.random())
            galaxy.spy_all(commit=commit)

def build_defenses(planets=range(1, 11), commit=True):
    # check that we are in the correct tab
    # go 10 galaxies back and print witch type of target it has
    start = time.time()
    for p in planets:
        base.planet(p)
        for d in [defense.SMALL_SHIELD, defense.BIG_SHIELD, defense.ANTIBALLISTIC]:
            defense.build(d, commit=commit)

    for d in [defense.PLASMA_TURRET, defense.GAUSS_CANNON, defense.HEAVY_LASER, defense.ROCKET_LAUNCHER]:
        for p in planets:
            base.planet(p)
            defense.build(item=d, n=0, commit=commit)
    end = time.time()
    return end - start
        
def auto_fleetsave_recall(hours, minutes=0, commit=True, init=True):
    print(f"initiating fleetsaving at {time.asctime()} for {hours:02d}h{minutes:02d}")
    if init:
        proc.init()
    fleet.move(fleet.FLEETLOGIC_FS1GX, fleet.FLEETCOMP_ALL, speed=1, commit=commit) 
    bd_time = build_defenses(commit=commit)
    proc.end()

    t_waiting = (hours*3600 + min*60)/2 - bd_time 
    time.sleep(t_waiting if t_waiting > 0 else 1)

    proc.init()
    fleet.recall(commit=commit)

def random_actions(n=10):
    action = [(galaxy._select, 10), 
              (defense._select, 4), 
              (overview, 2), 
              (shipyard._select, 4), 
              (fleet._select, 2)]
    n_actions = 0
    n = random.randrange(1, n)

    while (True): 
        p = random.randrange(1, 11)
        base.planet(p)
        for _ in range(0, random.randrange(1, 7)):
            act = random.choice(action)
            n_actions += 1
            #print(f"action: nº {n_actions} - {act[0].__module__}")
            act[0]()
            time.sleep(random.randrange(1, act[1]))
        if n_actions > n:
            return

def auto_defense(hours=[6, 14, 22], commit=True):
    if hours is None:
        return
    
    while(True):
        for h in hours:
            while(h != datetime.datetime.now().hour):
                time.sleep(600)
            time.sleep(random.randrange(1, 1800))
            print(f"--- Starting auto defense at {time.asctime()} ----")
            start = time.time()
            proc.init()
            base.l_wait()
            random_actions(40)
            build_defenses(commit=commit)
            random_actions(10)
            base.l_wait()
            end = time.time()
            dtime = end-start
            proc.end()
            print(f"total duration: {dtime} s")



# wait to complete load


if __name__ == "__main__":
    #spy(commit=False)
    pass