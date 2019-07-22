#!/usr/bin/env python3
"""Evolution"""

import argparse
import logging
import os
import random
import re
import string
import sys
import numpy as np
from itertools import combinations


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('positional',
    #                     metavar='str',
    #                     help='A positional argument')

    parser.add_argument('-i',
                        '--iterations',
                        help='Number of iterations',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument(
        '-S',
        '--select',
        help='Select by',
        metavar='str',
        type=str,
        choices=['random', 'short', 'long', 'vowels', 'consonants'],
        default='random')

    parser.add_argument('-t',
                        '--target',
                        help='Target number of words',
                        metavar='int',
                        type=int,
                        default=100)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-w',
                        '--wordlist',
                        help='Wordlist file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='/usr/share/dict/words')

    parser.add_argument('-d', '--debug', help='Log debug', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    random.seed(args.seed)
    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    cons = '[' + ''.join(re.findall('[^aeiou]', string.ascii_lowercase)) + ']'
    cons_re = re.compile(cons, re.I)
    vowels_re = re.compile('[aeiou]', re.I)
    vowel_count = lambda word: len(vowels_re.findall(word))
    cons_count = lambda word: len(cons_re.findall(word))

    def selector(pair):
        if args.select == 'random':
            return random.choice(pair)
        if args.select == 'short':
            return pair[np.argmin(list(map(len, pair)))]
        if args.select == 'long':
            return pair[np.argmax(list(map(len, pair)))]
        if args.select == 'vowels':
            return pair[np.argmax(list(map(vowel_count, pair)))]
        if args.select == 'consonants':
            return pair[np.argmax(list(map(cons_count, pair)))]

    words = args.wordlist.read().split()
    lens = []
    num_vowels = []
    num_cons = []

    for i in range(args.iterations):
        print(f'Iteration {i+1}')
        words = sim(words, selector, args.target)
        lens.append(np.mean(list(map(len, words))))
        num_vowels.append(np.mean(list(map(vowel_count, words))))
        num_cons.append(np.mean(list(map(cons_count, words))))

    print('Selection  = {}'.format(args.select))
    print('Avg len    = {}'.format(int(np.mean(lens))))
    print('Vowels     = {}'.format(int(np.mean(num_vowels))))
    print('Consonants = {}'.format(int(np.mean(num_cons))))


# --------------------------------------------------
def sim(words, selector, target):
    """Run a simulation"""

    rounds = 0
    while True:
        if len(words) <= target:
            break

        random.shuffle(words)
        rounds += 1
        logging.debug(f'ROUND {rounds}: words = {len(words)}')
        winners = []
        for i in range(0, len(words) - 1, 2):
            pair = words[i], words[i + 1]
            winner = selector(pair)
            winners.append(winner)
            logging.debug(f'pair = {pair}, winner = {winner}')
            #winners.append((word1, word2)[vowel_winner])
            #winners.append((word1, word2)[consonant_winner])
            #break

        words = winners

    logging.debug('words =\n%s', '\n'.join(words))
    return words


# --------------------------------------------------
if __name__ == '__main__':
    main()
