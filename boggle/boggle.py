#!/usr/bin/env python3
"""Boggle"""

import argparse
import os
import random
import sys
from itertools import combinations
from collections import defaultdict, Counter


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Boggle',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('positional',
    #                     metavar='str',
    #                     help='A positional argument')

    # parser.add_argument('-a',
    #                     '--arg',
    #                     help='A named string argument',
    #                     metavar='str',
    #                     type=str,
    #                     default='')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-w',
                        '--wordlist',
                        help='Wordlist',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='/usr/share/dict/words')

    # parser.add_argument('-o',
    #                     '--on',
    #                     help='A boolean flag',
    #                     action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    words = get_words(args.wordlist)

    random.seed(args.seed)

    dice = [
        'U Qu H M N I', 'O B J A O B', 'F F S K A P', 'N S I E U E',
        'E G H W E N', 'S O A C H P', 'T T R E Y L', 'R N Z N H L',
        'R E V L Y D', 'T U I C M O', 'T D T Y S I', 'O O W T T A',
        'N A E A E G', 'R V T H E W', 'L X E D R I', 'O T S E S I'
    ]

    show = list(map(lambda s: random.choice(s.split()), dice))

    for i, die in enumerate(show, start=1):
        print('{:2} '.format(die), end='')
        if i % 4 == 0:
            print()

    i = 0
    found = set()
    for n in range(1, 17):
        print(n)
        for combo in combinations(show, n):
            wanted = Counter(combo)
            for word, counter in words[len(combo)]:
                if counter == wanted and word not in found:
                    found.add(word)

    if found:
        for i, word in enumerate(sorted(found), start=1):
            print('{:5}: {}'.format(i, word))
    else:
        print('Found no words.')


# --------------------------------------------------
def get_words(fh):
    """Return words from file handle grouped by length"""

    words = defaultdict(list)
    for word in fh.read().upper().split():
        words[len(word)].append((word, Counter(word)))

    return words


# --------------------------------------------------
def test_get_words():
    """Test get_words"""

    words = get_words(io.StringIO('apple banana cherry fig'))
    assert len(words[3]) == 1
    assert words[3][0] == ('fig', Counter('fig'))
    assert len(words[5]) == 1
    assert len(words[6]) == 2


# --------------------------------------------------
if __name__ == '__main__':
    main()
