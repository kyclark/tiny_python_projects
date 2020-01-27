#!/usr/bin/env python3
"""Lookup tables"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter', help='Letter', metavar='str', type=str)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='str',
                        type=argparse.FileType('r'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    letter = args.letter

    for line in args.file:
        if line[0].upper() == letter.upper():
            print(line, end='')
            sys.exit(0)

    print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
