import time
import pyautogui

from base import X_PAD, Y_PAD, xs_wait, s_wait, m_wait, enter
from menu import menu, MENU_FLEET, planet

LIGHT_FIGHTER = (605, 222)
HEAVY_FIGHTER = (685, 222)
CRUISER = (765, 222)
BATTLESHIP = (845, 222)
BATTLECRUISER = (925, 222)
BOMBER = (605, 300)
DESTROYER = (685, 300)
RIP = (765, 300)
REAPER = (845, 300)
PATHFINDER = (925, 300)
SMALL_CARGO = (1020, 222)
LARGE_CARGO = (1100, 222)
COLONYSER = (1180, 222)
RECYCLER = (1020, 300)
ESP_PROBE = (1100, 300)
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

@menu(MENU_FLEET)
def _select(item=None, n=None):
    if item is None:
        return
    elif isinstance(item, str):
        x, y = pyautogui.locateCenterOnScreen(item) 
    else:
        x, y = (X_PAD+item[0], Y_PAD+item[1])
    if n is None:
        pyautogui.moveTo(x, y, xs_wait())
        pyautogui.click()
    else:
        pyautogui.moveTo(x, y+45, xs_wait())
        pyautogui.doubleClick()
        pyautogui.typewrite(f"{n}")

def _shortcut(planet, moon=False):
    pyautogui.moveTo(X_PAD+1183, Y_PAD+232, xs_wait())
    pyautogui.click()
    x = 1015 if moon else 935
    y = 345 + planet*25
    pyautogui.moveTo(X_PAD+x, Y_PAD+y, xs_wait())
    pyautogui.click()


def _send(speed=10, commit=True, resources=False):
    x = 553+speed*62
    pyautogui.moveTo(X_PAD+x, Y_PAD+716, xs_wait())
    pyautogui.click()
    if resources:
        _resources()
    if commit:
        enter()

def _resources():
    pyautogui.moveTo(X_PAD+1140, Y_PAD+516, xs_wait())
    pyautogui.click()
    xs_wait(wait=True)
   
def recall(commit=True):
    # no need to be on galaxy!
    # clickar despliegue
    desb = pyautogui.locateCenterOnScreen("images/fleet_details.png")
    pyautogui.moveTo(*desb, xs_wait(wait=False))
    pyautogui.click()
    s_wait()
    # pinchar recall
    count = 0
    while(True):
        try:
            recb = pyautogui.locateCenterOnScreen("images/recall.png")
        except pyautogui.ImageNotFoundException:
            print(f"--- {count} fleets recalled successfully at {time.asctime()} ---")
            return
        pyautogui.moveTo(*recb, xs_wait(wait=False))
        pyautogui.click()
        s_wait()
        reyb = pyautogui.locateCenterOnScreen("images/recall_yes.png")
        pyautogui.moveTo(*reyb, xs_wait(wait=False))
        if commit:
            pyautogui.click()
        else:
            pyautogui.press("esc")
        count += 1
        s_wait()
        if not commit and count > 3:
            return
    # es posible que sea necesario scrollear

def move(fleetlogic=FLEETLOGIC_FS1GX, fleetcomp=FLEETCOMP_ALL, speed=6, commit=True):
   for p in fleetlogic:
        planet(*p)
        _select()
        if pyautogui.pixel(X_PAD+821, Y_PAD+187) == (176, 0, 0):
            print("ERROR: No fleet on planet")
            continue
        for f in fleetcomp:
            _select(*f)
        enter()
        _shortcut(*fleetlogic[p])
        s_wait()
        _send(speed, commit, resources=True)
        m_wait()
 