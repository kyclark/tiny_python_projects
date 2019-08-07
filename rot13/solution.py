#!/usr/bin/env python3
"""ROT13"""

import argparse
import random
import re
import string


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='ROT13 encryption',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        type=argparse.FileType('r'),
                        help='Input text, file, or "-" for STDIN')

    parser.add_argument('-p',
                        '--pad',
                        help='Pad size',
                        metavar='int',
                        type=int,
                        default=4)

    parser.add_argument('-s',
                        '--shift',
                        help='Shift arg',
                        metavar='int',
                        type=int,
                        default=0)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = re.sub('[^A-Z]', '', args.text.read().upper())
    letters = list(string.ascii_uppercase)
    shift = args.shift or int(len(letters) / 2)
    chars = map(lambda char: rot(char, letters, shift), text)
    print(pad_out(''.join(chars), args.pad))


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
        text += random.choice(text)

    return ''.join(
        map(lambda t: ' ' + t[1] if t[0] > 0 and t[0] % width == 0 else t[1],
            enumerate(text)))


# --------------------------------------------------
def test_pad_out():
    """Test pad_out"""

    random.seed(1)
    assert pad_out('ab cdef g', 2) == 'ab cd ef gb'
    assert pad_out('ab cdef g', 3) == 'abc def geb'
    assert pad_out('ab cdef g', 4) == 'abcd efgc'
    assert pad_out('ab cdef g', 5) == 'abcde fgaaa'
    assert pad_out('ab cdef g', 6) == 'abcdef gdgdbd'
    random.seed(None)


# --------------------------------------------------
if __name__ == '__main__':
    main()
