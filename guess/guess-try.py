#!/usr/bin/env python3
"""
Author:  Ken Youens-Clark <kyclark@gmail.com>
Purpose: Guess-the-number game
"""

import argparse
import random
import re
import sys


# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Guessing game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-m',
        '--min',
        help='Minimum value',
        metavar='int',
        type=int,
        default=1)

    parser.add_argument(
        '-x',
        '--max',
        help='Maximum value',
        metavar='int',
        type=int,
        default=50)

    parser.add_argument(
        '-g',
        '--guesses',
        help='Number of guesses',
        metavar='int',
        type=int,
        default=5)

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
    """main"""
    args = get_args()
    low = args.min
    high = args.max
    guesses_allowed = args.guesses
    secret = random.randint(low, high)

    if low < 1:
        die('--min "{}" cannot be lower than 1'.format(low))

    if guesses_allowed < 1:
        die('--guesses "{}" cannot be lower than 1'.format(high))

    if low > high:
        die('--min "{}" is higher than --max "{}"'.format(low, high))

    prompt = 'Guess a number between {} and {} (q to quit): '.format(low, high)
    num_guesses = 0

    while True:
        guess = input(prompt)
        num_guesses += 1

        if re.match('q(uit)?', guess.lower()):
            die('Now you will never know the answer.')

        num = 0
        try:
            num = int(guess)
        except:
            warn('"{}" is not an integer'.format(guess))
            continue

        if not low <= num <= high:
            print('Number "{}" is not in the allowed range'.format(num))
        elif num == secret:
            print('"{}" is correct. You win!'.format(num))
            break
        else:
            print('"{}" is too {}.'.format(num, 'low'
                                           if num < secret else 'high'))

        if num_guesses >= guesses_allowed:
            die('Too many guesses, loser! The number was "{}."'.format(secret))


# --------------------------------------------------
if __name__ == '__main__':
    main()
