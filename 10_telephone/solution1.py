#!/usr/bin/env python3
"""Telephone"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    random.seed(args.seed)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    len_text = len(text)
    num_mutations = round(args.mutations * len_text)
    new_text = text

    for i in random.sample(range(len_text), num_mutations):
        new_char = random.choice(alpha.replace(new_text[i], ''))
        new_text = new_text[:i] + new_char + new_text[i + 1:]

    print(f'You said: "{text}"\nI heard : "{new_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
