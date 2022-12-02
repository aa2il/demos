#! /usr/bin/python3

# A very simple Hello World using Custom Tk showing how to convert Tk version (hello1.py)

import sys
import customtkinter

###############################################################################

mode="dark"
customtkinter.set_appearance_mode(mode)        # Modes: system (default), light, dark

#root = Tk()
root = customtkinter.CTk()
msg="Hello World! - Custom Tk Version"
print(msg)

#w = Label(root, text=msg)
w = customtkinter.CTkLabel(master=root, text=msg)
#w = customtkinter.CTkLabel(master=root,
#                           text=msg,
#                           text_font=("Roboto Medium", -16))  # font name and size in px
w.pack()

root.mainloop()
