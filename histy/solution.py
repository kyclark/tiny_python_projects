#!/usr/bin/env python3
"""Histogrammer"""

import argparse
import os
import re
from collections import Counter


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Histogrammer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    parser.add_argument('-s',
                        '--symbol',
                        help='Symbol for marks',
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

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    if args.case_insensitive:
        args.text = args.text.upper()

    if len(args.symbol) != 1:
        parser.error('--symbol "{}" must be one character'.format(args.symbol))

    return args


# --------------------------------------------------
def count(text, minimum=0, width=0, frequency_sort=False):
    """Count characters in text"""

    freqs = Counter(re.findall(r'[a-zA-Z]', text))

    if minimum > 1:
        freqs = {k:v for k,v in freqs.items() if v >= minimum}

    high = max(freqs.values())
    if width > 0 and high > width:
        scale = width / high
        freqs = {k:int(v * scale) for k,v in freqs.items()}

    if frequency_sort:
        return list(
            map(lambda t: (t[1], t[0]),
                sorted([(v, k) for k, v in freqs.items()], reverse=True)))
    else:
        return list(
            map(lambda t: (t[1], t[2]),
                sorted([(k.lower(), k, v) for k, v in freqs.items()])))


# --------------------------------------------------
def test_count():
    """Test count"""

    text = '"ab,Bc CC: dd_d-d"'
    assert count(text) == [('a', 1), ('B', 1), ('b', 1), ('C', 2), ('c', 1),
                           ('d', 4)]

    assert count(text, minimum=2) == [('C', 2), ('d', 4)]

    assert count(text, frequency_sort=True) == [('d', 4), ('C', 2), ('c', 1),
                                                ('b', 1), ('a', 1), ('B', 1)]

    assert count(text, frequency_sort=True, minimum=2) == [('d', 4), ('C', 2)]

    assert count(text, width=3) == [('a', 0), ('B', 0), ('b', 0), ('C', 1),
                                    ('c', 0), ('d', 3)]


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    freqs = count(args.text, args.minimum, args.width, args.frequency_sort)

    for c, num in freqs:
        print('{} {:6} {}'.format(c, num, args.symbol * num))


# --------------------------------------------------
if __name__ == '__main__':
    main()
