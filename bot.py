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

import proc
import galaxy 
import defence
import fleet
from base import m_wait, l_wait
from menu import menu, planet

def spy(planets=range(1, 11), commit=True):
    start = time.time()
    srange = 21
    for p in planets:
        planet(p)
        galaxy.spy_all(commit=commit)
        for _ in range(0, srange):
            galaxy.system_up()
            time.sleep(1 + random.random()/2)
            galaxy.spy_all(commit=commit)
        planet(p, forced=True)
        for _ in range(0, srange):
            galaxy.system_up(-1)
            time.sleep(0.5 + random.random())
            galaxy.spy_all(commit=commit)
    end = time.time()
    dtime = end - start
    print(f"spy total duration: {dtime/60:.1f} min")
    return dtime

def build_defenses(planets=range(1, 11), commit=True):
    # check that we are in the correct tab
    # go 10 galaxies back and print witch type of target it has
    start = time.time()
    for p in planets:
        planet(p)
        for d in [defence.SMALL_SHIELD, defence.BIG_SHIELD, defence.ANTIBALLISTIC]:
            defence.build(d, commit=commit)

    for d in [defence.PLASMA_TURRET, defence.GAUSS_CANNON, defence.HEAVY_LASER, defence.ROCKET_LAUNCHER]:
        for p in planets:
            planet(p)
            defence.build(item=d, n=0, commit=commit)
    end = time.time()
    dtime = end-start
    print(f"build defenses total duration: {dtime/60:.1f} min")
    return dtime
        
def auto_fleetsave_recall(hours, minutes=0, commit=True, defenses=True):
    print(f"--- initiating fleetsaving at {time.asctime()} for {hours:02d}h{minutes:02d} ---")
    start= time.time()
    if commit:
        proc.init()
    l_wait()
    fleet.move(fleet.FLEETLOGIC_FS1GX, fleet.FLEETCOMP_ALL, speed=1, commit=commit) 
    #fleet.move({(2, False): (10, True)}, ((fleet.RECYCLER, 1),), speed=1, commit=commit) #for test
    random_actions(10)
    end = time.time()
    dtime = end-start
    print(f"fleetsave total duration: {dtime/60:.1f} min")
    if not commit:
        return
    bd_time = build_defenses(commit=commit) if defenses else 0
    proc.end()
    t_waiting = (hours*3600 + minutes*60)//2 - bd_time - dtime
    time.sleep(t_waiting if t_waiting > 30 else 30)
    proc.init()
    fleet.recall(commit=commit)
    proc.end()


def random_actions(n=10):
    actions = ((lambda: 0 ),)
    n_actions = 0
    n = random.randrange(1, n)

    while (True): 
        p = random.randrange(1, 11)
        planet(p)
        for _ in range(0, random.randrange(1, 7)):
            act = random.choice(actions)
            n_actions += 1
            #print(f"action: nº {n_actions} - {act[0].__module__}")
            act[0]()
            time.sleep(random.randrange(1, act[1]))
        if n_actions > n:
            return

def auto_defense(hours, commit=True):
    while(True):
        for h in hours:
            while(h != datetime.datetime.now().hour):
                time.sleep(600)
            time.sleep(random.randrange(1, 1800))
            print(f"--- Starting auto defense at {time.asctime()} ----")
            start = time.time()
            proc.init()
            l_wait()
            random_actions(40)
            build_defenses(commit=commit)
            random_actions(10)
            l_wait()
            end = time.time()
            dtime = end-start
            proc.end()
            print(f"total duration: {dtime/60:.1f} min")



# wait to complete load


if __name__ == "__main__":
    #spy(commit=False)
    pass