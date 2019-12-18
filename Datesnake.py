from os import system
import time
from datetime import date


today = date.today()

Day_as_int = int(today.strftime("%d"))
Todays_date = today.strftime("/%m/%Y")

Day_plus_7 = Day_as_int + 7

if Day_plus_7 > 30:
    Day_plus_7 = 30

print(Day_plus_7, Todays_date, sep="")

# WORKING #