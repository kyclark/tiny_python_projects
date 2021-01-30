#!/usr/bin/env python3
"""
Author : petra
Date   : 2021-01-26
Purpose: Crow's Nest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    char = word[0]
    article = ''

    if char.islower():
        article = 'an' if word[0] in 'aeiou' else 'a'
    else:
        article = 'An' if word[0] in 'AEIOU' else 'A'

    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
