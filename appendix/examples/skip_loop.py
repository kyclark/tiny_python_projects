#!/usr/bin/env python3

import os
import sys


args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

file = args[0]

if not os.path.isfile(file):
    print('"{}" is not a file'.format(file), file=sys.stderr)
    sys.exit(1)

for i, line in enumerate(open(file)):
    if (i + 1) % 2 == 0:
        continue

    print(i + 1, line, end='')

print('i = ', i)
