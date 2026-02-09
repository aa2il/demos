#!/usr/bin/env -S uv run --script

#OLD: ! /usr/bin/python3

# A very simple Hello World using Tk.  Also used to figure out selection

# On the RPi, font rendering lloks like crap - pixelated.
# This is apparently due to the xft option is not enabled in tk ...
#    Well it is for the system python but not for the version under xv!
# Xft refers to the X Windows System Fontconfig TrueType font rendering extensio
# X-window Free Type?
# Below are various attempts to fix this problem ... nothing solid yet ...

import sys
"""
if sys.version_info[0]==3:
    from tkinter import *
    import tkinter.font
else:
    from Tkinter import *
    import tkFont
"""
import time

import tkinter as tk
import tkinter.font
#from tkinter_unblur import Tk
#import tkinter_unblur as tk

#from ctypes import windll

###############################################################################

def try_again(evt):
    print('Trying again ... evt num=',evt.num)
    txt = evt.widget.selection_get()
    print('TXT:',txt)

def Selection(evt):
    print('SELECTION: evt num=',evt.num)
    # Need to let the double click action complete before we
    # can get the selection
    root.after(10,lambda: try_again(evt) )

print('version=',sys.version_info)
    
root = tk.Tk()
#windll.shcore.SetProcessDpiAwareness(1)
#root.tk.call('tk', 'scaling', 2.0)

msg="Hello World! - Tk Version"
print(msg)

font_system = root.eval("tk::pkgconfig get fontsystem")
print(f"Tk font system: {font_system}")

FAMILY="monospace"
SIZE=28
fnt =  tkinter.font.Font(family=FAMILY,size=SIZE, weight="bold")

w = tk.Label(root, text=msg, font=fnt)
w.pack()

e = tk.Entry(root,fg='blue',selectbackground='white', font=fnt)
e.pack()
e.insert(0,"This is an Entry Box")

#t = Text(root,exportselection=True)
#t.pack()
#t.insert(1.0,"This is an Text Box")

e.bind('<Double-Button-1>',Selection)


root.mainloop()
