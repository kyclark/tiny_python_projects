#!/usr/bin/env python3
"""Nickel and Dime"""

import argparse
import os
import random
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--nickels',
                        help='Number of nickels',
                        metavar='int',
                        type=int,
                        default=2018)

    parser.add_argument('-d',
                        '--dimes',
                        help='Number of dimes',
                        metavar='int',
                        type=int,
                        default=2019)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    nickels = args.nickels
    dimes = args.dimes

    def mk_jar(n, d):
        return (['n'] * nickels) + (['d'] * dimes)

    jar = mk_jar(nickels, dimes)
    while len(jar) > 1:
        c1, c2 = random.sample(jar, k=2)

        if c1 == 'd' and c2 == 'd':
            dimes -= 1
        elif c1 == 'n' and c2 == 'n':
            nickels -= 2
            dimes += 1
        else:
            dimes -= 1
            nickels += 1

        jar = mk_jar(nickels, dimes)

    print(jar)


# --------------------------------------------------
if __name__ == '__main__':
    main()
