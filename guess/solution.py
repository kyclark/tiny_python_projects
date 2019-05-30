#!/usr/bin/env python3

import argparse
import random
import re
import sys
from dire import die


# --------------------------------------------------
def get_args():
    """get args"""
    parser = argparse.ArgumentParser(
        description='Guessing game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-m',
                        '--min',
                        help='Minimum value',
                        metavar='int',
                        type=int,
                        default=1)

    parser.add_argument('-x',
                        '--max',
                        help='Maximum value',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-g',
                        '--guesses',
                        help='Number of guesses',
                        metavar='int',
                        type=int,
                        default=5)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs',
                        metavar='str',
                        type=str,
                        nargs='+',
                        default=[])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    low = args.min
    high = args.max
    guesses_allowed = args.guesses
    inputs = args.inputs
    random.seed(args.seed)

    if low < 1:
        die('--min "{}" cannot be lower than 1'.format(low))

    if guesses_allowed < 1:
        die('--guesses "{}" cannot be lower than 1'.format(guesses_allowed))

    if low > high:
        die('--min "{}" is higher than --max "{}"'.format(low, high))

    secret = random.randint(low, high)
    prompt = 'Guess a number between {} and {} (q to quit): '.format(low, high)
    num_guesses = 0

    while True:
        guess = inputs.pop(0) if inputs else input(prompt)
        num_guesses += 1

        if re.match('q(uit)?', guess.lower()):
            print('Now you will never know the answer.')
            sys.exit()

        # Method 1: test if the guess is a digit
        if not guess.isdigit():
            print('"{}" is not a number.'.format(guess))
            continue
        num = int(guess)

        # Method 2: try/except
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
            print('"{}" is too {}.'.format(num,
                                           'low' if num < secret else 'high'))

        if num_guesses >= guesses_allowed:
            print(
                'Too many guesses, loser! The number was "{}."'.format(secret))
            sys.exit(1)


# --------------------------------------------------
if __name__ == '__main__':
    main()
