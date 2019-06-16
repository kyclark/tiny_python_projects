#!/usr/bin/env python3
"""Coin combos for value"""

import argparse
from itertools import product
from functools import partial


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Coin combos for value',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('value', metavar='int', type=int, help='Sum')

    args = parser.parse_args()

    if not 0 < args.value <= 100:
        parser.error('value "{}" must be > 1 and <= 100'.format(args.value))

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    value = args.value
    nickels = range((value // 5) + 1)
    dimes = range((value // 10) + 1)
    quarters = range((value // 25) + 1)
    fig = partial(figure, value)
    combos = [c for c in map(fig, product(nickels, dimes, quarters)) if c]

    print('If you give me {} cent{}, I can give you:'.format(
        value, '' if value == 1 else 's'))

    for i, combo in enumerate(combos, 1):
        print('{:3}: {}'.format(i, fmt_combo(combo)))


# --------------------------------------------------
def fmt_combo(combo):
    """English version of combo"""

    out = []
    for coin, val in zip(('quarter', 'dime', 'nickel', 'penny'), combo):
        if val:
            plural = 'pennies' if coin == 'penny' else coin + 's'
            out.append('{} {}'.format(val, coin if val == 1 else plural))

    return ', '.join(out)


# --------------------------------------------------
def figure(value, coins):
    """
    If there is a valid combo of 'coins' in 'value',
    return a tuple of ints for (quarters, dimes, nickels, pennies)
    """

    nickels, dimes, quarters = coins
    big_coins = (5 * nickels) + (10 * dimes) + (25 * quarters)

    if big_coins <= value:
        return (quarters, dimes, nickels, value - big_coins)


# --------------------------------------------------
if __name__ == '__main__':
    main()
