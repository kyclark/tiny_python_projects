#!/usr/bin/env python3
"""Rummikub"""

import argparse
import os
import sys
import random
from itertools import combinations, product
from typing import List


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rummikub',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def make_tiles():
    """Make tiles"""

    return list(product(list('BYRK'), range(1, 14))) * 2


# --------------------------------------------------
def test_make_tiles():
    """Test make_tiles"""

    tiles = make_tiles()
    assert len(tiles) == 104
    assert len(list(filter(lambda tile: tile[0] == 'R', tiles))) == 26
    assert len(list(filter(lambda tile: tile[1] == 1, tiles))) == 8
    assert len(
        list(filter(lambda tile: tile[0] == 'K' and tile[1] == 10,
                    tiles))) == 2


# --------------------------------------------------
def fst(t):
    """Return first element of a tuple"""

    return t[0]


# --------------------------------------------------
def snd(t):
    """Return second element of a tuple"""

    return t[1]


# --------------------------------------------------
def diffs(a: List[int]) -> List[int]:
    """Return the pairwise differences between all elements of a list"""
    a.sort()
    return [abs(a[n] - a[n + 1]) for n in range(len(a) - 1)]


# --------------------------------------------------
def test_diffs():
    """Test diffs"""

    assert diffs([1, 2, 3]) == [1, 1]
    assert diffs([4, 1, 6]) == [3, 2]
    assert diffs([1, 1, 1]) == [0, 0]


# --------------------------------------------------
def is_set(tiles):
    """Determine if tiles are a set"""

    num_tiles = len(tiles)
    colors = set(map(fst, tiles))
    nums = set(map(snd, tiles))

    # A set of 3-4 tiles all the same number and different colors
    if (3 <= num_tiles <=
            4) and (len(colors) == num_tiles) and (len(nums) == 1):
        return True

    # 3 or more consecutive numbers of the same color 
    if (num_tiles >= 3) and (len(colors) == 1) and all(
        map(lambda n: n == 1, diffs(list(map(snd, tiles))))):
        return True

    return False


# --------------------------------------------------
def test_is_set():
    """Test is_set"""

    assert is_set([('R', 1), ('Y', 1), ('K', 1)])
    assert is_set([('B', 7), ('Y', 7), ('K', 7), ('R', 7)])
    assert not is_set([('Y', 1), ('K', 1)])
    assert not is_set([('B', 8), ('Y', 7), ('K', 7), ('R', 7)])

    assert is_set([('R', 1), ('R', 2), ('R', 3)])
    assert is_set([('K', 3), ('K', 4), ('K', 5), ('K', 7), ('K', 6)])
    assert not is_set([('K', 2), ('K', 4), ('K', 5), ('K', 7), ('K', 6)])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    tiles = make_tiles()
    random.shuffle(tiles)
    tiles = random.sample(tiles, k=14)
    show = lambda t: '{}{}'.format(*t)
    seen = set()

    i = 0
    for n in range(3, len(tiles)):
        for combo in filter(is_set, combinations(tiles, n)):
            combo = tuple(sorted(combo))
            if combo in seen:
                continue
            seen.add(combo)
            i += 1
            print('{:3}: {}'.format(i, ' '.join(map(show, sorted(combo)))))

    if i == 0:
        print('Found no sets.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
