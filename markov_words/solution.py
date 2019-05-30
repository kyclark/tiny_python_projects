#!/usr/bin/env python3

import argparse
import logging
import os
import random
import re
import sys
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Markov chain for characters/words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        help='Training file(s)')

    parser.add_argument('-n',
                        '--num_words',
                        help='Number of words to generate',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-k',
                        '--kmer_size',
                        help='Kmer size',
                        metavar='int',
                        type=int,
                        default=2)

    parser.add_argument('-m',
                        '--max_word',
                        help='Max word length',
                        metavar='int',
                        type=int,
                        default=12)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-d',
                        '--debug',
                        help='Debug to ".log"',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    k = args.kmer_size
    random.seed(args.seed)

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    # debate use of set/list in terms of letter frequencies
    chains = defaultdict(list)
    for file in args.file:
        for line in open(file):
            for word in line.lower().split():
                word = re.sub('[^a-z]', '', word)
                for i in range(0, len(word) - k):
                    kmer = word[i:i + k + 1]
                    chains[kmer[:-1]].append(kmer[-1])

    logging.debug(chains)

    kmers = list(chains.keys())
    starts = set()

    for i in range(1, args.num_words + 1):
        word = ''
        while not word:
            kmer = random.choice(kmers)
            if not kmer in starts and chains[kmer] and re.search(
                    '[aeiou]', kmer):
                starts.add(kmer)
                word = kmer

        length = random.choice(range(k + 2, args.max_word))
        logging.debug('Make a word {} long starting with "{}"'.format(
            length, word))
        while len(word) < length:
            if not chains[kmer]: break
            char = random.choice(list(chains[kmer]))
            logging.debug('char = "{}"'.format(char))
            word += char
            kmer = kmer[1:] + char

        logging.debug('word = "{}"'.format(word))
        print('{:3}: {}'.format(i, word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
