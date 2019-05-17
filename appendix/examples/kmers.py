#!/usr/bin/env python3
"""Extract k-mers from string"""

import os
import sys

args = sys.argv[1:]
num_args = len(args)

if not 1 <= num_args <= 2:
    print('Usage: {} STR [K]'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

string = args[0]
k = args[1] if num_args == 2 else '3'

# Guard against a string like "foo"
if not k.isdigit():
    print('k "{}" is not a digit'.format(k))
    sys.exit(1)

# Safe to convert now
k = int(k)

if len(string) < k:
    print('There are no {}-length substrings in "{}"'.format(k, string))
else:
    n = len(string) - k + 1
    for i in range(0, n):
        print(string[i:i+k])
