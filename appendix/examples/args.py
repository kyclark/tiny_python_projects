#!/usr/bin/env python3

import os
import sys

args = sys.argv[1:]
num = len(args)

print('There are {} arg{}'.format(num, '' if num == 1 else 's'))
