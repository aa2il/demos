#! /usr/bin/python3

# Script to play with pyhamtools

import sys
from pyhamtools import LookupLib, Callinfo
import redis

###############################################################################

# Need to install redis database to get this all to work - see

# https://realpython.com/python-redis/

# Or just look at the file resdis in this dir.

###############################################################################

"""
# This is very slow since it downloads the database each time - ugh!
print('Lookup instantiaion ...')
my_lookuplib = LookupLib(lookuptype="countryfile")

call="DH1TW"
print('Call info for call',call)
cic = Callinfo(my_lookuplib)

info=cic.get_all(call)
print(info)

"""

"""
# Let's see if this is any better - First, download latest data
print('\nHey 1')
r = redis.Redis()
print('Hey 2')
my_lookuplib = LookupLib(lookuptype="countryfile")
print('Hey 3')
print( my_lookuplib.copy_data_in_redis(redis_prefix="CF", redis_instance=r) )

"""

# Now do something with it - this is looking promising !!!
# BUT it requires user to install redis database so probably not a viable option
print('\nHey 4')
r = redis.Redis()
print('Hey 5')
my_lookuplib = LookupLib(lookuptype="redis", redis_instance=r, redis_prefix="CF")
print('Hey 6')
call="3D2RI"
info=my_lookuplib.lookup_callsign(call)
print('call=',call)
print(info)

# Get home call
call="HC2/DH1TW/P"
cic = Callinfo(my_lookuplib)
homecall=cic.get_homecall(call)
print('\ncall=',call,'\thome call=',homecall)
