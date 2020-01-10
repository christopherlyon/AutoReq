import pyautogui
from os import system
import time
from playsound import playsound


system("cls")
print("Capturing in 2 second")

pyautogui.click(2272, 425)   #Click Add


time.sleep(2)
Where = pyautogui.position()
print(Where)
