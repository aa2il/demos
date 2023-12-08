#!/usr/bin/python3
################################################################################
#
# Play with PING
#
# pip3 install ping3
#
################################################################################

"""
# This works
import os
hostname = "google.com"    # example
hostname = "8.8.8.8"       # Screwggle DNS
response = os.system("ping -c 1 " + hostname)

# and then check the response...
if response == 0:
  print(f"{hostname} is up!")
else:
  print(f"{hostname} is down!")
"""

"""
# This is a better version of above that works on linux & windoz
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):

    # Returns True if host (str) responds to a ping request.
    # Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

hostname = "8.8.8.8"       # Screwggle DNS
response = ping( hostname)
print(response)

# and then check the response...
if response:
  print(f"{hostname} is up!")
else:
  print(f"{hostname} is down!")
"""

# The jury is out on this one but seems ok?
from ping3 import ping, verbose_ping
hostname = "8.8.8.8"       # Screwggle DNS
response=ping(hostname)  # Returns delay in seconds.
print(response)
    
