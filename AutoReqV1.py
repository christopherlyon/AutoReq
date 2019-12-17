import pyautogui
from os import system
import time
import webbrowser
from datetime import date

today = date.today()
Todays_date = today.strftime("%d/%m/%Y")

system("cls")


Requisition_link = "https://fsprd.oii.oceaneering.com/psc/FSPRD/EMPLOYEE/ERP/c/NUI_FRAMEWORK.PT_AGSTARTPAGE_NUI.GBL?CONTEXTIDPARAMS=TEMPLATE_ID%3aPTPPNAVCOL&scname=ADMN_OII_REQUISITIONING&PanelCollapsible=Y&PTPPB_GROUPLET_ID=OII_REQUISITION&CRefName=ADMN_NAVCOLL_9"

Project = input("Project number? ")
Activity = input("Activity number? ")
#print("Setting req to", Project, "on activity number", Activity)

#webbrowser.open(Requisition_link) #Open Tab

#pyautogui.click(2748, 419)   #Click Req
#pyautogui.click(2272, 425)   #Click Add


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
pyautogui.typewrite("3468")
time.sleep(0.1)

pyautogui.click(2755, 989)          #Click PC Bus Unit
pyautogui.typewrite("B0571")
time.sleep(0.1)

pyautogui.click(2866, 985)          #Click Project
pyautogui.typewrite(Project)
time.sleep(0.1)

pyautogui.click(3060, 985)          #Click Activity
pyautogui.typewrite(Activity)
time.sleep(0.1)

pyautogui.click(3194, 985)          #Click Account
pyautogui.typewrite("5110")

# pyautogui.click(2019, 183)          #Click Whitespace


pyautogui.click(3078, 196)          #Click Hours
pyautogui.typewrite("5110")

# pyautogui.click(2019, 183)          #