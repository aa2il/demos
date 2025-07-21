#! /usr/bin/python3

# List all the serial ports available.
# This works on both windoz and linux

##############################################################################

import sys
import serial.tools.list_ports as lp
#from serial.tools.list_ports import comports,grep
from pprint import pprint
#if sys.platform == "win32":
#    import win32

##############################################################################

def find_nano_io_device():
    ports = lp.grep(NANO_IO_VIDPID)
    nports=0
    device=None
    for port in ports:
        nports+=1
        pprint(vars(port))
        device=port.device
        print('\nFIND NANO IO DEVICE:',device)

    if nports==0:
        print('FIND NANO IO DEVICE: Unable to locate nano_io')
    elif nports>1:
        print('FIND NANO IO DEVICE: Multiple devices found!')

    return device

print('\nPort finder - lets get started ...\n')

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

NANO_IO_VIDPID='1A86:7523'

# Look at all ports
ports = lp.comports()
print('ports=',ports,'\n')

for port in ports:
    print(port.device)
    print('\tdesc: ',port.description)
    print('\thwid: ',port.hwid)
sys.exit(0)

for port in ports:
    pprint(vars(port))
    if NANO_IO_VIDPID in port.hwid.upper():
        print('************** There it is **********************',port.device)
    #print("port={}: desc={} hwid=[{}]".format(port.device, port.description, port.hwid))

# This should be a direct way to find a specific device    
print('\nSearching for NANO_IO ...')
port=find_nano_io_device()

#for port, desc, hwid in sorted(ports):
#    print("port={}: desc={} hwid=[{}]".format(port, desc, hwid))

# As a test, plug in nano_io and find it
SERIAL_NANO_IO = '/dev/serial/by-id/usb-1a86_USB2.0-Ser_-if00-port0'
print('\nNano_io is supposed to be at port',SERIAL_NANO_IO)
    
print('Done.\n')
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


