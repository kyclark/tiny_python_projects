#!/usr/bin/env python3
"""Lookup tables"""

import argparse
import os
from dire import die


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
                        type=str,
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    letter = args.letter.upper()
    file = args.file

    if not os.path.isfile(file):
        die('--file "{}" is not a file.'.format(file))

    if len(letter) != 1:
        die('"{}" is not 1 character.'.format(letter))

    lookup = {}
    for line in open(file):
        lookup[line[0]] = line.rstrip()

    if letter in lookup:
        print(lookup[letter])
    else:
        print('I do not know "{}".'.format(letter))


# --------------------------------------------------
if __name__ == '__main__':
    main()
