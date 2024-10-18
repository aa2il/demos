#! /usr/bin/python3
##############################################################################
#
# Script to explore fonts available
#
# By default, conda does not include very many fonts for tk and therefore the
# tk guis look ugly.  Do this when creating the sandbox to avoid this:
#
# conda create -y --prefix "conda_env" -c conda-forge "python==3.12.*" "tk[build=xft_*]"
#
# This can be used to fix an existing sandbox:
#
# conda install --prefix "conda_env" -c conda-forge tk=*=xft_* 
#
# In my case, conda_env is ~/miniconda3/envs/aa2il_12 or whatever
#
##############################################################################

from tkinter import *
from tkinter import font
import sys

root = Tk()
root.title('Font Families')
fonts=list(font.families())
fonts.sort()

print('\nAvailable fonts:',fonts)
print('\nDefault font:',font.nametofont('TkTextFont').actual())
sys.exit(0)

size=24

def populate(frame):
    '''Put in the fonts'''
    listnumber = 1
    for i, item in enumerate(fonts):
        print('Loading item',i,'of',len(fonts),':',item,'...')
        label = "listlabel" + str(listnumber)
        label = Label(frame,text=item,font=(item, size))
        label.grid(row=i)
        label.bind("<Button-1>",lambda e,item=item:copy_to_clipboard(item))
        listnumber += 1

def copy_to_clipboard(item):
    root.clipboard_clear()
    root.clipboard_append("font=('" + item.lstrip('@') + "', 12)")

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas = Canvas(root, borderwidth=0, background="#ffffff")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")

frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

populate(frame)

root.mainloop()


sys.exit(0)



from tkinter import Tk, font
root = Tk()
print('families=',font.families())
#print('names=',font.names())

font1 = font.Font(family="monospace",size=12,weight="bold")
print('font1=',font1.actual())

#conda install -c conda-forge mscorefonts
