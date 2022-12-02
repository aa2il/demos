#! /usr/bin/python3

# Example showing how to easily transition from tk to custom tk.
# Derived from examples in ../ctk/examples

###############################################################################

import sys
import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk

###############################################################################

USE_CTK=True
USE_CTK=False

###############################################################################

# Callback
def button_callback():
    print("button pressed")

def slider_callback(value):
    progressbar_1["value"] = value

# Apply generic names to gui widgets from selected tool set
if USE_CTK:
    Title='Example Using ctk'
    ctk.set_appearance_mode("dark")      # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
    Tk=ctk.CTk
    Frame = ctk.CTkFrame
    Label = ctk.CTkLabel
    ProgressBar = ctk.CTkProgressBar
    Button = ctk.CTkButton
    Slider = ctk.CTkSlider
    Entry = ctk.CTkEntry
    CheckBox = ctk.CTkCheckBox
    RadioButton = ctk.CTkRadioButton
else:
    Title='Example Using tk'
    Tk=tk.Tk
    Frame = tk.Frame
    Label = tk.Label
    ProgressBar = ttk.Progressbar
    Button = tk.Button
    Slider = tk.Scale
    Entry = tk.Entry
    CheckBox = tk.Checkbutton
    RadioButton = ttk.Radiobutton

# Root window    
app = Tk()
app.geometry("400x350")
app.title(Title)

# Not sure what this does?
s = ttk.Style()
s.configure("TRadiobutton", fg="red")

y_padding = 6
radiobutton_var = tk.IntVar(value=1)

# Widgets
frame_1 = Frame(master=app)  # , width=300, height=260, bg="lightgray")
label_1 = Label(master=frame_1, text='Label 1',justify=tk.LEFT)
progressbar_1 = ProgressBar(master=frame_1)  # , style='black.Horizontal.TProgressbar', length=150)
button_1 = Button(master=frame_1, command=button_callback,text="Button 1")   #, highlightbackground="lightgray")
slider_1 = Slider(master=frame_1, command=slider_callback, orient="horizontal",from_=0, to=1)  #, bg="lightgray", length=150)
entry_1 = Entry(master=frame_1,text="Entry Box")   # , highlightbackground="lightgray", width=10)
checkbox_1 = CheckBox(master=frame_1,text='CheckBox') # , bg=frame_1.cget("bg"), text="CheckButton")
radiobutton_1 = RadioButton(master=frame_1, variable=radiobutton_var, value=1, text="Radiobutton 1")
radiobutton_2 = RadioButton(master=frame_1, variable=radiobutton_var, value=2, text="Radiobutton 2")

# Layout
frame_1.pack(padx=60, pady=20, fill="both", expand=True)
label_1.pack(pady=y_padding, padx=10)
progressbar_1.pack(pady=y_padding, padx=10)
button_1.pack(pady=y_padding, padx=10)
slider_1.pack(pady=y_padding, padx=10)
entry_1.pack(pady=y_padding, padx=10)
checkbox_1.pack(pady=y_padding, padx=10)
radiobutton_1.pack(pady=y_padding, padx=10)
radiobutton_2.pack(pady=y_padding, padx=10)

# Set widgets
progressbar_1["value"] = 50
slider_1.set(0.5)

app.mainloop()
sys.exit(0)

###############################################################################

# This was the tk example

import tkinter.ttk as ttk
import tkinter

app = tkinter.Tk()
app.geometry("400x350")
app.title("simple_example_standard_tkinter.py")


def button_function():
    print("button pressed")


def slider_function(value):
    progressbar_1["value"] = value


s = ttk.Style()
s.configure("TRadiobutton", fg="red")

y_padding = 6

frame_1 = tkinter.Frame(master=app, width=300, height=260, bg="lightgray")
frame_1.pack(padx=60, pady=20, fill="both", expand=True)

label_1 = tkinter.Label(master=frame_1, text="Label", bg="lightgray")
label_1.pack(pady=y_padding, padx=10)

progressbar_1 = ttk.Progressbar(master=frame_1, style='black.Horizontal.TProgressbar', length=150)
progressbar_1.pack(pady=y_padding, padx=10)
progressbar_1["value"] = 50

button_1 = tkinter.Button(master=frame_1, command=button_function, text="Button", highlightbackground="lightgray")
button_1.pack(pady=y_padding, padx=10)

slider_1 = tkinter.Scale(master=frame_1, command=slider_function, orient="horizontal", bg="lightgray", length=150)
slider_1.pack(pady=y_padding, padx=10)

entry_1 = tkinter.Entry(master=frame_1, highlightbackground="lightgray", width=10)
entry_1.pack(pady=y_padding, padx=10)

checkbox_1 = tkinter.Checkbutton(master=frame_1, bg=frame_1.cget("bg"), text="CheckButton")
checkbox_1.pack(pady=y_padding, padx=10)

radiobutton_var = tkinter.IntVar()

radiobutton_1 = ttk.Radiobutton(master=frame_1, variable=radiobutton_var, value=1, text="Radiobutton")
radiobutton_1.pack(pady=y_padding, padx=10)

radiobutton_2 = ttk.Radiobutton(master=frame_1, variable=radiobutton_var, value=2, text="Radiobutton")
radiobutton_2.pack(pady=y_padding, padx=10)

app.mainloop()

###############################################################################

# This was the ctk example
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x580")
app.title("CustomTkinter simple_example.py")


def button_callback():
    print("Button click", combobox_1.get())


def slider_callback(value):
    progressbar_1.set(value)


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)

progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
button_1.pack(pady=12, padx=10)

slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
slider_1.pack(pady=12, padx=10)
slider_1.set(0.5)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
entry_1.pack(pady=12, padx=10)

### Does this have a tk counterpart???
optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
optionmenu_1.pack(pady=12, padx=10)
optionmenu_1.set("CTkOptionMenu")

combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
combobox_1.pack(pady=12, padx=10)
optionmenu_1.set("CTkComboBox")

checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
checkbox_1.pack(pady=12, padx=10)

radiobutton_var = tkinter.IntVar(value=1)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
radiobutton_1.pack(pady=12, padx=10)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
radiobutton_2.pack(pady=12, padx=10)

### Does this have a tk counterpart???
switch_1 = customtkinter.CTkSwitch(master=frame_1)
switch_1.pack(pady=12, padx=10)

app.mainloop()
