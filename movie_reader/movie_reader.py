#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-16
Purpose: Print text like in the movies
"""

import os
import sys
import time


# --------------------------------------------------
def main():
    """main"""
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]

    if not os.path.isfile(file):
        print('"{}" is not a file.'.format(file))
        sys.exit(1)

    for line in open(file):
        for char in line:
            print(char, end='')
            time.sleep(.5 if char in '.!?' else .2 if char in ',;' else .05)
            sys.stdout.flush()


# --------------------------------------------------
if __name__ == '__main__':
    main()
