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
                        metavar='str',
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
    text = re.sub('[^A-Z]', '', args.text.upper())
    letters = list(string.ascii_uppercase)
    shift = args.shift or int(len(letters) / 2)
    chars = map(lambda char: rot(char, letters, shift), text)
    print('\n'.join(
        textwrap.wrap(pad_out(''.join(chars), args.pad), width=args.width)))


# --------------------------------------------------
def rot(char, letters, shift):
    """Shift a character through a list"""

    return letters[(letters.index(char) + shift) %
                   len(letters)] if char in letters else char


# --------------------------------------------------
def test_rot():
    """Test rot"""

    assert rot('a', 'abcd', 1) == 'b'
    assert rot('b', 'abcd', 3) == 'a'
    assert rot('c', 'abcd', 5) == 'd'
    assert rot('x', 'abcd', 1) == 'x'


# --------------------------------------------------
def pad_out(text, width=4):
    """Pad output into width-columns"""

    text = re.sub(r'\s+', '', text)
    while len(text) % width != 0:
        text += random.choice(string.ascii_uppercase)

    return ''.join(
        map(lambda t: ' ' + t[1] if t[0] > 0 and t[0] % width == 0 else t[1],
            enumerate(text)))


# --------------------------------------------------
def test_pad_out():
    """Test pad_out"""

    random.seed(1)
    assert pad_out('AB CDEF G', 2) == 'AB CD EF GE'
    assert pad_out('AB CDEF G', 3) == 'ABC DEF GSZ'
    assert pad_out('AB CDEF G', 4) == 'ABCD EFGY'
    assert pad_out('AB CDEF G', 5) == 'ABCDE FGCID'
    assert pad_out('AB CDEF G', 6) == 'ABCDEF GPYOPU'
    random.seed(None)


# --------------------------------------------------
if __name__ == '__main__':
    main()
