#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-14
Purpose: Tiny Python Exercises: gashlycrumb (interactive version)
"""

import argparse


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Print line(s) from file specified by parameters",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        default="gashlycrumb.txt",
        type=argparse.FileType("rt"),
        help="Input file",
        metavar="FILE",
    )

    return parser.parse_args()


def main():
    """Main program"""

    args = get_args()
    phrases = {line[0].upper(): line.rstrip() for line in args.file}
    while True:
        print('Enter a letter: ')
        letter = input()
        if (letter == '!'):
            break
        else:
            print(phrases.get(letter.upper(), f'I do not know "{letter}".'))


if __name__ == "__main__":
    main()
