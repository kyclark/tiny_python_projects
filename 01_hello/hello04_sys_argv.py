#!/usr/bin/env python3
# Purpose: Say hello

import sys

args = sys.argv[1:]          # argv is a list, slice from index 1
if args:                     # if there are any arguments
    name = args[0]           # get the "name" from index 0
    print(f'Hello, {name}!') # print "name" using an f-string
else:                        # otherwise
    print('Hello, World!')   # print the default greeting
