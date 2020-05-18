#!/usr/bin/env python3
"""Apples and Bananas"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(''.join([new_char(c, args.vowel) for c in args.text]))


# --------------------------------------------------
def new_char(char, vowel):
    """Return the given vowel if a char is a vowel else the char"""

    return vowel if char in 'aeiou' else \
        vowel.upper() if char in 'AEIOU' else char


# --------------------------------------------------
if __name__ == '__main__':
    main()
