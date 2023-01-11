#! /usr/bin/python3

# pip3 install pyautogui
# sudo apt-get install scrot

import sys
import pyautogui

print("Hey!")
sz=pyautogui.size()
print('sz=',sz)

# Print out mouse coords until ^C
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

# Take a screen shot
print('Taking screen snapshot ...')
screenshot = pyautogui.screenshot()
screenshot.save("screen.png")
print('Done.')

