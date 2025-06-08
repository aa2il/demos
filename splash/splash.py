#!/usr/bin/env -S uv run --script

#! /usr/bin/python3

# Script to test splash screens

import sys
import tkinter as tk

# create the main window
root = tk.Tk()
win  = tk.Toplevel(root)

# disable the window bar
#win.overrideredirect(1)
win.title("Splish Splash")

# set trasparency and make the window stay on top
# This doesn't work
#root.attributes('-transparentcolor', 'white', '-topmost', True)
if sys.platform == "linux" or sys.platform == "linux2":
    # linux
    win.attributes("-topmost", True,'-type', 'splash')
elif sys.platform == "win32":
    # Windows...
    win.attributes("-topmost", True)
elif sys.platform == "darwin":
    # OS X
    print('No support for Mac OS')
    sys.exit(0)

# set the background image
#labtk.Label(text='Hey')
pic = tk.PhotoImage(file='splash.png')
#pic = tk.PhotoImage(file='splash.jpg')
lab=tk.Label(win, bg='white', image=pic)
lab.pack()

# move the window to center
root.eval('tk::PlaceWindow . Center')

# schedule the window to close after 4 seconds
win.after(4000, win.destroy)

# run the main loop
root.mainloop()
