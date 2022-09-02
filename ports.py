#! /usr/bin/python3

# List all the serial ports available

import sys
if sys.platform == "win32":
    import win32
    
print('Howdy 0')

"""
if sys.platform == "linux" or sys.platform == "linux2":
    # linux
    pass
elif sys.platform == "darwin":
    # OS X
    pass
elif sys.platform == "win32":
    # Windows...
"""    

# This does not load on bottles/win
#import serial.tools.list_ports as lp
from serial.tools.list_ports import comports

print('Howdy 1')
ports = comports()

print('Howdy 2')
for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc, hwid))

sys.exit(0)






import usb.core
dev = usb.core.find()

print(dev)

# find nanoIO
dev = usb.core.find(idVendor=0x1a86, idProduct=0x7523)

print('\n',dev)

sys.exit(0)


import usb
busses = usb.busses()
for bus in busses:
    for dev in bus.devices:
        try:
            print ("iManufacturer   : %s" %usb.util.get_string(dev.dev, 256, 1))
            print ("iProduct            : %s" %usb.util.get_string(dev.dev, 256, 2))
            print ("iSerialNumber   : %s" %usb.util.get_string(dev.dev, 256, 3))
        except:
            pass

#print ("Test vehicle %s device NOT FOUND!" %protocol)

sys.exit(0)


import win32com.client

wmi = win32com.client.GetObject ("winmgmts:")
for usb in wmi.InstancesOf ("Win32_USBHub"):
    print(usb.DeviceID)

sys.exit(0)


# Works only on Windows:

import winreg
import itertools

def get_serial_ports() -> list:
    path = 'HARDWARE\\DEVICEMAP\\SERIALCOMM'
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)

    ports = []
    for i in itertools.count():
        try:
            ports.append(winreg.EnumValue(key, i)[1])
        except EnvironmentError:
            break

    return ports

#if __name__ == "__main__":
#    ports = serial_ports()

ports=get_serial_ports()
print(ports)


sys.exit(0)


import glob
import serial

def get_serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            print(s.name)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

ports=get_serial_ports()
print(ports)

sys.exit(0)


