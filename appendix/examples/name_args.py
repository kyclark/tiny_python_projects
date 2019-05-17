#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]

if len(args) != 2:
    print('Usage: {} FILE NUM'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

file, num = args

file = args[0]
num = args[1]

print('FILE is "{}", NUM is "{}"'.format(file, num))
