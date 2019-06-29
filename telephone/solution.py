#!/usr/bin/env python3
"""Telephone"""

import argparse
import os
import random
import string
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='str',
                        type=str,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='float',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if not 0 < args.mutations <= 1:
        msg = '--mutations "{}" must be b/w 0 and 1'.format(args.mutations)
        parser.error(msg)

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.input
    random.seed(args.seed)

    if os.path.isfile(text):
        text = open(text).read()

    len_text = len(text)
    num_mutations = int(args.mutations * len_text)
    alpha = string.ascii_letters + string.punctuation

    for _ in range(num_mutations):
        i = random.choice(range(len_text))
        text = text[:i] + random.choice(alpha) + text[i+1:]

    print(text.rstrip())

# --------------------------------------------------
if __name__ == '__main__':
    main()
