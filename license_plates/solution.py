#!/usr/bin/env python3
"""License plate regular expression"""

import argparse
import re
from itertools import product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='License plate regular expression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('plate', metavar='PLATE', help='License plate')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    plate = args.plate
    mixups = [('5', 'S'), ('X', 'K', 'Y'), ('1', 'I'), ('3', 'E'),
              ('D', '0', 'O', 'Q'), ('M', 'N'), ('U', 'V', 'W'), ('2', '7')]

    def find(char):
        group = list(filter(lambda t: char in t, mixups)) or [(char, )]
        return group[0]

    chars = list(map(find, plate))
    regex = '^{}$'.format(''.join(
        map(lambda t: '[' + ''.join(t) + ']' if len(t) > 1 else t[0], chars)))

    print('plate = "{}"'.format(plate))
    print('regex = "{}"'.format(regex))

    for combo in map(''.join, sorted(product(*chars))):
        print(combo, 'Match' if re.search(regex, combo) else 'Miss')


# --------------------------------------------------
if __name__ == '__main__':
    main()
