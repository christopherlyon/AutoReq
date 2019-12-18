import pyautogui
from os import system
import time
from playsound import playsound

playsound("AutoReq/Done_alert.mp3")

system("cls")
print("Capturing in 2 second")



time.sleep(2)
Where = pyautogui.position()
print(Where)
