#!/usr/bin/env python3
"""Read a file argument"""

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

filename = args[0]

if not os.path.isfile(filename):
    print('"{}" is not a file'.format(filename), file=sys.stderr)
    sys.exit(1)

for line in open(filename):
    print(line, end='')
