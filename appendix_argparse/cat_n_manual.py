#!/usr/bin/env python3
"""Python version of `cat -n`, manually checking file argument"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python version of `cat -n`',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='str', type=str, help='Input file')

    args = parser.parse_args()

    if not os.path.isfile(args.file):
        parser.error(f'"{args.file}" is not a file')

    args.file = open(args.file)

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for i, line in enumerate(args.file, start=1):
        print(f'{i:6}  {line}', end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
