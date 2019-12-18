import pyautogui
from os import system
import time
import webbrowser
from datetime import date
from playsound import playsound


system("cls")

# Setting some variables
# ------------------------------------------------

today = date.today()

Day_as_int = int(today.strftime("%d"))
Todays_date = today.strftime("/%m/%Y")

Day_plus_7 = Day_as_int + 7

if Day_plus_7 > 30:
    Day_plus_7 = 30

Requisition_link = "https://fsprd.oii.oceaneering.com/psc/FSPRD/EMPLOYEE/ERP/c/NUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL?CONTEXTIDPARAMS=TEMPLATE_ID%3aPTPPNAVCOL&scname=ADMN_OII_REQUISITIONING&PanelCollapsible=Y&PTPPB_GROUPLET_ID=OII_REQUISITION&CRefName=ADMN_NAVCOLL_9"



# Program Start
# ------------------------------------------------

Project = input("Project number? ")
Activity = input("Activity number? ")
#print("Setting req to", Project, "on activity number", Activity)

#webbrowser.open(Requisition_link) #Open Tab

pyautogui.click(2748, 419)   #Click Req
time.sleep(2)

pyautogui.click(2272, 425)   #Click Add
time.sleep(1)

pyautogui.click(2493, 517)   #Click Defaults
time.sleep(1)

pyautogui.click(2222, 422)          #Click Buyer
pyautogui.typewrite("CREINSKAU")
time.sleep(0.1)

pyautogui.click(2222, 500)          #Click Category
pyautogui.typewrite("39000000")
time.sleep(0.1)

pyautogui.click(2222, 600)          #Click Date
pyautogui.typewrite(Todays_date)
time.sleep(0.1)

pyautogui.click(2869, 423)          #Click Measure
pyautogui.typewrite("EA")
time.sleep(0.1)

pyautogui.click(2377, 992)          #Click Account
pyautogui.typewrite("5110")
time.sleep(0.1)

pyautogui.click(2524, 989)          #Click Dept
time.sleep(1)
pyautogui.typewrite("3468")
time.sleep(0.3)

pyautogui.click(2765, 992)          #Click PC Bus Unit
time.sleep(0.1)
pyautogui.typewrite("B0571")
time.sleep(0.1)

pyautogui.click(2866, 985)          #Click Project
pyautogui.typewrite(Project)
time.sleep(0.1)

pyautogui.click(3060, 985)          #Click Activity
pyautogui.typewrite(Activity)
time.sleep(0.1)

pyautogui.click(3194, 985)          #Click Source Type
pyautogui.typewrite("5110")

pyautogui.click(3308, 992)          #Click Source Type
pyautogui.typewrite("MATO")

pyautogui.click(2037, 1041)         #Click OK


playsound("AutoReq/Done_alert.mp3") # DING DING


# pyautogui.click(2019, 183)          #Click Whitespace



# pyautogui.click(2019, 183)          #