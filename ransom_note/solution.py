#!/usr/bin/env python3
"""Ransom note"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def choose(c):
    """Randomly choose an upper or lowercase letter to return"""

    return c.upper() if random.choice([0, 1]) else c.lower()


# --------------------------------------------------
def test_choose():
    """Test choose"""

    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.seed(None)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    text = args.text
    random.seed(args.seed)

    # Method 1: Iterate each character, add to list
    ransom = []
    for char in text:
        ransom.append(char.upper() if random.choice([0, 1]) else char.lower())

    # Method 2: List comprehension
    #ransom = [c.upper() if random.choice([0, 1]) else c.lower() for c in text]

    # Method 3: List comprehension with function
    #ransom = [choose(c) for c in text]

    # Method 4: map with lambda
    # ransom = map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(),
    #              text)

    # Method 5: map with function
    # ransom = map(choose, text)

    print(''.join(ransom))


# --------------------------------------------------
if __name__ == '__main__':
    main()
