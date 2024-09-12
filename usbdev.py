#! /usr/bin/python3

# Examine usb devices
# pip install pyusb

##############################################################################

"""
import usb
busses = usb.busses()
for bus in busses:
    devices = bus.devices
    for dev in devices:
        print("\nDevice:", dev.filename)
        print("  idVendor: %d (0x%04x)" % (dev.idVendor, dev.idVendor))
        print("  idProduct: %d (0x%04x)" % (dev.idProduct, dev.idProduct))
        #print("  bus: %d \taddr: %d" % (dev.devnum, dev.devnum))
        print(dev.iManufacturer)
        print(dev.iProduct)
        #print(dev)
"""


import pyudev

context = pyudev.Context()
devices = context.list_devices(subsystem='usb')

for device in devices:
    print('\n',device)
    #print(device.get('ID_MODEL') )
    
    if device.get('ID_MODEL'):
        print(f'Device Name: {device.get("ID_VENDOR")} {device.get("ID_MODEL")}')
        print(f'Device Serial Number: {device.get("ID_SERIAL_SHORT")}')
        print(f'Device Bus: {device.get("ID_BUS")}')
        print(f'Device Device: {device.get("ID_PATH")}')

