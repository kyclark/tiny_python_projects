#!/usr/bin/env python3

import argparse
import os
import sys
import time


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Movie Reader',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    if os.path.isfile(text):
        text = open(text).read()

    for line in text.splitlines():
        for char in line:
            print(char, end='')
            time.sleep(.5 if char in '.!?\n' else .2 if char in ',:;' else .05)
            sys.stdout.flush()

        print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
