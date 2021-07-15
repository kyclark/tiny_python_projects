#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-14
Purpose: Tiny Python Exercises: populate dictionary to count unique words
"""

import argparse
import string
from pprint import pprint as pp


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Print unique word count",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        nargs=1,
        default="",
        type=argparse.FileType("rt"),
        help="Input file",
        metavar="FILE",
    )

    return parser.parse_args()


def main():
    """Main program"""

    args = get_args()
    dictionary = {}
    for line in args.file[0]:
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.translate(str.maketrans('', '', string.digits))
        line = line.upper()
        for entry in line.split():
            if entry in dictionary:
                dictionary[entry] += 1
            else:
                dictionary[entry] = 1
    print(len(dictionary))

if __name__ == "__main__":
    main()
