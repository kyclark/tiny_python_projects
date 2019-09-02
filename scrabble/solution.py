#!/usr/bin/env python3
"""Scrabble simulator"""

import argparse
import io
import os
import random
import sys
from collections import defaultdict, Counter
from itertools import chain, combinations
from typing import Iterator, Dict, List


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scrabble',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-t',
                        '--tiles',
                        help='Input tiles',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-l',
                        '--length',
                        help='Word length',
                        metavar='int',
                        type=int,
                        default=0)

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

    args = parser.parse_args()

    if len(args.tiles) > 7:
        parser.error('--tiles "{}" can only be 7 characters'.format(args.tiles))

    return args


# --------------------------------------------------
def make_tiles():
    """Scrabble tile distribution"""

    tile_number = { '_': 2, 'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12,
        'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2,
        'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4,
        'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1,
    }

    return list(chain(*[list(tile * num)
                        for tile, num in tile_number.items()]))


# --------------------------------------------------
def get_words(fh):
    """Return words from file handle grouped by length"""

    words = defaultdict(list)
    for word in fh.read().upper().split():
        words[len(word)].append((word, Counter(word)))

    return words


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    words = get_words(args.wordlist)
    bag = make_tiles()
    random.seed(args.seed)
    random.shuffle(bag)
    tiles = args.tiles or random.sample(bag, k=7)
    print('Tiles = "{}"'.format(''.join(tiles)))

    search = [args.length - 1] if args.length else list(range(1, 8))
    i = 0
    for n in search:
        combos = list(combinations(tiles, n))
        for combo in combos:
            chars = Counter(combo)
            combo = sorted(combo)
            for word, char_cnt in words[n + 1]:
                if all([char_cnt[char] == cnt for char, cnt in chars.items()]):
                    i += 1
                    print('{:6}: {} => {}'.format(i, ''.join(combo), word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
