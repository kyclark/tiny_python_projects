#!/usr/bin/env python3
""" Make ASCII table """

import argparse
import pandas as pd


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make ASCII table',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c',
                        '--cols',
                        help='Number of columns',
                        metavar='int',
                        type=int,
                        default=8)

    parser.add_argument('-l',
                        '--lower',
                        help='Lower chr value',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-u',
                        '--upper',
                        help='Upper chr value',
                        metavar='int',
                        type=int,
                        default=128)

    args = parser.parse_args()

    if args.lower < 0:
        parser.error(f'--lower "{args.lower}" must be >= 0')

    if args.upper > 128:
        parser.error(f'--upper "{args.upper}" must be <= 128')

    if args.lower > args.upper:
        args.lower, args.upper = args.upper, args.lower

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    lower = args.lower
    upper = args.upper
    num_cells = args.upper - args.lower
    num_rows = round(num_cells / args.cols)
    cells = list(chunker(list(map(cell, range(lower, upper))), num_rows))
    df = pd.DataFrame(cells)

    for i, row in df.T.iterrows():
        print('  '.join(map(lambda v: v or ' ' * 5, row)))


# --------------------------------------------------
def cell(n):
    """Format a cell"""

    return '{:3} {:5}'.format(
        n, 'SPACE'
        if n == 32 else 'DEL' if n == 127 else chr(n) if n >= 33 else 'NA')


# --------------------------------------------------
def chunker(seq, size):
    """Chunk a list into bits"""

    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


# --------------------------------------------------
if __name__ == '__main__':
    main()
