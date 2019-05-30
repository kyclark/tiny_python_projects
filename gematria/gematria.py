#!/usr/bin/env python3
"""Gematria"""

import argparse
import os
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
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

    def clean(word):
        return re.sub('[^a-zA-Z0-9]', '', word)

    for line in text.splitlines():
        words = line.rstrip().split()
        nums = map(lambda word: str(sum(map(ord, clean(word)))), words)
        print(' '.join(nums))


# --------------------------------------------------
if __name__ == '__main__':
    main()
