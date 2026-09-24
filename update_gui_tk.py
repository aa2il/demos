#! /usr/bin/python3

# Script showing how to update a tk  from a non-main thread using an event handler
# According to chatgpt, this can also be accomplished using a queue but I like this approach since it is immediate
# Perhaps I need to rethink how bandmap operates?!

# Source - https://stackoverflow.com/a/64289276
# Posted by Mike67, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-21, License - CC BY-SA 4.0

from tkinter import *
import datetime
import threading
import time

root = Tk()
root.title("Thread Test")
print('Main Thread', threading.get_ident())    # main thread id

junk='abc'

def timecnt():  # runs in background thread
    global junk
    print('Timer Thread',threading.get_ident())  # background thread id
    for x in range(10):
        root.event_generate("<<event1>>", when="tail", state=123)   # trigger event in main thread
        txtvar.set(' '*15 + str(x))  # update text entry from background thread
        junk=str(x)
        time.sleep(1)  # one second

def eventhandler(evt):  # runs in main thread
    print('Event Thread',threading.get_ident())   # event thread id (same as main)
    print(evt.state)  # 123, data from event
    #print(dir(evt))
    #print(vars(evt))
    #print(evt.state=='<<event1>>')
    string = datetime.datetime.now().strftime('%I:%M:%S %p')
    lbl.config(text=string)  # update widget

    txt = txtvar.get()
    print('txt=',txt,'\tjunk=',junk)

lbl = Label(root, text='Start')  # label in main thread
lbl.place(x=0, y=0, relwidth=1, relheight=.5)

txtvar = StringVar() # var for text entry
txt = Entry(root, textvariable=txtvar)  # in main thread
txt.place(relx = 0.5, rely = 0.75, relwidth=.5, anchor = CENTER)

thd = threading.Thread(target=timecnt)   # timer thread
thd.daemon = True
thd.start()  # start timer loop

root.bind("<<event1>>", eventhandler)  # event triggered by background thread
root.mainloop()
thd.join()  # not needed
