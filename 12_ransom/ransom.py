#!/usr/bin/env python3
"""
Author : Ken Youens-Clark<kyclark@gmail.com>
Date   : 2020-04-06
Purpose: Create a ransom note
"""

import argparse
import os
import random
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create a ransom note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    # new_text = ''
    # for char in args.text:
    #     new_text += choose(char)

    # print(''.join([choose(char) for char in args.text]))

    print(''.join(map(choose, args.text)))


# --------------------------------------------------
def choose(char):
    """Return an upper or lowercase char"""

    return char.upper() if random.choice([0, 1]) else char.lower()


# --------------------------------------------------
def test_choose():
    """Test choose()"""

    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
