#! /usr/bin/python3

# Script to explore fonts available

from tkinter import Tk, font
root = Tk()
print('families=',font.families())
#print('names=',font.names())

font1 = font.Font(family="monospace",size=12,weight="bold")
print('font1=',font1.actual())

#conda install -c conda-forge mscorefonts
