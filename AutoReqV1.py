import pyautogui
from os import system
import time
import webbrowser
from datetime import date
from playsound import playsound
from tkinter import *



# Setting some variables
# ------------------------------------------------

today = date.today()

Day_as_int = int(today.strftime("%d"))
Todays_date = today.strftime("/%m/%Y")

Day_plus_7 = Day_as_int + 7

if Day_plus_7 > 30:
    Day_plus_7 = 30

New_Req_Date = str(Day_plus_7) + str(Todays_date)

Requisition_link = "https://fsprd.oii.oceaneering.com/psc/FSPRD/EMPLOYEE/ERP/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL"


# Program Start
# ------------------------------------------------

master = Tk() 
master.title('AutoReq V1') 
master.configure(bg = '#000000')

Project_global = 0
Activity_global = 0

var = IntVar()

def Run_program():

    global Project_global
    global Activity_global

    Project_global = Project.get()
    Activity_global = Activity.get()
    master.destroy()

# Label

Label(master, text='Project Number', bg ="#2d2d2d", fg = "white").grid(row=0, padx=(20,10), pady=(20,10)) 
Label(master, text='Activity Number', bg ="#2d2d2d", fg = "white").grid(row=1, padx=(20,10), pady=(10,10)) 

# Entry

Project = Entry(master, width = 20)
Activity = Entry(master, width = 20)
Project.grid(row=0, column=1, padx=(0,20), pady=(20,10)) 
Activity.grid(row=1, column=1, padx=(0,20), pady=(10,10)) 

# Checkbutton

Logged_in_check = Checkbutton(master, variable=var, bg ="#2d2d2d").grid(row=3, padx=(20,10), pady=(10,10))

# Button

button = Button(master, width = 30, text='Start', command=Run_program, bg ="#2d2d2d", fg = "white") 
button.grid(row=4, columnspan = 2, pady=(10,20))


mainloop()

print(var.get())

if var.get() == 1:
    exit

else:

    pass
    webbrowser.open(Requisition_link)
    time.sleep(2)

    pyautogui.click(2748, 419)   #Click Req
    time.sleep(2.5)

    pyautogui.keyDown("alt")
    pyautogui.press("1")
    pyautogui.keyUp("alt")

    pyautogui.click(2272, 425)   #Click Add
    time.sleep(1.5)

    pyautogui.click(2493, 517)   #Click Requsition Defaults
    time.sleep(1)

    pyautogui.click(2222, 422)          #Click Buyer
    pyautogui.typewrite("CREINSKAU")
    time.sleep(0.1)

    pyautogui.click(2222, 500)          #Click Category
    pyautogui.typewrite("39000000")
    time.sleep(0.1)

    pyautogui.click(2222, 600)          #Click Date
    print(Day_plus_7, Todays_date, sep="")
    pyautogui.typewrite(New_Req_Date)
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
    pyautogui.typewrite(Project_global)
    time.sleep(0.1)

    pyautogui.click(3060, 985)          #Click Activity
    pyautogui.typewrite(Activity_global)
    time.sleep(0.1)

    pyautogui.click(3194, 985)          #Click Source Type
    pyautogui.typewrite("5110")

    pyautogui.click(3308, 992)          #Click Source Type
    pyautogui.typewrite("MATO")

    pyautogui.click(2037, 1041)         #Click OK
    time.sleep(1)

    pyautogui.click(2911, 824)         #Click Quantity
    pyautogui.press("backspace")
    pyautogui.typewrite("1")

    pyautogui.click(3340, 824)         #Click Price
    pyautogui.press("backspace")
    pyautogui.typewrite("999")

    pyautogui.click(2454, 927)         #Click Refresh


    playsound("AutoReq/Done_alert.mp3") # DING DING
    time.sleep(1)
