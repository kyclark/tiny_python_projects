#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-02
Purpose: Ransom Note
"""

import argparse
import os
import random
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    random.seed(args.seed)

    text = args.text
    if os.path.isfile(text):
        text = open(text).read()

    #ransom = []
    #for char in text:
    #    ransom.append(char.upper() if random.choice([0, 1]) else char.lower())

    #ransom = [c.upper() if random.choice([0, 1]) else c.lower() for c in text]

    #ransom = map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(),
    #             text)

    f = lambda c: c.upper() if random.choice([0, 1]) else c.lower()
    ransom = map(f, text)

    print(''.join(ransom))


# --------------------------------------------------
if __name__ == '__main__':
    main()
