#!/usr/bin/env python3
"""Show contents of directory argument"""

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} DIR'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

dirname = args[0]

if not os.path.isdir(dirname):
    print('"{}" is not a directory'.format(dirname), file=sys.stderr)
    sys.exit(1)

for entry in os.listdir(dirname):
    print(entry)
