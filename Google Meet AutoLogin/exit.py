from datetime import datetime
import pyautogui, time
from pynput.keyboard import Controller,Key
from data import lst
import webbrowser

keyboard = Controller()

isStarted = False

for i in lst:
    while True:
        if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
            for i in range(1):
                cords5 = (777, 1027) # change all co-ordinates depending on your screen size
                cords6 = (777, 1027) # I have used a 1920*1080p monitor for example
                cords7 = (1006, 289)

                time.sleep(2)
                pyautogui.leftClick(cords5)
                time.sleep(2)
                pyautogui.leftClick(cords6)
                time.sleep(2)
                pyautogui.leftClick(cords7)
                isStarted = False
                break
