#!/usr/bin/env python3
"""Set card game"""

import argparse
import random
from itertools import product, combinations
from typing import List, Tuple


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
def make_deck() -> List[Tuple[str, str, str, str]]:
    """Make Set deck"""

    numbers = ('1', '2', '3')
    colors = ('Red', 'Purple', 'Green')
    shadings = ('Solid', 'Striped', 'Outlined')
    shapes = ('Oval', 'Squiggle', 'Diamond')
    return sorted(product(numbers, colors, shadings, shapes))


# --------------------------------------------------
def test_make_deck():
    """Test make_deck"""

    deck = make_deck()
    assert len(deck) == 81
    assert deck[0] == ('1', 'Green', 'Outlined', 'Diamond')
    assert deck[-1] == ('3', 'Red', 'Striped', 'Squiggle')


# --------------------------------------------------
def is_set(cards: List[tuple]) -> bool:
    """Decide if cards form a set"""

    sets = map(set, zip(*cards))
    return all([len(s) in [1, 3] for s in sets])


# --------------------------------------------------
def test_is_set():
    """Test is_set"""

    assert is_set([tuple('ABCD'), tuple('ABCD'), tuple('ABCD')])
    assert is_set([tuple('ABCD'), tuple('EFGH'), tuple('IJKL')])
    assert not is_set([tuple('ABCD'), tuple('ABCD'), tuple('ABCE')])
    assert is_set([('1', 'Green', 'Outlined', 'Diamond'),
                   ('1', 'Green', 'Outlined', 'Squiggle'),
                   ('1', 'Green', 'Outlined', 'Oval')])
    assert is_set([('1', 'Green', 'Outlined', 'Diamond'),
                   ('2', 'Red', 'Striped', 'Squiggle'),
                   ('3', 'Purple', 'Solid', 'Oval')])
    assert not is_set([('1', 'Green', 'Outlined', 'Diamond'),
                       ('2', 'Red', 'Striped', 'Squiggle'),
                       ('3', 'Green', 'Solid', 'Oval')])


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
        print('\n'.join(sorted(map(' '.join, combo))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
