#!/usr/bin/env python3
"""Twelve Days of Christmas"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile (STDOUT)',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='int',
                        type=int,
                        default=12)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_days = args.num
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout

    days = [
        'A partridge in a pear tree.',
        'Two turtle doves',
        'Three French hens',
        'Four calling birds',
        'Five gold rings',
        'Six geese a laying',
        'Seven swans a swimming',
        'Eight maids a milking',
        'Nine ladies dancing',
        'Ten lords a leaping',
        'Eleven pipers piping',
        'Twelve drummers drumming',
    ]

    if not num_days in range(1, len(days) + 1):
        print('Cannot sing "{}" days'.format(num_days))
        sys.exit(1)

    ordinal = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleven', 'twelfth'
    ]

    first = 'On the {} day of Christmas,\nMy true love gave to me,'
    for i in range(1, num_days + 1):
        out_fh.write(first.format(ordinal[i - 1]) + '\n')
        lines = list(reversed(days[:i]))
        if len(lines) > 1:
            lines[-1] = 'And ' + lines[-1].lower()
        _ = out_fh.write(',\n'.join(lines) +
                         ('\n\n' if i < num_days else '\n'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
