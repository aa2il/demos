#! /usr/bin/python3

# Simple spreadsheet-like display/editor

# pip3 install tksheet

import sys
from tkinter import *


class demo0():
    def __init__(self):
        self.root = Tk()

        height = 5
        width = 5
        self.sheet=[]
        
        for i in range(height): #Rows
            row=[]
            for j in range(width): #Columns
                #b = Entry(root)
                b = Entry(self.root,validate='all',
                          validatecommand=(self.root.register(self.Changed), '%W','%P'),
                          name='!Cell'+str(i)+'_'+str(j))
                b.grid(row=i,column=j)
                b.insert(0,"Row "+str(i)+" Col "+str(j))
                row.append(b)
            self.sheet.append(row)

        val = self.sheet[3][4].get()
        print(val)

    def Changed(self,widget,txt):
        idx=list(map(int, widget.replace('.!Cell','').split('_') ))
        print(widget,'\t',idx,'\t',txt)
        return True
    

demo0()
mainloop()
sys,exit(0)





import tkinter as tk
#from tksheet import Sheet
from tksheet import Sheet, num2alpha

class demo1(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)
        self.sheet = Sheet(self.frame,
                           theme='light green',
                           data = [[f"Row {r}, Column {c}" for c in range(50)] for r in range(500)])
        self.sheet.enable_bindings()
        self.frame.grid(row = 0, column = 0, sticky = "nswe")
        self.sheet.grid(row = 0, column = 0, sticky = "nswe")
        self.sheet.change_theme("light green", True) 

class demo2(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

        # create an instance of Sheet()
        self.sheet = Sheet(
            # set the Sheets parent widget
            self.frame,
            # optional: set the Sheets data at initialization
            data=[[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(20)] for r in range(100)],
            theme="light green",
            height=520,
            width=1000,
        )
        # enable various bindings
        self.sheet.enable_bindings("all", "edit_index", "edit_header")

        # set a user edit validation function
        # AND bind all sheet modification events to a function
        # chained as two functions
        # more information at:
        # https://github.com/ragardner/tksheet/wiki/Version-7#validate-user-cell-edits
        self.sheet.edit_validation(self.validate_edits).bind("<<SheetModified>>", self.sheet_modified)

        # add some new commands to the in-built right click menu
        # setting data
        self.sheet.popup_menu_add_command(
            "Say Hello",
            self.say_hello,
            index_menu=False,
            header_menu=False,
            empty_space_menu=False,
        )
        # getting data
        self.sheet.popup_menu_add_command(
            "Print some data",
            self.print_data,
            empty_space_menu=False,
        )
        # overwrite Sheet data
        self.sheet.popup_menu_add_command("Reset Sheet data", self.reset)
        # set the header
        self.sheet.popup_menu_add_command(
            "Set header data",
            self.set_header,
            table_menu=False,
            index_menu=False,
            empty_space_menu=False,
        )
        # set the index
        self.sheet.popup_menu_add_command(
            "Set index data",
            self.set_index,
            table_menu=False,
            header_menu=False,
            empty_space_menu=False,
        )

        self.frame.grid(row=0, column=0, sticky="nswe")
        self.sheet.grid(row=0, column=0, sticky="nswe")

    def validate_edits(self, event):
        # print (event)
        if event.eventname.endswith("header"):
            return event.value + " edited header"
        elif event.eventname.endswith("index"):
            return event.value + " edited index"
        else:
            if not event.value:
                return "EMPTY"
            return event.value[:3]

    def say_hello(self):
        current_selection = self.sheet.get_currently_selected()
        if current_selection:
            box = (current_selection.row, current_selection.column)
            # set cell data, end user Undo enabled
            # more information at:
            # https://github.com/ragardner/tksheet/wiki/Version-7#setting-sheet-data
            self.sheet[box].options(undo=True).data = "Hello World!"
            # highlight the cell for 2 seconds
            self.highlight_area(box)

    def print_data(self):
        for box in self.sheet.get_all_selection_boxes():
            # get user selected area sheet data
            # more information at:
            # https://github.com/ragardner/tksheet/wiki/Version-7#getting-sheet-data
            data = self.sheet[box].data
            for row in data:
                print(row)

    def reset(self):
        # overwrites sheet data, more information at:
        # https://github.com/ragardner/tksheet/wiki/Version-7#setting-sheet-data
        self.sheet.set_sheet_data([[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(20)] for r in range(100)])
        # reset header and index
        self.sheet.headers([])
        self.sheet.index([])

    def set_header(self):
        self.sheet.headers(
            [f"Header {(letter := num2alpha(i))} - {i + 1}\nHeader {letter} 2nd line!" for i in range(20)]
        )

    def set_index(self):
        self.sheet.set_index_width()
        self.sheet.row_index(
            [f"Index {(letter := num2alpha(i))} - {i + 1}\nIndex {letter} 2nd line!" for i in range(100)]
        )

    def sheet_modified(self, event):
        # uncomment below if you want to take a look at the event object
        # print ("The sheet was modified! Event object:")
        # for k, v in event.items():
        #     print (k, ":", v)
        # print ("\n")

        # otherwise more information at:
        # https://github.com/ragardner/tksheet/wiki/Version-7#event-data

        # highlight the modified cells briefly
        if event.eventname.startswith("move"):
            for box in self.sheet.get_all_selection_boxes():
                self.highlight_area(box)
        else:
            for box in event.selection_boxes:
                self.highlight_area(box)

    def highlight_area(self, box, time=800):
        # highlighting an area of the sheet
        # more information at:
        # https://github.com/ragardner/tksheet/wiki/Version-7#highlighting-cells
        self.sheet[box].bg = "indianred1"
        self.after(time, lambda: self.clear_highlight(box))

    def clear_highlight(self, box):
        self.sheet[box].dehighlight()


app = demo1()
#app = demo2()
app.mainloop()
