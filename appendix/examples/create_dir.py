#!/usr/bin/env python3
"""Test for a directory and create if needed"""

import os
import sys

args = sys.argv[1:]

if len(args) != 1:
    print('Usage: {} DIR'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

dirname = args[0]

if os.path.isdir(dirname):
    print('"{}" exists'.format(dirname))
else:
    print('Creating "{}"'.format(dirname))
    os.makedirs(dirname)
