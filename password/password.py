#!/usr/bin/env python3
"""Password maker"""

import argparse
import os
import sys
import re
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--num',
                        metavar='INT',
                        type=int,
                        default=20,
                        help='Number of passwords to generate')

    parser.add_argument('-m',
                        '--min_length',
                        metavar='INT',
                        type=int,
                        default=8,
                        help='Minimum password length')

    parser.add_argument('-x',
                        '--max_length',
                        metavar='INT',
                        type=int,
                        default=20,
                        help='Maximum password length')

    parser.add_argument('-s',
                        '--seed',
                        metavar='INT',
                        type=int,
                        help='Random seed')

    parser.add_argument('-l',
                        '--l33t',
                        action='store_true',
                        help='Obsfuscate letters')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    for fh in args.file:
        for word in fh.read().split():
            words.add(re.sub('[^a-zA-Z]', '', word))

    words = list(words)

    for i in range(args.num):
        password = ''
        while len(password) < args.max_length:
            password += random.choice(words)

        if args.l33t:
            password = l33t(password)

        print(password)

# --------------------------------------------------
def l33t(text):
    """l33t"""

    xform = {'a': '@', 'A': '4', 'o': '0', 'O': '0'}
    for x, y in xform.items():
        text = text.replace(x, y)

    return text

# --------------------------------------------------
if __name__ == '__main__':
    main()
