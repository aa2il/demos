#! /usr/bin/python3

# Demo of "modern" gui development using custom tk

# pip3 install customtkinter

# See also
#  git clone https://github.com/TomSchimansky/CustomTkinter ctk

import customtkinter

###############################################################################

mode="System"
mode="dark"
#mode="light"
customtkinter.set_appearance_mode(mode)        # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()

