#!/usr/bin/env python3
"""
Author : matt <matt@localhost>
Date   : 2021-05-17
Purpose: Choose the article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='The thing we see')

    return parser.parse_args()


def print_object(object_seen):
    """Print object seen
       First check for vowel or consonant
    """
    vowels = ('a', 'e', 'i', 'o', 'u')

    if object_seen[0].lower() in vowels:
        print("Ahoy, Captain, an " + object_seen + " off the larboard bow!")
    else:
        print("Ahoy, Captain, a " + object_seen + " off the larboard bow!")


# --------------------------------------------------
def main():
    """Print the object seen"""

    args = get_args()
    word = args.word
    print_object(word)


# --------------------------------------------------
if __name__ == '__main__':
    main()
