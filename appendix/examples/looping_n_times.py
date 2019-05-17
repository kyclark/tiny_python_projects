#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-17
Purpose: Looping N times
"""

import os
import sys


# --------------------------------------------------
def main():
    """main"""
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    arg = args[0]

    if arg.isdigit():
        for i in range(1, int(arg) + 1):
            print('{} time{}'.format(i, '' if i == 1 else 's'))
    else:
        print('"{}" is not a number'.format(arg))



# --------------------------------------------------
if __name__ == '__main__':
    main()
