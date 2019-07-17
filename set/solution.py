#!/usr/bin/env python3
"""Set card game"""

import argparse
import random
import logging
from itertools import product, combinations
from typing import List
from dataclasses import dataclass


# --------------------------------------------------
@dataclass
class Card:
    """Represent a card"""

    color: str; shape: str; number: str; shading: str

    def __str__(self):
        """How to print"""
        return ' '.join([self.number, self.color, self.shading, self.shape])

    def encode_color(self):
        colors = ['Red', 'Purple', 'Green']
        return [1 if self.color == c else 0 for c in colors]

    def encode_shape(self):
        shapes = ['Oval', 'Squiggle', 'Diamond']
        return [1 if self.shape == s else 0 for s in shapes]

    def encode_number(self):
        numbers = ['1', '2', '3']
        return [1 if self.number == n else 0 for n in numbers]

    def encode_shading(self):
        shadings = ['Solid', 'Striped', 'Outlined']
        return [1 if self.shading == s else 0 for s in shadings]


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

    parser.add_argument('-d', '--debug', help='Debug', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def make_deck() -> List[Card]:
    """Make Set deck"""

    colors = ['Red', 'Purple', 'Green']
    shapes = ['Oval', 'Squiggle', 'Diamond']
    number = ['1', '2', '3']
    shading = ['Solid', 'Striped', 'Outlined']

    deck = list(
        map(lambda t: Card(color=t[0], shape=t[1], number=t[2], shading=t[3]),
            product(colors, shapes, number, shading)))

    return list(map(lambda t: t[1], sorted(map(lambda c: (str(c), c), deck))))


# --------------------------------------------------
def test_make_deck():
    """Test make_deck"""

    deck = make_deck()
    assert len(deck) == 81
    assert str(deck[0]) == '1 Green Outlined Diamond'
    assert str(deck[-1]) == '3 Red Striped Squiggle'


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

        if all([n in [1, 3] for n in [color, shape, number, shading]]):
            sets.append(combo)

    return sets


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    deck: List[Card] = make_deck()
    logging.debug('deck =\n%s', '\n'.join(map(str, deck)))

    random.seed(args.seed)
    logging.debug('seed = %s', args.seed)

    random.shuffle(deck)
    logging.debug('shuffled deck =\n%s', '\n'.join(map(str, deck)))

    hand: List[Card] = random.sample(deck, k=12)
    logging.debug('hand =\n%s', '\n'.join(map(str, hand)))

    for i, combo in enumerate(find_set(hand), start=1):
        print(f'Set {i}')
        for j in combo:
            print(f'{j:3}: {hand[j]}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
