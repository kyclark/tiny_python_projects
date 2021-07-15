#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-14
Purpose: Tiny Python Exercises: addressbook
"""

import argparse
import json


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Print line(s) from file specified by parameters",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        default="addressbook.json",
        type=argparse.FileType("rt"),
        help="Input file in json format",
        metavar="FILE",
    )

    parser.add_argument("entry", help="Name of person", metavar="entry")

    return parser.parse_args()


def main():
    """Main program"""

    args = get_args()
    addresses = json.load(args.file)
    if args.entry in addresses:
        print(
            addresses[args.entry]["emailAddress"]
            + "\n"
            + addresses[args.entry]["phoneNumber"]
        )
    else:
        print(f'I do not have an entry for "{args.entry}".')


if __name__ == "__main__":
    main()
