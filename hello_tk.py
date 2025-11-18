#!/usr/bin/env -S uv run --script

#OLD: ! /usr/bin/python3

# A very simple Hello World using Tk.  Also used to figure out selection

import sys
if sys.version_info[0]==3:
    from tkinter import *
    import tkinter.font
else:
    from Tkinter import *
    import tkFont
import time

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
    
root = Tk()
msg="Hello World! - Tk Version"
print(msg)

FAMILY="monospace"
SIZE=28
fnt =  tkinter.font.Font(family=FAMILY,size=SIZE, weight="bold")

w = Label(root, text=msg, font=fnt)
w.pack()

e = Entry(root,fg='blue',selectbackground='white', font=fnt)
e.pack()
e.insert(0,"This is an Entry Box")

#t = Text(root,exportselection=True)
#t.pack()
#t.insert(1.0,"This is an Text Box")

e.bind('<Double-Button-1>',Selection)


root.mainloop()
