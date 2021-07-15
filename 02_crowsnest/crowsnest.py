#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-09
Purpose: Tiny Python Problems Crows Nest Exercise
"""

import argparse

def initial_alpha(word):
    if word[0].isalpha():
        return word
    else:
        raise argparse.ArgumentTypeError('must start with alpha character')

def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Crows Nest Report',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', '--side', metavar='side', default='larboard', help='Side of sighting')
    parser.add_argument('sighting', type=initial_alpha, help='The sighting, must start with alpha character')

    return parser.parse_args()


def main():
    """Print crows nest report"""

    args = get_args()
    side = args.side
    word = args.sighting
    test_character = word[0]
    if test_character.islower():
        article = 'an' if test_character in 'aeiou' else 'a'
    else:
        article = 'An' if test_character in 'AEIOU' else 'A'
    print(f'Ahoy, Captain, {article} {word} off the {side} bow!')


if __name__ == '__main__':
    main()
