#!/usr/bin/env python3
"""Crossword helper"""

import argparse
import os
import re
import sys
from typing import List, TextIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crossword helper',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern', metavar='str', help='The pattern to search')

    parser.add_argument('-w',
                        '--wordlist',
                        help='Wordlist to search',
                        metavar='str',
                        type=argparse.FileType('r'),
                        default='/usr/share/dict/words')

    return parser.parse_args()


# --------------------------------------------------
def regex_solution(pattern: str, wordlist: TextIO) -> List[str]:
    """Using regular expressions"""

    regex = r'\b{}\b'.format(pattern.replace('_', '.'))
    return re.findall(regex, wordlist.read())


# --------------------------------------------------
def manual_solution(pattern: str, wordlist: TextIO) -> List[str]:
    """Not using regular expressions"""

    letters = [t for t in enumerate(pattern) if t[1] != '_']
    #letters = filter(lambda t: t[1] != '_', enumerate(pattern))
    wanted_len = len(pattern)
    words = []

    for word in wordlist.read().split():
        if len(word) == wanted_len and all(
            [True if word[i] == char else False for i, char in letters]):
            words.append(word)

    return words


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    words = regex_solution(args.pattern, args.wordlist)
    #words = manual_solution(args.pattern, args.wordlist)

    if words:
        for i, word in enumerate(words, start=1):
            print('{:3}: {}'.format(i, word))
    else:
        print('Found no words matching "{}".'.format(args.pattern))


# --------------------------------------------------
if __name__ == '__main__':
    main()
