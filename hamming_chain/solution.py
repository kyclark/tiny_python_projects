#!/usr/bin/env python3
"""Hamming chain"""

import argparse
import logging
import random
import re
from dire import die


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Hamming chain',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s', '--start', type=str, help='Starting word', default='')

    parser.add_argument('-w',
                        '--wordlist',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='File input',
                        default='/usr/share/dict/words')

    parser.add_argument('-d',
                        '--max_distance',
                        metavar='int',
                        type=int,
                        help='Maximum Hamming distance',
                        default=1)

    parser.add_argument('-i',
                        '--iterations',
                        metavar='int',
                        type=int,
                        help='Random seed',
                        default=20)

    parser.add_argument('-S',
                        '--seed',
                        metavar='int',
                        type=int,
                        help='Random seed',
                        default=None)

    parser.add_argument('-D', '--debug', help='Debug', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def dist(s1, s2):
    """Given two strings, return the Hamming distance (int)"""

    return abs(len(s1) - len(s2)) + sum(
        map(lambda p: 0 if p[0] == p[1] else 1, zip(s1.lower(), s2.lower())))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    start = args.start
    fh = args.wordlist
    distance = args.max_distance

    random.seed(args.seed)

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    logging.debug('file = %s', fh.name)

    words = fh.read().splitlines()

    if not start:
        start = random.choice(words)

    if not start in words:
        die('Unknown word "{}"'.format(start))

    def find_close(word):
        l = len(word)
        low, high = l - distance, l + distance
        test = filter(lambda w: low <= len(w) <= high, words)
        return filter(lambda w: dist(word, w) <= distance, test)

    print('{} ->'.format(start))
    prev = [start]
    for i in range(1, args.iterations + 1):
        close = list(filter(lambda w: w not in prev, find_close(prev[-1])))
        if not close:
            die('Failed to find more words!')

        next_word = random.choice(close)
        print('{:3}: {}'.format(i, next_word))
        prev.append(next_word)


# --------------------------------------------------
if __name__ == '__main__':
    main()
