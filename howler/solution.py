#!/usr/bin/env python3
"""Howler"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Howler (upper-case input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='STR', help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    text = args.text
    out_file = args.outfile

    if os.path.isfile(text):
        text = open(text).read()

    out_fh = open(out_file, 'wt') if out_file else sys.stdout
    out_fh.write(text.upper() + '\n')


# --------------------------------------------------
if __name__ == '__main__':
    main()
