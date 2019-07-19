#!/usr/bin/env python3
"""Set card game"""

import argparse
import random
from itertools import product, combinations
from typing import List


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def make_deck() -> List[str]:
    """Make Set deck"""

    colors = ['Red', 'Purple', 'Green']
    shapes = ['Oval', 'Squiggle', 'Diamond']
    numbers = ['1', '2', '3']
    shadings = ['Solid', 'Striped', 'Outlined']

    return sorted(map(' '.join, product(numbers, colors, shadings, shapes)))


# --------------------------------------------------
def test_make_deck():
    """Test make_deck"""

    deck = make_deck()
    assert len(deck) == 81
    assert deck[0] == '1 Green Outlined Diamond'
    assert deck[-1] == '3 Red Striped Squiggle'


# --------------------------------------------------
def is_set(cards: List[str]) -> bool:
    """Decide if cards form a set"""

    bits = map(set, zip(*[c.split() for c in cards]))
    return all([len(b) in [1,3] for b in bits])


# --------------------------------------------------
def test_is_set():
    """Test is_set"""

    assert is_set(['A B C D'] * 3)
    assert is_set(['A B C D'], ['E F G H'], ['I J K L']])
    assert not is_set(['A B C D', 'A B C D', 'A B C E'])
    assert is_set([
        '1 Green Outlined Diamond', '1 Green Outlined Squiggle',
        '1 Green Outlined Oval'
    ])
    assert is_set([
        '1 Green Outlined Diamond', '2 Red Striped Squiggle',
        '3 Purple Solid Oval'
    ])
    assert not is_set([
        '1 Green Outlined Diamond', '2 Red Striped Squiggle',
        '3 Green Solid Oval'
    ])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    deck = make_deck()
    random.shuffle(deck)

    hand = random.sample(deck, k=12)
    sets = filter(is_set, combinations(hand, 3))

    for i, combo in enumerate(sets, start=1):
        print(f'Set {i}')
        print('\n'.join(sorted(combo)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
