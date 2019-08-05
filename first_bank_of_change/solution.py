#!/usr/bin/env python3
"""Coin combos for value"""

import argparse
from itertools import product, starmap
from functools import partial


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='First Bank of Change',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('value', metavar='int', type=int, help='Sum')

    args = parser.parse_args()

    if not 0 < args.value <= 100:
        parser.error('value "{}" must be > 0 and <= 100'.format(args.value))

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
    combos = [c for c in map(fig, product(quarters, dimes, nickels)) if c]

    print('If you give me {} cent{}, I can give you:'.format(
        value, '' if value == 1 else 's'))

    for i, combo in enumerate(combos, start=1):
        print('{:3}: {}'.format(i, fmt_combo(combo)))


# --------------------------------------------------
def fmt_combo(combo):
    """English version of combo"""

    coins = list(
        filter(lambda t: t[0],
               zip(combo, ('quarter', 'dime', 'nickel', 'penny'))))

    def fmt(val, coin):
        plural = 'pennies' if coin == 'penny' else coin + 's'
        return '{} {}'.format(val, coin if val == 1 else plural)

    return join(list(starmap(fmt, coins)))


# --------------------------------------------------
def join(items):
    """Join items with commas, 'and'"""

    n = len(items)
    return '' if n == 0 else items[0] if n == 1 else ' and '.join(
        items) if n == 2 else ', '.join(items[:-1] + ['and ' + items[-1]])


# --------------------------------------------------
def figure(value, coins):
    """
    Find possible combo of 'coins' for 'value'
    Returns a tuple of ints for (quarters, dimes, nickels, pennies) or ()
    """

    q, d, n = coins
    big_coins = sum([5 * n, 10 * d, 25 * q])
    return (q, d, n, value - big_coins) if big_coins <= value else ()


# --------------------------------------------------
if __name__ == '__main__':
    main()
