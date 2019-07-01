#!/usr/bin/env python3
"""Spoonerisms"""

import argparse
import os
import re
import string
import textwrap


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Introduce Spoonerisms',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-w',
                        '--width',
                        help='Output text width',
                        metavar='int',
                        type=int,
                        default=70)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    words = text.split()
    pairs = []

    for k in range(len(words) - 1):
        pairs.append((words[k], words[k+1]))

    vowels = 'aeiouAEIOU'
    consonants = ''.join([c for c in string.ascii_letters if c not in vowels])
    regex = re.compile('^([' + consonants + ']+)([' + vowels + '].*)')
    stop = set('before behind between beyond but by concerning'
               'despite down during following for from into like near'
               'plus since that the through throughout to towards'
               'which with within without'.split())
    skip = set()

    for i, pair in enumerate(pairs):
        w1, w2 = pair
        if set([w1.lower(), w2.lower()]).intersection(stop):
            continue

        i1, i2 = i, i + 1
        if i1 in skip or i2 in skip:
            continue

        m1 = regex.search(w1)
        m2 = regex.search(w2)
        if m1 and m2:
            prefix1, suffix1 = m1.groups()
            prefix2, suffix2 = m2.groups()
            words[i1] = prefix2 + suffix1
            words[i2] = prefix1 + suffix2
            skip.add(i1)
            skip.add(i2)

    print('\n'.join(textwrap.wrap(' '.join(words), width=args.width)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
