#!/usr/bin/env python3
"""Blackjack"""

import argparse
import random
import re
import sys
from itertools import product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Blackjack',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-d',
                        '--dealer_hits',
                        help='Dealer hits',
                        action='store_true')

    parser.add_argument('-p',
                        '--player_hits',
                        help='Player hits',
                        action='store_true')

    parser.add_argument('-S',
                        '--stand',
                        help='Stand on value',
                        metavar='int',
                        type=int,
                        default=18)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.stand < 1:
        parser.error('--stand "{}" must be greater than 0'.format(args.stand))

    return args


# --------------------------------------------------
def bail(msg):
    """print() and exit(0)"""

    print(msg)
    sys.exit(0)


# --------------------------------------------------
def card_value(card):
    """card to numeric value"""

    vals = {str(i): i for i in range(2, 11)}
    vals.update({'A': 1, 'J': 10, 'Q': 10, 'K': 10})
    val = card[1:]
    assert val in vals
    return vals[val]


# --------------------------------------------------
def make_deck():
    """Make a deck of cards"""

    suites = list('♥♠♣♦')
    values = list(map(str, range(2, 11))) + list('AJQK')
    cards = sorted(map(''.join, product(suites, values)))
    random.shuffle(cards)
    return cards


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    stand_on = args.stand

    random.seed(args.seed)
    cards = make_deck()

    p1, d1, p2, d2 = cards.pop(), cards.pop(), cards.pop(), cards.pop()
    player = [p1, p2]
    dealer = [d1, d2]

    if args.player_hits:
        player.append(cards.pop())
    if args.dealer_hits:
        dealer.append(cards.pop())

    player_hand = sum(map(card_value, player))
    dealer_hand = sum(map(card_value, dealer))

    print('Dealer [{:2}]: {}'.format(dealer_hand, ' '.join(dealer)))
    print('Player [{:2}]: {}'.format(player_hand, ' '.join(player)))

    blackjack = 21
    if player_hand > blackjack:
        bail('Player busts! You lose, loser!')

    if dealer_hand > blackjack:
        bail('Dealer busts.')

    if player_hand == blackjack:
        bail('Player wins. You probably cheated.')

    if dealer_hand == blackjack:
        bail('Dealer wins!')

    if dealer_hand < stand_on:
        print('Dealer should hit.')

    if player_hand < stand_on:
        print('Player should hit.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
