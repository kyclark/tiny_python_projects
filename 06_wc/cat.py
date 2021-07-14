#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-13
Purpose: Tiny Python Projects cat implementation
"""

import argparse
import sys


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='concatenate files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)',
                        type=argparse.FileType('rt'),
                        nargs='*',
                        default=[sys.stdin])


    return parser.parse_args()


def main():
    """Main program"""

    args = get_args()
    for file_handle in args.file:
        for line in file_handle:
            sys.stdout.write(line)

if __name__ == '__main__':
    main()
