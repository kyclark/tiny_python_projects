#!/usr/bin/env python3
"""Extract codons from DNA"""

import os
import sys

args = sys.argv[1:]
num_args = len(args)

if not 1 <= num_args <= 2:
    print('Usage: {} DNA'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

string = args[0]
k = 3
n = len(string) - k + 1

for i in range(0, n, k):
    print(string[i:i+k])
