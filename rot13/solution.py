#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-09
Purpose: Rot13 (rotate 13) encryption
"""

import argparse
import os
import re
import string
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'text', metavar='str', help='Input text, file, or "-" for STDIN')

    parser.add_argument(
        '-s',
        '--shift',
        help='Shift arg',
        metavar='int',
        type=int,
        default=0)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    text = args.text

    if text == '-':
        text = sys.stdin.read()
    elif os.path.isfile(text):
        text = open(text).read()

    lcase = list(string.ascii_lowercase)
    ucase = list(string.ascii_uppercase)
    num_lcase = len(lcase)
    num_ucase = len(ucase)
    lcase_shift = args.shift or int(num_lcase / 2)
    ucase_shift = args.shift or int(num_ucase / 2)

    def rot13(char):
        if char in lcase:
            pos = lcase.index(char)
            rot = (pos + lcase_shift) % num_lcase
            return lcase[rot]
        elif char in ucase:
            pos = ucase.index(char)
            rot = (pos + ucase_shift) % num_ucase
            return ucase[rot]
        else:
            return char

    print(''.join(map(rot13, text)).rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
