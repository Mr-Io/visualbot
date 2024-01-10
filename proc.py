import webbrowser

import pyautogui

import base


def init():
    # open browser
    webbrowser.get('firefox').open("https://lobby.ogame.gameforge.com/en_GB/hub",
                                   new=1, 
                                   autoraise=True)
    base.l_wait()

    # move browser window
    pyautogui.keyDown('shift')
    pyautogui.keyDown('win')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.keyUp('win')
    pyautogui.keyUp('shift')

    # login
    pyautogui.scroll(-10)
    logb = pyautogui.locateCenterOnScreen("images/play.png")
    pyautogui.moveTo(*logb, 0.4)
    pyautogui.click()
    base.m_wait()
    pyautogui.moveTo(base.X_PAD+1390, base.Y_PAD+385, base.xs_wait())
    pyautogui.click()
    base.l_wait()


def end():
    # close browser
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.moveTo(1240, 1200, base.xs_wait())
    pyautogui.click()

def test():
    pyautogui.click(base.X_PAD+100,base.Y_PAD+200)
    base.back()



