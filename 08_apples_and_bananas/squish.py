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
    text = args.text
    vowel = args.vowel
    text = re.sub('[aeiou]', vowel, text)
    text = re.sub('[AEIOU]', vowel.upper(), text)
    pattern = vowel + '+'
    result = vowel
    text = re.sub(pattern, result, text)
    pattern = vowel.upper() + '+'
    result = vowel.upper()
    text = re.sub(pattern, result, text)
    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
