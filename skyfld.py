#!/usr/bin/env -S uv run --script

# Script to play with skyfiled orbit predictor
# It looks like this is supposed to be the successor to ephem

# Seems pretty straight-forward - Not sure if/when we'lll need to transition ...

from skyfield.api import load

# Load the satellite TLE data
satellite_url = 'https://celestrak.org/NORAD/elements/stations.txt'
satellites = load.tle_file(satellite_url)
print(satellites)

# Select a specific satellite, e.g., the International Space Station (ISS)
satellite = satellites[0]  # Adjust index as needed
print(' ')
print(satellites[0])
print(' ')

# Create a timescale and get the current time
ts = load.timescale()
t = ts.now()

# Compute the satellite's position
astrometric = satellite.at(t)
position = astrometric.position.km  # Position in kilometers

print(f'Satellite Position (km): {position}')
