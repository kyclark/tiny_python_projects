#!/usr/bin/env python3
"""Boggle"""

import argparse
import io
import random
import sys
from itertools import combinations
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Boggle',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--output',
                        help='Output words to file',
                        metavar='FILE',
                        type=str,
                        default=None)

    parser.add_argument('-w',
                        '--wordlist',
                        help='Wordlist',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='/usr/share/dict/words')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    words = get_words(args.wordlist)
    random.seed(args.seed)

    dice = ['O B J A O B', 'F F S K A P', 'N S I E U E', 'E G H W E N',
            'S O A C H P', 'T T R E Y L', 'R N Z N H L', 'R E V L Y D',
            'T U I C M O', 'T D T Y S I', 'O O W T T A', 'N A E A E G',
            'R V T H E W', 'L X E D R I', 'O T S E S I', 'U QU H M N I']

    show = list(map(lambda s: random.choice(s.split()), dice))
    for i, die in enumerate(show, start=1):
        print('{:2} '.format(die), end='\n' if i % 4 == 0 else '')

    combos_by_len = defaultdict(set)
    for n in range(3, 17):
        for combo in map(lambda c: ''.join(sorted(''.join(c))),
                         combinations(show, n)):

            combos_by_len[len(combo)].add(combo)

    found = []
    for n, combos in combos_by_len.items():
        lookup = defaultdict(set)
        for word in words[n]:
            lookup[''.join(sorted(word))].add(word)

        for combo in combos:
            found.extend(lookup[combo])

    point_value = { 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11 }
    points = 0
    out_fh = open(args.output, 'wt') if args.output else sys.stdout
    if found:
        for i, word in enumerate(sorted(found), start=1):
            n = len(word)
            points += point_value[n] if n in point_value else point_value[8]
            out_fh.write('{:5}: {}\n'.format(i, word))
        print(f'Total points = {points}')
    else:
        print('Found no words.')


# --------------------------------------------------
def get_words(fh):
    """Return words from file handle grouped by length"""

    words = defaultdict(list)
    for word in fh.read().upper().split():
        words[len(word)].append(word)
    return words


# --------------------------------------------------
def test_get_words():
    """Test get_words"""

    words = get_words(io.StringIO('apple banana cherry fig'))
    assert len(words[3]) == 1
    assert 'FIG' in words[3]
    assert len(words[5]) == 1
    assert len(words[6]) == 2


# --------------------------------------------------
if __name__ == '__main__':
    main()
