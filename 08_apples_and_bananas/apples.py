#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-15
Purpose: Tiny Python Projects exercise: Find and replace 
"""

import argparse
import os
import io


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Apples and bananas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-v",
        "--vowel",
        default="a",
        type=str,
        choices=list('aeiou'),
        help="The vowel to substitute",
        metavar="vowel",
    )

    parser.add_argument("text", help="Input text or file", metavar="text")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text, "rt")
    else:
        args.text = io.StringIO(args.text + "\n")

    return args


def main():
    """Main program"""

    args = get_args()
    table = {
        "a": args.vowel,
        "e": args.vowel,
        "i": args.vowel,
        "o": args.vowel,
        "u": args.vowel,
        "A": args.vowel.upper(),
        "E": args.vowel.upper(),
        "I": args.vowel.upper(),
        "O": args.vowel.upper(),
        "U": args.vowel.upper(),
    }
    for line in args.text:
        line = line.translate(str.maketrans(table))
        print(line.rstrip())


if __name__ == "__main__":
    main()
