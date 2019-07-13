#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-07-11
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Text for banner')

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
    #                     default=0)

    # parser.add_argument('-o',
    #                     '--on',
    #                     help='A boolean flag',
    #                     action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    print(mk_letter(alpha{'A'}))

# --------------------------------------------------
def mk_letter(letter)
    """Make banner"""

    alpha = {
        'A': '10    _     / \    / _ \   / ___ \  /_/   \_\ '
    }

    assert letter in alpha

    rx = alpha[letter]
    match = re.match('^(\d+)(.+)')
    assert match

    width, pattern = match.groups()
    lines = 


# --------------------------------------------------
if __name__ == '__main__':
    main()
