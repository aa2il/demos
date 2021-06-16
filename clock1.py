#!/usr/bin/python3

import sys
if sys.version_info[0]==3:
    import tkinter as tk
else:
    import Tkinter as tk
import time

def update_timeText():
    # Get the current time, note you can change the format as you wish
    current = time.strftime("%H:%M:%S")
    # Update the timeText Label box with the current time
    timeText.configure(text=current)
    # Call the update_timeText() function after 1 second
    print("tic")
    root.after(1000, update_timeText)
    print("toc")

root = tk.Tk()
root.wm_title("Simple Clock Example")

# Create a timeText Label (a text box)
timeText = tk.Label(root, text="", font=("Helvetica", 150))
timeText.pack()
update_timeText()
root.mainloop()
