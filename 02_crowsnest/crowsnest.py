#!/usr/bin/env python3

import argparse


def get_args():
    """Get the comand-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word',
                        default='octopus', help='Name of thing seen')

    return parser.parse_args()


def main():
    """Sentence Constructor"""
    thing_seen = get_args().word
    if start_vowel(thing_seen):
        article = 'An' if thing_seen[0].isupper() else 'an'
    else:
        article = 'A' if thing_seen[0].isupper() else 'a'

    print(f'Ahoy, Captain, {article} {thing_seen} off the larboard bow!')


def start_vowel(word):
    """Checks if word starts with a vowel. Returns True if so"""
    return word[0].lower() in ['a', 'e', 'i', 'o', 'u']


if __name__ == "__main__":
    main()
