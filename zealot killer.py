import pyautogui
import time
import win32api, win32con


def click():
    for x in range(5):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.06)


while True:
    mousePos = pyautogui.position()
    i,j = mousePos[0], mousePos[1]
    pxl = pyautogui.pixel(i, j)

    if pxl[1] <= 10:
        if pxl[2] <= 10:
            if pxl[0] > 20:
                print("red")
                click()
            else:
                pass
    else:
        i1 = i - 3
        j1 = j - 3
        pic = pyautogui.screenshot(region=(i1, j1, 6, 6))
        width, height = pic.size
        for x in range(0, width, 5):
            for y in range(0, height, 5):
                r,g,b = pic.getpixel((x,y))

                if g <= 10:
                    if b <= 10:
                        if r > 20:
                            print("red")
                            click()

