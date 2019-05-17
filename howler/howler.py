#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-16
Purpose: Uppercase text
"""

import os
import sys


# --------------------------------------------------
def main():
    """main"""
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} INPUT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    text = args[0]
    if os.path.isfile(text):
        text = open(text).read()

    print(text.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
