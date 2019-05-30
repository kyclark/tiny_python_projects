#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-13
Purpose: Tranpose ABC notation
"""

import argparse
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tranpose ABC notation',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar='FILE', help='Input file')

    parser.add_argument(
        '-s',
        '--shift',
        help='Interval to shift',
        metavar='int',
        type=int,
        default=2)

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
    file = args.file
    shift = args.shift
    ucase = 'ABCDEFG'
    lcase = 'abcdefg'
    num_notes = 7

    if not 1 < abs(shift) <= 8:
        die('--shift "{}" must be between 2 and 8'.format(shift))

    if not os.path.isfile(file):
        die('"{}" is not a file'.format(file))

    # account for interval where a 2nd (-s 2) is a move of one note
    shift = shift - 1 if shift > 0 else shift + 1

    def transpose(note):
        if note in lcase:
            pos = lcase.index(note)
            tran = (pos + shift) % num_notes
            return lcase[tran]
        elif note in ucase:
            pos = ucase.index(note)
            tran = (pos + shift) % num_notes
            return ucase[tran]
        else:
            return note

    for line in open(file):
        line = line.rstrip()

        if line.startswith('K:'):
            key = line[2]
            print('K:' + transpose(key))
        elif (line.startswith('<') and line.endswith('>')) or re.match(
                '[A-Z]:\s?', line):
            print(line)
        else:
            for char in line.rstrip():
                print(transpose(char), end='')

            print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
