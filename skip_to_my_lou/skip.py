#!/usr/bin/env python3
"""Skip code"""

import argparse
import os
import sys
from itertools import chain


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Skip code',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    # parser.add_argument('-a',
    #                     '--arg',
    #                     help='A named string argument',
    #                     metavar='str',
    #                     type=str,
    #                     default='')

    # parser.add_argument('-i',
    #                     '--int',
    #                     help='A named integer argument',
    #                     metavar='int',
    #                     type=int,
    #                     default=0)

    # parser.add_argument('-f',
    #                     '--file',
    #                     help='A readable file',
    #                     metavar='FILE',
    #                     type=argparse.FileType('r'),
    #                     default=None)

    # parser.add_argument('-o',
    #                     '--on',
    #                     help='A boolean flag',
    #                     action='store_true')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(' '.join(map(skip, args.text.split())))


# --------------------------------------------------
def divide(word):
    """Divide a word in half"""

    l = len(word)
    mid = 1 if l == 1 else round(l / 2)
    return (word[:mid], word[mid:])


# --------------------------------------------------
def test_divide():
    """Test divide"""

    assert divide('a') == ('a', '')
    assert divide('an') == ('a', 'n')
    assert divide('foo') == ('fo', 'o')
    assert divide('foobar') == ('foo', 'bar')


# --------------------------------------------------
def swap(s):
    """Swap letters"""

    r1 = range(0, len(s), 2)
    r2 = range(1, len(s), 2)
    f = lambda i: s[i]
    return ''.join(chain(map(f, r1), map(f, r2)))


# --------------------------------------------------
def test_swap():
    """Test swap"""

    assert swap('abc') == 'acb'
    assert swap('abcd') == 'acbd'


# --------------------------------------------------
def skip(word):
    """Skip-code a word"""

    return ''.join(map(swap, divide(word)))


# --------------------------------------------------
def test_skip():
    """Test skip"""

    assert skip('a') == 'a'
    assert skip('an') == 'an'
    assert skip('the') == 'the'
    assert skip('then') == 'then'
    assert skip('foobar') == 'foobra'


# --------------------------------------------------
if __name__ == '__main__':
    main()
