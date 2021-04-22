'''
Below are the required libraries needed for the script to run, read the man page for further help!!
'''
import time
from datetime import datetime
import pyautogui
from pynput.keyboard import Controller
from data import lst
import webbrowser

keyboard = Controller()
isStarted = False

for i in lst:
    while True:
        if isStarted == False:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                isStarted = True
                cords1 = (2365, 780) #Change these to your needed co-ordinates
                cords2 = (2869, 643)
                cords3 = (3250, 185)

                time.sleep(4)
                pyautogui.leftClick(cords1)
                time.sleep(2)
                pyautogui.leftClick(cords2)
                time.sleep(10)
                pyautogui.leftClick(cords3)
        elif isStarted == True:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                isStarted = False
                cords4 = (3491, 195)
                cords5 = (2560, 1035)
                cords6 = (2602, 357)
                cords7 = (3509, 57)

                pyautogui.leftClick(cords4)
                time.sleep(2)
                pyautogui.leftClick(cords5)
                time.sleep(2)
                pyautogui.leftClick(cords6)
                time.sleep(2)
                pyautogui.leftClick(cords7)
                break
