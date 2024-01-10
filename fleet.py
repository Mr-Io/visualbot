import time
import pyautogui

import base

MENU_FLEET = "MENU_FLEET"

LIGHT_FIGHTER = (605, 455)
HEAVY_FIGHTER = (685, 455)
CRUISER = (765, 455)
BATTLESHIP = (845, 455)
BATTLECRUISER = (925, 455)
BOMBER = (605, 530)
DESTROYER = (685, 530)
RIP = (765, 530)
REAPER = (845, 530)
PATHFINDER = (925, 530)
SMALL_CARGO = (1020, 455)
LARGE_CARGO = (1100, 455)
COLONYSER = (1100, 455)
RECYCLER = (1020, 530)
ESP_PROBE = (1180, 530)
ALL_FLEET = "images/fleet_selectall.png"

FLEETLOGIC_FS1GX = {(1, False): (7, True),
                    (2, False): (7, True),
                    (3, False): (7, True),
                    (4, False): (7, True),
                    (5, False): (7, True),
                    (6, False): (7, True),
                    (7, False): (8, True),
                    (8, False): (7, True),
                    (9, False): (10, True),
                    (10, False): (9, True),
                    }

FLEETCOMP_EXAMPLE = ((LARGE_CARGO, 124),
                     (RECYCLER, 1),
                     (SMALL_CARGO, None))

FLEETCOMP_ALL = ((ALL_FLEET, None),)

EMPTYMOOMS = {(2, True): (2, False),
              (3, True): (3, False),
              (5, True): (5, False),
              (7, True): (7, False),
              (8, True): (8, False),
              (9, True): (9, False),
              (10, True): (10, False),
              }

def _select(item=None, n=None):
    if base.menu_location != MENU_FLEET:
        base.menu_location = MENU_FLEET
        pyautogui.moveTo(base.X_PAD+455, base.Y_PAD+510, base.xs_wait())
        pyautogui.click()
        #print("change menu to Fleet")
        base.m_wait()
    if item is None:
        return
    elif isinstance(item, str):
        x, y = pyautogui.locateCenterOnScreen(item) 
    else:
        x, y = (base.X_PAD+item[0], base.Y_PAD+item[1])
    if n is None:
        pyautogui.moveTo(x, y, base.xs_wait())
        pyautogui.click()
    else:
        pyautogui.moveTo(x, y+45, base.xs_wait())
        pyautogui.doubleClick()
        pyautogui.typewrite(f"{n}")

def _continue():
    pyautogui.moveTo(base.X_PAD+1160, base.Y_PAD+555, base.xs_wait())
    pyautogui.click()

def _shortcut(planet, moon=False):
    pyautogui.moveTo(base.X_PAD+1183, base.Y_PAD+377, base.xs_wait())
    pyautogui.click()
    x = 1015 if moon else 935
    y = 475 + planet*25
    pyautogui.moveTo(base.X_PAD+x, base.Y_PAD+y, base.xs_wait())
    pyautogui.click()


def _send(speed=10, commit=True):
    x = 553+speed*62
    pyautogui.moveTo(base.X_PAD+x, base.Y_PAD+860, base.xs_wait())
    pyautogui.click()
    pyautogui.moveTo(base.X_PAD+1070, base.Y_PAD+910, base.xs_wait())
    if commit:
        pyautogui.click()

def _resources():
    pyautogui.moveTo(base.X_PAD+1140, base.Y_PAD+660, base.xs_wait())
    pyautogui.click()
   
def recall(commit=True):
    # no need to be on galaxy!
    # clickar despliegue
    desb = pyautogui.locateCenterOnScreen("images/fleet_details.png")
    pyautogui.moveTo(*desb, base.xs_wait(wait=False))
    pyautogui.click()
    base.s_wait()
    # pinchar recall
    count = 0
    while(True):
        try:
            recb = pyautogui.locateCenterOnScreen("images/recall.png")
        except pyautogui.ImageNotFoundException:
            print(f"{count} fleets recalled successfully at {time.asctime()}")
            return
        pyautogui.moveTo(*recb, base.xs_wait(wait=False))
        pyautogui.click()
        base.s_wait()
        reyb = pyautogui.locateCenterOnScreen("images/recall_yes.png")
        pyautogui.moveTo(*reyb, base.xs_wait(wait=False))
        if commit:
            pyautogui.click()
        else:
            pyautogui.press("esc")
        count += 1
        base.s_wait()
        if not commit and count > 3:
            return
    # es posible que sea necesario scrollear

def move(fleetlogic=FLEETLOGIC_FS1GX, fleetcomp=FLEETCOMP_ALL, speed=6, commit=True):
   for p in fleetlogic:
        base.planet(*p)
        _select()
        if pyautogui.pixel(base.X_PAD+821, base.Y_PAD+331) == (176, 0, 0):
            print("ERROR: No fleet on planet")
            continue
        for f in fleetcomp:
            _select(*f)
        _continue()
        base.s_wait()
        _shortcut(*fleetlogic[p])
        base.s_wait()
        _resources()
        _send(speed, commit)
        base.m_wait()
 