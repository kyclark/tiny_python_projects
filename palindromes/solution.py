#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-29
Purpose: Find palindromes in text
"""

import argparse
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find palindromes in text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    parser.add_argument('-m',
                        '--min',
                        metavar='int',
                        type=int,
                        help='Minimum word length',
                        default=3)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    min_length = args.min

    if os.path.isfile(text):
        text = open(text).read()

    for line in text.splitlines():
        for word in re.split('(\W+)', line.lower()):
            if len(word) >= min_length:
                rev = ''.join(reversed(word))
                if rev == word:
                    print(word)


# --------------------------------------------------
if __name__ == '__main__':
    main()
