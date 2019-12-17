import pyautogui
from os import system
import time


system("cls")
print("Capturing in 2 second")
time.sleep(2)
Where = pyautogui.position()
print(Where)
