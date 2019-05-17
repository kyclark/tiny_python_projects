#!/usr/bin/env python3

import os
import sys

albums = {
    "2112": 1976,
    "A Farewell To Kings": 1977,
    "All the World's a Stage": 1976,
    "Caress of Steel": 1975,
    "Exit, Stage Left": 1981,
    "Fly By Night": 1975,
    "Grace Under Pressure": 1984,
    "Hemispheres": 1978,
    "Hold Your Fire": 1987,
    "Moving Pictures": 1981,
    "Permanent Waves": 1980,
    "Power Windows": 1985,
    "Signals": 1982,
}

# Create a list of (value, key) tuples 
# sorted in descending order by the values
pairs = sorted([(x[1], x[0]) for x in albums.items()])

for year, album in pairs:
    print('{} {}'.format(year, album))
