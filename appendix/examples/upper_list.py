#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) < 1:
    print('Usage: {} ARG [ARG...]'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

print('List comprehension')
print(', '.join([x.upper() for x in args]))

print('Map')
print(', '.join(map(str.upper, args)))
