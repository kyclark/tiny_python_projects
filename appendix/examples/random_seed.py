#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-17
Purpose: Get/use a random seed from argparse
"""

import argparse
import random
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Get/use a random seed from argparse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    random.seed(args.seed)

    print('Random number is "{}"'.format(random.randint(1, 100)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
