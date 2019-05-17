#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-06
Purpose: Jump the Five
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} NUMBER'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    num = args[0]
    jumper = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5'
    }

    for char in num:
        print(jumper[char] if char in jumper else char, end='')
    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
