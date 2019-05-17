#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-03-15
Purpose: Rock the Casbah
"""

import argparse
import random
import re
import sys
from itertools import product


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

    parser.add_argument(
        '-d',
        '--dealer_hits',
        help='Dealer hits',
        action='store_true')

    parser.add_argument(
        '-p',
        '--player_hits',
        help='Player hits',
        action='store_true')

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
def bail(msg):
    """print() and exit(0)"""
    print(msg)
    sys.exit(0)

# --------------------------------------------------
def card_value(card):
    """card to numeric value"""
    val = card[1:]
    faces = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}
    if val.isdigit():
        return int(val)
    elif val in faces:
        return faces[val]
    else:
        die('Unknown card value for "{}"'.format(card))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    random.seed(args.seed)

    # seed = args.seed
    # if seed is not None:
    #     random.seed(seed)

    suites = list('♥♠♣♦')
    values = list(range(2, 11)) + list('AJQK')
    cards = sorted(map(lambda t: '{}{}'.format(*t), product(suites, values)))
    random.shuffle(cards)

    p1, d1, p2, d2 = cards.pop(), cards.pop(), cards.pop(), cards.pop()
    player = [p1, p2]
    dealer = [d1, d2]

    if args.player_hits:
        player.append(cards.pop())

    if args.dealer_hits:
        dealer.append(cards.pop())

    player_hand = sum(map(card_value, player))
    dealer_hand = sum(map(card_value, dealer))

    print('D [{:2}]: {}'.format(dealer_hand, ' '.join(dealer)))
    print('P [{:2}]: {}'.format(player_hand, ' '.join(player)))

    if player_hand > 21:
        bail('Player busts! You lose, loser!')
    elif dealer_hand > 21:
        bail('Dealer busts.')
    elif player_hand == 21:
        bail('Player wins. You probably cheated.')
    elif dealer_hand == 21:
        bail('Dealer wins!')

    if dealer_hand < 18:
        print('Dealer should hit.')

    if player_hand < 18:
        print('Player should hit.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
