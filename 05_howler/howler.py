#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='A positional argument',
                        default='../inputs/fox.txt')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file path (relative) string',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    # Check if input is a string or valid filename  
    args.text = open(args.text).read() if os.path.isfile(args.text) else args.text

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
   
    # Open output file or stdout
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper())
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
