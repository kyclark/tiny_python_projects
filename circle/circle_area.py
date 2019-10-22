#!/usr/bin/env python3
"""Calculate area of a circle"""

import argparse
import os
import sys
from math import pi


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-r',
                        '--radius',
                        help='Circle radius',
                        metavar='float',
                        type=float,
                        default=0.)

    parser.add_argument('-d',
                        '--diameter',
                        help='Circle diameter',
                        metavar='float',
                        type=float,
                        default=0.)

    args = parser.parse_args()

    if all(map(lambda v: not v, [args.radius, args.diameter])) or all(
        [args.radius, args.diameter]):
        parser.error('Must choose one of --radius or --diameter')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    radius = args.radius or args.diameter / 2
    print(f'Area = {2 * pi * radius}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
