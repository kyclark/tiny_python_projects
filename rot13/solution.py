#!/usr/bin/env python3
"""ROT13"""

import argparse
import os
import random
import re
import textwrap
import string
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='ROT13 encryption',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='TEXT',
                        nargs='?',
                        default='-',
                        help='Input text, file, or "-" for STDIN')

    parser.add_argument('-p',
                        '--pad',
                        help='Pad size',
                        metavar='int',
                        type=int,
                        default=4)

    parser.add_argument('-w',
                        '--width',
                        help='Output width',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-s',
                        '--shift',
                        help='Shift arg',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-S',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()
    elif args.text == '-':
        args.text = sys.stdin.read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    text = re.sub('[^A-Z]', '', args.text.upper())
    letters = string.ascii_uppercase
    shift = args.shift or int(len(letters) / 2)
    encrypted = map(lambda char: rot(char, letters, shift), text)
    padded = pad_out(''.join(encrypted), args.pad)
    print('\n'.join(textwrap.wrap(padded, width=args.width)))


# --------------------------------------------------
def rot(char, letters, shift):
    """Shift a character through a list"""

    return letters[(letters.index(char) + shift) %
                   len(letters)] if char in letters else char


# --------------------------------------------------
def pad_out(text, width=4):
    """Pad output into width-columns"""

    while len(text) % width != 0:
        text += random.choice(string.ascii_uppercase)

    spacer = lambda t: ' ' + t[1] if t[0] > 0 and t[0] % width == 0 else t[1]
    return ''.join(map(spacer, enumerate(text)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
