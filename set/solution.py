#!/usr/bin/env python3
"""Set card game"""

import argparse
import os
import random
import sys
from itertools import product, combinations
from card import Card
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
def make_deck() -> List[Card]:
    """Make Set deck"""

    colors = ['Red', 'Purple', 'Green']
    shapes = ['Oval', 'Squiggle', 'Diamond']
    number = ['1', '2', '3']
    shading = ['Solid', 'Striped', 'Outlined']

    return list(
        map(lambda t: Card(color=t[0], shape=t[1], number=t[2], shading=t[3]),
            product(colors, shapes, number, shading)))


# --------------------------------------------------
def test_make_deck():
    """Test make_deck"""

    deck = make_deck()
    assert len(deck) == 81


# --------------------------------------------------
def add(bits: List[list]) -> int:
    """Add the bits"""

    assert isinstance(bits, list)
    assert isinstance(bits[0], list)

    num_recs = len(bits)
    num_bits = len(bits[0])

    ret = []
    for i in range(num_bits):
        ret.append(1 if any(map(lambda n: bits[n][i], range(num_recs))) else 0)

    return sum(ret)


# --------------------------------------------------
def find_set(cards: List[Card]) -> List[tuple]:
    """Find a 'set' in a hand of cards"""

    colors = list(map(lambda c: c.encode_color(), cards))
    shapes = list(map(lambda c: c.encode_shape(), cards))
    numbers = list(map(lambda c: c.encode_number(), cards))
    shadings = list(map(lambda c: c.encode_shading(), cards))

    sets = []
    for combo in combinations(range(len(cards)), 3):
        color = add(list(map(lambda i: colors[i], combo)))
        shape = add(list(map(lambda i: shapes[i], combo)))
        number = add(list(map(lambda i: numbers[i], combo)))
        shading = add(list(map(lambda i: shadings[i], combo)))

        if all([x in [1, 3] for x in [color, shape, number, shading]]):
            sets.append(combo)

    return sets

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    deck: List[Card] = make_deck()

    random.seed(args.seed)
    cards: List[Card] = random.sample(deck, k=12)

    for combo in find_set(cards):
        print(combo)
        print('\n'.join(map(lambda i: str(cards[i]), combo)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
