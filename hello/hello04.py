#!/usr/bin/env python3
# Author: Ken Youens-Clark

import sys

args = sys.argv[1:]
if args:
    name = args[0]
    print(f'Hello, {name}!')
else:
    print('Hello, World!')
