#! /usr/bin/python3

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
win.attributes("-topmost", True,'-type', 'splash')

# set the background image
#labtk.Label(text='Hey')
pic = tk.PhotoImage(file='splash.png')
lab=tk.Label(win, bg='white', image=pic)
lab.pack()

# move the window to center
root.eval('tk::PlaceWindow . Center')

# schedule the window to close after 4 seconds
win.after(4000, win.destroy)

# run the main loop
root.mainloop()
