#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]
num_args = len(args)

if not 1 <= num_args <= 2:
    print('Usage: {} FILE [NUM]'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

file = args[0]
num = args[1] if num_args == 2 else 10

print('FILE is "{}", NUM is "{}"'.format(file, num))
