#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-25
Purpose: Scramble the letters of words, leaving first and last in place
"""

import argparse
import os
import re
import random
import sys
from itertools import chain


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='STR', help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def scramble(word):
    """For words over 3 characters, shuffle the letters in the middle"""

    if len(word) > 3:
        orig = list(word[1:-1])
        middle = orig.copy()
        while middle == orig:
            random.shuffle(middle)
        word = word[0] + ''.join(middle) + word[-1]

    return word


# --------------------------------------------------
def splitter(s, regex, fn=None):
    """
    Params:
    - a string to split on
    - a regular expression
    - an optional function to apply to the regex matches
    Returns:
    - the input string broken into the parts that match the
      regex (optionally transformed by the fn) and the bits 
      in between the parts that match the regex
    """

    # Find all the parts of the string that match the regex
    # This will be a list like [(0, 2), (3, 8), (9, 12)]
    spans = [m.span() for m in regex.finditer(s)]

    # Flatten that into [0, 2, 3, 8, 9, 12]
    gaps = list(chain(*spans))

    # Bail if there is nothing
    if not gaps: return []

    # Make sure the list includes the start and end of the string
    if gaps[0] != 0: gaps.insert(0, 0)
    if gaps[-1] != len(s): gaps.append(len(s))

    # Find all the substrings, optionally apply the function if the
    # (start, stop) was in the list of spans matched by the regex.
    for i in range(0, len(gaps) - 1):
        start = gaps[i]
        stop = gaps[i + 1]
        substr = s[start:stop]
        if (start, stop) in spans and fn:
            substr = fn(substr)

        yield substr


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    random.seed(args.seed)

    if os.path.isfile(text):
        text = open(text).read()

    regex = re.compile(r"([a-zA-Z']+)")
    for line in text.splitlines():
        print(''.join(splitter(line, regex, scramble)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
