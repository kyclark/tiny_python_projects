#!/usr/bin/env python3
"""ROT13"""

import argparse
import os
import random
import re
import string
import sys
from textwrap import wrap
from typing import Any, List, Union


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
    encrypted = [rot(char, letters, shift) for char in text]
    padded = pad_out(encrypted, args.pad)
    print('\n'.join(wrap(padded, width=args.width)))


# --------------------------------------------------
def rot(char: str, letters: List[str], shift: int) -> str:
    """Shift a character through a list"""

    return letters[(letters.index(char) + shift) %
                   len(letters)] if char in letters else char


# --------------------------------------------------
def nth(n: int, a: List[Any]) -> List[int]:
    """Return the indexes of every `n`-th element of a given list `a`"""

    return list(filter(lambda i: i > 0, range(-1, len(a), n)))


# --------------------------------------------------
def pad_out(text: Union[str, List[str]], pad: int = 4) -> str:
    """Pad output into width-columns"""

    text = list(text)
    while len(text) % pad != 0:
        text.append(random.choice(string.ascii_uppercase))

    for i in nth(pad, text):
        text[i] += ' '

    return ''.join(text).rstrip()


# --------------------------------------------------
if __name__ == '__main__':
    main()
