#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-06-10
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

    parser.add_argument('-n',
                        '--num',
                        help='Number of coins',
                        metavar='int',
                        type=int,
                        default=10000)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    n = args.num
    coins = ['h'] * n

    for step in range(1, n + 1):
        print('step ', step)
        for i in range(0, n, step):
            print(i)
            coins[i] = 't' if coins[i] == 'h' else 'h'


    for i, coin in enumerate(coins, 1):
        if coin == 't':
            print('{:5}: {}'.format(i, coin))

    print('# heads = {}'.format(len([c for c in coins if c == 'h'])))
    print('# tails = {}'.format(len([c for c in coins if c == 't'])))

# --------------------------------------------------
if __name__ == '__main__':
    main()
