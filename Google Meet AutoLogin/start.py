from datetime import datetime
import pyautogui, time
from pynput.keyboard import Controller,Key
from data import lst
import webbrowser

keyboard = Controller()

isStarted = False

for i in lst:
    while True:
        if isStarted==False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                for i in range(1):
                    cords1 = (688, 775) # change all co-ordinates depending on your screen size
                    cords2 = (776, 776) # I have used a 1920*1080p monitor for example
                    cords3 = (1271, 611)
                    cords4 = (1641, 114)

                    time.sleep(5)
                    pyautogui.leftClick(cords1)
                    time.sleep(3)
                    pyautogui.leftClick(cords2)
                    time.sleep(2)
                    pyautogui.leftClick(cords3)
                    time.sleep(60)
                    pyautogui.leftClick(cords4)
                    isStarted = True
                    exec(open("exit.py").read())