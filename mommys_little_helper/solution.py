#!/usr/bin/env python3
"""Crossword helper"""

import argparse
import io
import re
from typing import List, TextIO


# --------------------------------------------------
def get_args() -> argparse.Namespace:
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
def test_regex_solution():
    """Test regex_solution"""

    text = lambda: io.StringIO('apple banana cherry date')
    assert regex_solution('_ppl_', text()) == ['apple']
    assert regex_solution('c_e_ry', text()) == ['cherry']


# --------------------------------------------------
def manual_solution(pattern: str, wordlist: TextIO) -> List[str]:
    """Not using regular expressions"""

    letters = filter(lambda t: t[1] != '_', enumerate(pattern))
    wanted_len = len(pattern)

    return list(
        filter(
            lambda word: len(word) == wanted_len and all(
                [word[i] == char for i, char in letters]),
            wordlist.read().split()))


# --------------------------------------------------
def test_manual_solution():
    """Test manual_solution"""

    text = lambda: io.StringIO('apple banana cherry date')
    assert manual_solution('_ppl_', text()) == ['apple']
    assert manual_solution('c_e_ry', text()) == ['cherry']


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
