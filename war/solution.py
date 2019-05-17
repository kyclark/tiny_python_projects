#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-03-18
Purpose: Cardgame "War"
"""

import argparse
import random
import sys
from itertools import product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='"War" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    seed = args.seed

    if seed is not None:
        random.seed(seed)

    suits = list('♥♠♣♦')
    values = list(map(str, range(2, 11))) + list('JQKA')
    cards = sorted(map(lambda t: '{}{}'.format(*t), product(suits, values)))
    random.shuffle(cards)

    p1_wins = 0
    p2_wins = 0

    card_value = dict(
        list(map(lambda t: list(reversed(t)), enumerate(list(values)))))

    while cards:
        p1, p2 = cards.pop(), cards.pop()
        v1, v2 = card_value[p1[1:]], card_value[p2[1:]]
        res = ''

        if v1 > v2:
            p1_wins += 1
            res = 'P1'
        elif v2 > v1:
            p2_wins += 1
            res = 'P2'
        else:
            res = 'WAR!'

        print('{:>3} {:>3} {}'.format(p1, p2, res))

    print('P1 {} P2 {}: {}'.format(
        p1_wins, p2_wins, 'Player 1 wins'
        if p1_wins > p2_wins else 'Player 2 wins'
        if p2_wins > p1_wins else 'DRAW'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
