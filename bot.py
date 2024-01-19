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
import menu
import galaxy 
import defence
import fleet
import shipyard
import menu

from ships import LARGE_CARGO
from base import l_wait, m_wait, xs_wait

def spy(planets=range(1, 11), commit=True):
    start = time.time()
    srange = 21
    for p in planets:
        menu.planet(p)
        galaxy.spy_all(commit=commit)
        for _ in range(0, srange):
            galaxy.system_up()
            time.sleep(1 + random.random()/2)
            galaxy.spy_all(commit=commit)
        menu.planet(p, forced=True)
        for _ in range(0, srange):
            galaxy.system_up(-1)
            time.sleep(0.5 + random.random())
            galaxy.spy_all(commit=commit)
        menu.go(menu.MSSG)
    end = time.time()
    dtime = end - start
    print(f"spy total duration: {dtime/60:.1f} min")
    return dtime

def build_defences(planets=range(1, 11), commit=True):
    # check that we are in the correct tab
    # go 10 galaxies back and print witch type of target it has
    start = time.time()
    for p in planets:
        menu.planet(p)
        for d in [defence.SMALL_SHIELD, defence.LARGE_SHIELD, defence.ANTIBALLISTIC_MISSILE]:
            defence.build(d, commit=commit)

    for d in [defence.PLASMA_TURRET, defence.GAUSS_CANNON, defence.HEAVY_LASER, defence.ROCKET_LAUNCHER]:
        for p in planets:
            menu.planet(p)
            defence.build(item=d, n=0, commit=commit)
    end = time.time()
    dtime = end-start
    print(f"build defences total duration: {dtime/60:.1f} min")
    return dtime
        
def fleetsave_recall(hours, minutes=0, commit=True, build_lc = False):
    print(f"--- initiating fleetsaving at {time.asctime()} for {hours:02d}h{minutes:02d} ---")
    start= time.time()
    if commit:
        proc.init()
    l_wait()
    # calcular cuantas LC necesito de más
    if build_lc:
        max_buildt = 1
        for p in fleet.FLEETLOGIC_FS1GX:
            menu.planet(*p)
            res = menu.resources()
            needed_lc = int((res["metal"] + res["crystal"] + res["deuterium"]) / LARGE_CARGO.cargo)
            xs_wait(wait=True)
            shipyard.update_number()
            print(f" planet {p}: res= {res}, total_lc={needed_lc}, available={LARGE_CARGO.number}")
            # construir en caso necesario
            if LARGE_CARGO.number < needed_lc:
                build_lc = 0 if LARGE_CARGO.number > needed_lc else ((needed_lc- LARGE_CARGO.number)//100 + 1)*100
                build_t = build_lc * LARGE_CARGO.build_s
                shipyard.build(LARGE_CARGO, n=build_lc, commit=commit)
                print(f"building {build_lc} large cargos in {build_t/60:.2f} min")
                m_wait()
                max_buildt = max(max_buildt, build_t)
        if commit:
            time.sleep(max_buildt)
    fleet.move(fleet.FLEETLOGIC_FS1GX, fleet.FLEETCOMP_ALL, speed=1, commit=commit) 
    end = time.time()
    dtime = end-start
    print(f"fleetsave and LC build total duration: {dtime/60:.1f} min")
    t_waiting = (hours*3600 + minutes*60 - dtime)//2 
    if t_waiting < 60*10:
        t_waiting = 60*10
    recall_dt = datetime.datetime.now() + datetime.timedelta(seconds=t_waiting)
    print(f"fleet recall scheduled at {recall_dt.strftime('%a %b %d %H:%M:%S %Y')}") 
    if not commit:
        return
    proc.end()
    time.sleep(t_waiting)
    proc.init()
    fleet.recall(commit=commit)
    proc.end()

def auto_defence(hours, commit=True):
    while(True):
        for h in hours:
            while(h != datetime.datetime.now().hour):
                time.sleep(600)
            time.sleep(random.randrange(1, 1800))
            print(f"--- Starting auto defence at {time.asctime()} ----")
            start = time.time()
            proc.init()
            l_wait()
            #random_actions(40)
            build_defences(commit=commit)
            #random_actions(10)
            l_wait()
            end = time.time()
            dtime = end-start
            proc.end()
            print(f"total duration: {dtime/60:.1f} min")


if __name__ == "__main__":
    #spy(commit=False)
    pass