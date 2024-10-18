#! /usr/bin/python3

# A very simple Hello World using Tk.  Also used to figure out selection

import sys
if sys.version_info[0]==3:
    from tkinter import *
else:
    from Tkinter import *
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

root = Tk()
msg="Hello World! - Tk Version"
print(msg)

w = Label(root, text=msg)
w.pack()

e = Entry(root,fg='blue',selectbackground='white')
e.pack()
e.insert(0,"This is an Entry Box")

#t = Text(root,exportselection=True)
#t.pack()
#t.insert(1.0,"This is an Text Box")

e.bind('<Double-Button-1>',Selection)


root.mainloop()
