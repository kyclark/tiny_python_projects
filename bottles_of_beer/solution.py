#!/usr/bin/env python3

import argparse
import sys
from dire import die


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num_bottles',
                        metavar='INT',
                        type=int,
                        default=10,
                        help='How many bottles')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    num_bottles = args.num_bottles

    if num_bottles < 1:
        die('N ({}) must be a positive integer'.format(num_bottles))

    line1 = '{} bottle{} of beer on the wall'
    line2 = '{} bottle{} of beer'
    line3 = 'Take one down, pass it around'
    tmpl = ',\n'.join([line1, line2, line3, line1 + '!'])

    for n in reversed(range(1, num_bottles + 1)):
        s1 = '' if n == 1 else 's'
        s2 = '' if n - 1 == 1 else 's'
        print(tmpl.format(n, s1, n, s1, n - 1, s2))
        if n > 1: print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
