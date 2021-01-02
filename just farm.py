import win32api, win32con
import keyboard
import time

time.sleep(2)

def mainClicks():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    keyboard.press("shift")
    keyboard.press("w")

mainClicks()

a = "a"
d = "d"

###### 315 speed
run = True


def farm():
    global run
    while run:
        keyboard.press(d)
        time.sleep(43.5)
        keyboard.release(d)
        mainClicks()
        keyboard.press(a)
        time.sleep(43.6)
        keyboard.release(a)

farm()
