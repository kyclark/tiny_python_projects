#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-14
Purpose: Tiny Python Projects tac implementation
"""

import argparse
import sys


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="concatenate file reversed by line",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        help="Input file",
        type=argparse.FileType("r"),
        nargs="?",
        default=sys.stdin,
    )

    return parser.parse_args()


def main():
    """Main program"""

    args = get_args()
    for line in reversed(args.file.readlines()):
        sys.stdout.write(line)


if __name__ == "__main__":
    main()
