#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-23
Purpose: Markov Chain
"""

import argparse
import logging
import os
import random
import string
import sys
from pprint import pprint as pp
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Markov Chain',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('training',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Training file(s)')

    parser.add_argument('-l',
                        '--length',
                        help='Output length (characters)',
                        metavar='int',
                        type=int,
                        default=500)

    parser.add_argument('-n',
                        '--num_words',
                        help='Number of words',
                        metavar='int',
                        type=int,
                        default=2)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-w',
                        '--text_width',
                        help='Max number of characters per line',
                        metavar='int',
                        type=int,
                        default=70)

    parser.add_argument('-d',
                        '--debug',
                        help='Debug to ".log"',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_words = args.num_words
    char_max = args.length
    text_width = args.text_width

    random.seed(args.seed)

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    all_words = defaultdict(list)
    for fh in args.training:
        words = fh.read().split()

        for i in range(0, len(words) - num_words):
            l = words[i:i + num_words + 1]
            all_words[tuple(l[:-1])].append(l[-1])

    logging.debug('all words = {}'.format(all_words))

    prev = ''
    while not prev:
        start = random.choice(
            list(
                filter(lambda w: w[0][0] in string.ascii_uppercase,
                       all_words.keys())))
        if all_words[start]:
            prev = start

    logging.debug('Starting with "{}"'.format(prev))

    p = ' '.join(prev)
    char_count = len(p)
    print(p, end=' ')
    line_width = char_count

    while True:
        if not prev in all_words: break

        new_word = random.choice(all_words[prev])
        new_len = len(new_word) + 1
        logging.debug('chose = "{}" from {}'.format(new_word, all_words[prev]))

        if line_width + new_len >= text_width:
            print()
            line_width = new_len
        else:
            line_width += new_len

        char_count += new_len

        print(new_word, end=' ')
        prev = prev[1:] + (new_word, )

        if char_count >= char_max and prev[-1][-1] in '.!?': break

    logging.debug('Finished')
    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
