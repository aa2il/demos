#! /usr/bin/python3

import sys
import os

# A very simple Hello World

print("\n\tHello World! - Plain text, no gui\n")

# Let's see how the various system path discovery mechanisms work
PYTHON_EXE=os.path.dirname(sys.executable)
print('Path to PYTHON EXECUTABLE   =\t',PYTHON_EXE)

HOME = os.path.expanduser('~/')
print('Path to HOME         =\t',HOME)
print('Path to FILE         =\t',__file__)

EXE_PATH=os.path.realpath(sys.executable)
print('Path to EXECUTABLE   =\t',EXE_PATH)

CWD=os.getcwd()
print('Current Working Dir  =\t',CWD)

os.chdir('..')
CWD2=os.getcwd()
print('Current Working Dir2 =\t',CWD2)

