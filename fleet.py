import time
import pyautogui

import menu

from base import xs_wait, s_wait, m_wait, enter, copy

from ships import LIGHT_FIGHTER, HEAVY_FIGHTER, CRUISER, BATTLESHIP, BATTLECRUISER, BOMBER, DESTROYER, RIP, SMALL_CARGO, LARGE_CARGO, COLONYSER, RECYCLER, ESP_PROBE, ALL_SHIPS

FLEETLOGIC_ALLI2 = {(1, False): (2, True),
                    (2, False): (2, True),
                    (3, False): (2, True),
                    (4, False): (2, True),
                    (5, False): (2, True),
                    (6, False): (2, True),
                    (7, False): (2, True),
                    (8, False): (2, True),
                    (9, False): (2, True),
                    (10, False):(2, True),
                    }

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

FLEETCOMP_ALL = ((ALL_SHIPS, None),)

EMPTYMOOMS = {(1, True): (1, False),
              (2, True): (2, False),
              (3, True): (3, False),
              (4, True): (4, False),
              (5, True): (5, False),
              (6, True): (6, False),
              (7, True): (7, False),
              (8, True): (8, False),
              (9, True): (9, False),
              (10, True): (10, False),
              }

@menu.menu(menu.FLEET)
def _select(ship=None, n=None):
    if ship is None:
        return
    try: 
        x, y = pyautogui.locateCenterOnScreen(ship.img)
    except:
        print(f"{ship} not available")
        return
    if n is None:
        pyautogui.moveTo(x, y, xs_wait())
        pyautogui.click()
    else:
        pyautogui.moveTo(x, y+45, xs_wait())
        pyautogui.doubleClick()
        pyautogui.typewrite(f"{n}")

@menu.menu(menu.FLEET)
def _number(ship):
    try: 
        x, y = pyautogui.locateCenterOnScreen(ship.img, confidence=0.98) 
    except:
        return -1
    pyautogui.moveTo(x, y+45) #xs_wait())
    print(x, y)
    pyautogui.doubleClick()
    res = copy()
    return -1 if res == '' else int(res)

def get():
    res = {}
    _select(item=ALL_SHIPS)
    res[LIGHT_FIGHTER] = _number(LIGHT_FIGHTER)
    res[HEAVY_FIGHTER] = _number(HEAVY_FIGHTER)
    res[CRUISER] = _number(CRUISER)
    res[BATTLESHIP] = _number(BATTLESHIP)
    res[BATTLECRUISER] = _number(BATTLECRUISER)
    res[BOMBER] = _number(BOMBER)
    res[DESTROYER] = _number(DESTROYER)
    res[RIP] = _number(RIP)
    res[SMALL_CARGO] = _number(SMALL_CARGO)
    res[LARGE_CARGO] = _number(LARGE_CARGO)
    res[COLONYSER] = _number(COLONYSER)
    res[RECYCLER] = _number(RECYCLER)
    res[ESP_PROBE] = _number(ESP_PROBE)
    return res

def _shortcut(planet, moon=False):
    x, y = pyautogui.locateCenterOnScreen("images/arrow_down_green.png")
    pyautogui.click(x, y)
    s_wait(wait=True)
    x, y = pyautogui.locateCenterOnScreen("images/shortcut_coldsens.png", confidence=0.99)
    if moon:
        x += 75
    y += (planet-1)*25
    pyautogui.moveTo(x, y, xs_wait())
    pyautogui.click()


def _send(speed=10, commit=True, resources=False):
    x, y = pyautogui.locateCenterOnScreen("images/speed_10.png")
    x += (speed-1)*62
    pyautogui.moveTo(x, y, xs_wait())
    pyautogui.click()
    if resources:
        _resources()
    if commit:
        enter()

def _resources():
    x, y = pyautogui.locateCenterOnScreen("images/fleet_all_resources.png")
    pyautogui.moveTo(x, y, xs_wait())
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
        menu.planet(*p)
        _select()
        try: 
            pyautogui.locateOnScreen("images/no_ships.png")
        except pyautogui.ImageNotFoundException:
            for f in fleetcomp:
                _select(*f)
            enter()
            _shortcut(*fleetlogic[p])
            s_wait()
            _send(speed, commit, resources=True)
            m_wait()
        else:
            print("ERROR: No fleet on planet")

 