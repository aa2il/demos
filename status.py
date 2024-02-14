#!/usr/bin/python3
################################################################################
#
# Status bar demo using tk
#
################################################################################

import tkinter as tk

class StatusBar(tk.Frame):
    def __init__(self, master, fg_color='Black',bg_color=None):
        tk.Frame.__init__(self, master, background = bg_color)
         
        self.label = tk.Label(self, text = "", fg = fg_color, bg = bg_color)
        self.label.pack(side = tk.LEFT)
        self.pack(fill=tk.X, side = tk.BOTTOM)
     
    def setText(self, newText):
        self.label.config(text = newText)
 
    def clearText(self):
        self.label.config(text = "")
     
class Window:   
    def __init__(self, master):
        self.frame = tk.Frame(master)
        b1 = tk.Button(self.frame, text="Button 1", command=self.handleButtonOne)
        b1.pack(padx=30, pady=20)
         
        b2 = tk.Button(self.frame, text="Button 2", command=self.handleButtonTwo)
        b2.pack(padx=30, pady=20)
 
        #self.status_bar = StatusBar(self.frame, 'white',"blue")
        self.status_bar = StatusBar(self.frame)
        self.frame.pack(expand = True, fill = tk.BOTH)
 
    def handleButtonOne(self):
        self.status_bar.setText("Button 1 was Clicked")
 
    def handleButtonTwo(self):
        self.status_bar.setText("Button 2 was Clicked")
 
root = tk.Tk()
window = Window(root)
root.mainloop()
