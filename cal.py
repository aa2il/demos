#!/usr/bin/python3
################################################################################
#
# Date picker demo using tk
#
# pip3 install tkcalendar
#
################################################################################

import sys
if sys.version_info[0]==3:
    import tkinter as tk
else:
    import Tkinter as tk
import time
from tkcalendar import *

################################################################################

# Create window
win= tk.Tk()
win.title("Calendar")
#win.geometry("700x600")

# Calendar widget
#cal= Calendar(win, selectmode="day",year= 2021, month=3, day=3)
cal= Calendar(win, selectmode="day")      # Defaults to current day
cal.pack(pady=20)

# Function to select the date
def get_date():
   label.config(text=cal.get_date())

# Button to pick the date from the calendar
button= tk.Button(win, text= "Select the Date", command= get_date)
button.pack(pady=20)

# Label for displaying selected Date
label= tk.Label(win, text="")
label.pack(pady=20)

win.mainloop()
