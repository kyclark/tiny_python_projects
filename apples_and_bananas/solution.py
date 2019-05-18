#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-18
Purpose: Apples and bananas
"""

import argparse
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The only vowel allowed',
                        metavar='str',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

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
    vowel = args.vowel

    if os.path.isfile(text):
        text = open(text).read()

    # Method 1: Iterate every character
    new_text = []
    for char in text:
        if char in 'aeiou':
            new_text.append(vowel)
        elif char in 'AEIOU':
            new_text.append(vowel.upper())
        else:
            new_text.append(char)
    text = ''.join(new_text)

    # Method 2: str.replace
    # for v in 'aeiou':
    #     text = text.replace(v, vowel).replace(v.upper(), vowel.upper())

    # Method 3: Regular expressions
    # text = re.sub('[aeiou]', vowel, text)
    # text = re.sub('[AEIOU]', vowel.upper(), text)

    print(text.rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
