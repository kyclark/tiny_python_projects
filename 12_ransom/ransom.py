#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-28
Purpose: Tiny Python Projects Ransom exercise
"""

import argparse
import os
import random
from re import A


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Ransom Note",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-s", "--seed", default=None, type=int, help="Random seed", metavar="int"
    )

    parser.add_argument("-a", "--ascii", action="store_true", help="Convert to ASCII symbols")

    parser.add_argument("text", help="Input text or file", metavar="text")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def choose(char):
    """Randomly capitalize input character"""
    return char.lower() if random.choice([True, False]) else char.upper()


def test_choose():
    """Test choose()"""
    state = random.getstate()
    random.seed(1)
    assert choose("a") == "a"
    assert choose("b") == "b"
    assert choose("c") == "C"
    assert choose("d") == "d"
    random.setstate(state)

def ascii(char):
    """Convert characters to ASCII synbols"""
    table = {
        'A' : '4',
        'B' : '|3',
        'C' : '(',
        'D' : '|)',
        'E' : '3',
        'F' : '|=',
        'G' : '(-',
        'H' : '|-|',
        'I' : '1',
        'J' : '_|',
        'K' : '|<',
        'L' : '|_',
        'M' : '|\\/|',
        'N' : '|\\|',
        'P' : '|`',
        'S' : '5',
        'T' : '+',
        'V' : '\\/',
        'W' : '\\/\\/'
    }
    char = char.upper()
    return table.get(char, char)

def test_ascii():
    assert ascii('A') == '4'
    assert ascii('e') == '3'
    assert ascii('q') == 'Q'
    assert ascii('W') == '\\/\\/'
    assert ascii('z') == 'Z'


def main():
    """Main program"""

    args = get_args()
    random.seed(args.seed)
    # for char in list(args.text):
    #     new_chars.append(choose(char))
    # print("".join(choose(char) for char in list(args.text)))
    print("".join(map(choose, args.text))) if not args.ascii else print("".join(map(ascii, args.text)))


if __name__ == "__main__":
    main()
