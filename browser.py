#! /usr/bin/python3

# There are some issues with this on RPi
# Figure it out ...

#import sys
import webbrowser
import platform

# Sys inbfo
platform.system()
print('arch=',platform.architecture())
print('mach=',platform.machine())
print('ver =',platform.version())

# See what we have - None gives us the default
browser=None
for b in [None,'chrome','chromium','firefox']:
    try:
        bc = webbrowser.get(b)
        print(bc)
        print(bc.name)

        if browser==None and bc.name!='www-browser':
            browser=bc

        if b=='chromium':
            chromium=browser
    except:
        print('Unable to find',b)

# Open a URL in chromium
url='https://qrz.com/db/AA2IL'
#chromium.open(url)

if platform.machine()=='aarch64':
    browser=webbrowser.get('chromium')
else:
    browser=webbrowser.get()
print(browser)
browser.open(url)




