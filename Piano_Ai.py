import pyautogui
import time
import keyboard
import win32api, win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02);
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


cons = [300,400,500,600]
y = 500;
while keyboard.is_pressed("q")==False:
        if pyautogui.pixel(cons[0], y)[0] == 0:
            click(cons[0], y);
        if pyautogui.pixel(cons[1], y)[0] == 0:
            click(cons[1], y);
        if pyautogui.pixel(cons[2], y)[0] == 0:
            click(cons[2], y);
        if pyautogui.pixel(cons[3], y)[0] == 0:
            click(cons[3], y);

pyautogui.displayMousePosition();

