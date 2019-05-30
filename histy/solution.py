#!/usr/bin/env python3
"""Histogrammer"""

import argparse
import os
import re
from collections import Counter
from dire import die


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Histogrammer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    parser.add_argument('-c',
                        '--character',
                        help='Character for marks',
                        metavar='str',
                        type=str,
                        default='|')

    parser.add_argument('-m',
                        '--minimum',
                        help='Minimum frequency to print',
                        metavar='int',
                        type=int,
                        default=1)

    parser.add_argument('-w',
                        '--width',
                        help='Maximum width of output',
                        metavar='int',
                        type=int,
                        default=70)

    parser.add_argument('-i',
                        '--case_insensitive',
                        help='Case insensitive search',
                        action='store_true')

    parser.add_argument('-f',
                        '--frequency_sort',
                        help='Sort by frequency',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    char = args.character
    width = args.width
    min_val = args.minimum

    if len(char) != 1:
        die('--character "{}" must be one character'.format(char))

    if os.path.isfile(text):
        text = open(text).read()
    if args.case_insensitive:
        text = text.upper()

    freqs = Counter(filter(lambda c: re.match(r'\w', c), list(text)))
    high = max(freqs.values())
    scale = high / width if high > width else 1
    items = map(lambda t: (t[1], t[0]),
                sorted([(v, k) for k, v in freqs.items()],
                       reverse=True)) if args.frequency_sort else sorted(
                           freqs.items())

    for c, num in items:
        if num < min_val:
            continue
        print('{} {:6} {}'.format(c, num, char * int(num / scale)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
