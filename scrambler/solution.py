#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-25
Purpose: Scramble the letters of words, leaving first and last in place
"""

import argparse
import os
import re
import random
import sys
from itertools import chain


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='STR', help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def scramble(word):
    """For words over 3 characters, shuffle the letters in the middle"""

    if len(word) > 3:
        orig = list(word[1:-1])
        middle = orig.copy()
        while middle == orig:
            random.shuffle(middle)
        word = word[0] + ''.join(middle) + word[-1]

    return word

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    random.seed(args.seed)

    if os.path.isfile(text):
        text = open(text).read()

    for line in text.splitlines():
        print(''.join(map(scramble, re.split(r'(\W+)', line))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
