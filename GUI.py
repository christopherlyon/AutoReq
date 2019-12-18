from tkinter import *
from playsound import playsound

master = Tk() 
master.title('AutoReq V1') 

def printit():
    print("Project Number: %s\nActivity Number: %s" % (Project.get(), Activity.get()))
    master.destroy()



Label(master, text='Project Number').grid(row=0) 
Label(master, text='Activity Number').grid(row=1) 
Project = Entry(master) 
Activity = Entry(master) 
Project.grid(row=0, column=1) 
Activity.grid(row=1, column=1) 

button = Button(master, width = 30, text='Start', command=printit, bg="blue") 
button.grid(row=3, columnspan = 2,padx = 1, pady = 1)


mainloop()

#print("Value of IntVar()", intvar.get()) 

