#!/usr/bin/env python3
"""Markov chain word generator"""

import argparse
import io
import logging
import random
import re
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Markov chain word generator',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
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
def get_kmers(text, k=1):
    """Return k-mers from text"""

    return [text[i:i + k] for i in range(len(text) - k + 1)]


# --------------------------------------------------
def read_training(fhs, k=1):
    """Read training files, return chains"""

    chains = defaultdict(list)
    clean = lambda w: re.sub('[^a-z]', '', w.lower())

    for fh in fhs:
        for word in map(clean, fh.read().split()):
            for kmer in get_kmers(word, k + 1):
                chains[kmer[:-1]].append(kmer[-1])

    return chains


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

    chains = read_training(args.file, k)
    logging.debug(chains)

    kmers = list(chains.keys())
    for i in range(args.num_words):
        word = random.choice(kmers)
        length = random.choice(range(k + 2, args.max_word))
        logging.debug('Length "%s" starting with "%s"', length, word)

        while len(word) < length:
            kmer = word[-1 * k:]
            if not chains[kmer]:
                break

            char = random.choice(list(chains[kmer]))
            logging.debug('char = "%s"', char)
            word += char

        logging.debug('word = "%s"', word)
        print('{:3}: {}'.format(i + 1, word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
