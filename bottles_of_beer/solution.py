#!/usr/bin/env python3
"""Bottle of beer song"""

import argparse


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        metavar='INT',
                        type=int,
                        default=10,
                        help='How many bottles')

    args = parser.parse_args()

    if args.num < 1:
        parser.error('--num ({}) must > 0'.format(args.num))

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    tmpl = '\n'.join([
        '{} bottle{} of beer on the wall,',
        '{} bottle{} of beer,',
        'Take one down, pass it around,',
        '{} bottle{} of beer on the wall!',
    ])

    for bottle in reversed(range(1, args.num + 1)):
        next_bottle = bottle - 1
        s1 = '' if bottle == 1 else 's'
        s2 = '' if next_bottle == 1 else 's'
        print(tmpl.format(bottle, s1, bottle, s1, next_bottle, s2))
        if bottle > 1:
            print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
