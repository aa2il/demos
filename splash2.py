#! /usr/bin/python3

# Script to test splash screens - a different approach

import sys
import tkinter as tk
import time


class SIMPLE_GUI():
    def __init__(self):

        # create the main window & start off hidden
        self.root = tk.Tk()
        self.root.withdraw()
        self.root.geometry('500x500')
        self.root.withdraw()

        # Create splash screen
        self.splash  = tk.Toplevel(self.root)
        self.splash.title("Splish Splash")

        # disable the window bar
        self.splash.overrideredirect(1)
        self.splash.geometry('+500+500')

        # set the background image
        pic = tk.PhotoImage(file='splash.png')
        lab=tk.Label(self.splash, bg='white', image=pic)
        lab.pack()
        self.splash.update()
        self.splash.deiconify()

        # Simulate doing rest of inits
        time.sleep(2)

        # move root window to center & show it
        self.root.eval('tk::PlaceWindow . Center')
        self.root.update()
        self.root.deiconify()

        # Destroy splash screen
        time.sleep(.1)
        self.splash.destroy()

# Create simple gui        
GUI=SIMPLE_GUI()       

# run the main loop
GUI.root.mainloop()
