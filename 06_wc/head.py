#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-13
Purpose: Tiny Python Projects head implementation
"""

import argparse
import sys


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="display initial lines of file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        help="Input file",
        type=argparse.FileType("rt"),
        nargs="?",
        default=sys.stdin,
    )

    parser.add_argument(
        "-l",
        "--lines",
        help="number of lines to display",
        metavar="int",
        type=int,
        default=10,
    )

    return parser.parse_args()


def main():
    """Main program"""

    args = get_args()
    count = 0
    for line in args.file:
        sys.stdout.write(line)
        count += 1
        if count >= args.lines:
            break


if __name__ == "__main__":
    main()
