#!/usr/bin/env python3

import os
import sys


args = sys.argv[1:]

if len(args) < 1:
    print('Usage: {} ARG1 [ARG2...]'.format(os.path.basename(sys.argv[0])))
    sys.exit(1)

outfile = 'out.txt'
out_fh = open(outfile, 'wt')

for arg in args:
    out_fh.write(arg + '\n')

out_fh.close()
print('Done, see "{}"'.format(outfile))
