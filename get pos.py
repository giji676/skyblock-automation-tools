import win32api, win32con
import threading
import pyautogui
import keyboard
import time

time.sleep(2)

mousePos = pyautogui.position()
x, y = mousePos[0], mousePos[1]

pic = pyautogui.screenshot(region=(x, y, 60, 19))
pic.save(r"C:\Users\tvten\PycharmProjects\auto clicker\savedServer.png")
print("saved pick")
print()

time.sleep(2)

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
keyboard.press("shift")
keyboard.press("w")

a = "a"
d = "d"

###### 315 speed
run = True

def checkServer():
    global run
    #1813, 410, 1882, 428
    while run:
        if pyautogui.locateOnScreen("savedServer.png") != None:
            print("yes")
            pass
        else:
            print("no-")
            run = False
            keyboard.release(d)
            keyboard.release(a)
            keyboard.release("shift")
            keyboard.release("w")
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

            exit()
        time.sleep(5)

def farm():
    global run
    while run:
        keyboard.press(d)
        time.sleep(43.5)
        keyboard.release(d)
        keyboard.press(a)
        time.sleep(43.6)
        keyboard.release(a)


threading.Thread(target=checkServer).start()
threading.Thread(target=farm).start()
