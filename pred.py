#! /usr/bin/python3

# Script to play with pypredict - from pypredict project website

# sudo apt-get install python-dev
# sudo python setup.py install

import predict

# Observe a satellite (relative to a position on earth)
tle = """0 LEMUR 1
1 40044U 14033AL  15013.74135905  .00002013  00000-0  31503-3 0  6119
2 40044 097.9584 269.2923 0059425 258.2447 101.2095 14.72707190 30443"""
qth = (37.771034, 122.413815, 7)  # lat (N), long (W), alt (meters)
obs=predict.observe(tle, qth) # optional time argument defaults to time.time()
print('\nobs=',obs)

# Show upcoming transits of satellite over groundstation
p = predict.transits(tle, qth)
print('\np=',p)
for i in range(10):
    #transit = p.next()              # This is wrong on the web-site!
    transit = next(p)
    print("%f\t%f\t%f" % (transit.start, transit.duration(), transit.peak()['elevation']))
        
