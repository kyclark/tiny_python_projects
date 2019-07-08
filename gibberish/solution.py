#!/usr/bin/env python3
"""Markov chain word generator"""

import argparse
import io
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
def kmers(text, k=1):
    return [text[i:i + k] for i in range(len(text) - k + 1)]
    """Return k-mers from text"""



# --------------------------------------------------
def test_kmers():
    """Test kmers"""

    assert kmers('abcd') == list('abcd')
    assert kmers('abcd', 2) == ['ab', 'bc', 'cd']
    assert kmers('abcd', 3) == ['abc', 'bcd']
    assert kmers('abcd', 4) == ['abcd']
    assert kmers('abcd', 5) == []


# --------------------------------------------------
def read_training(fhs, k=1):
    """Read training files, return chains"""

    chains = defaultdict(list)
    clean = lambda word: re.sub('[^a-z]', '', word.lower())

    for fh in fhs:
        for word in map(clean, fh.read().split()):
            for kmer in kmers(word, k + 1):
                chains[kmer[:-1]].append(kmer[-1])

    return chains


# --------------------------------------------------
def test_read_training():
    """Test read_training"""

    text = 'The quick brown fox jumps over the lazy dog.'

    expected3 = {
        'qui': ['c'],
        'uic': ['k'],
        'bro': ['w'],
        'row': ['n'],
        'jum': ['p'],
        'ump': ['s'],
        'ove': ['r'],
        'laz': ['y']
    }
    assert read_training([io.StringIO(text)], k=3) == expected3

    expected4 = {'quic': ['k'], 'brow': ['n'], 'jump': ['s']}
    assert read_training([io.StringIO(text)], k=4) == expected4


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

    chains = read_training(args.file, args.kmer_size)
    logging.debug(chains)

    kmers = list(chains.keys())
    for i in range(args.num_words):
        word = random.choice(kmers)
        length = random.choice(range(k + 2, args.max_word))
        logging.debug('Length "{}" starting with "{}"'.format(length, word))

        while len(word) < length:
            kmer = word[-1 * k:]
            if not chains[kmer]:
                break

            char = random.choice(list(chains[kmer]))
            logging.debug('char = "{}"'.format(char))
            word += char

        logging.debug('word = "{}"'.format(word))
        print('{:3}: {}'.format(i+1, word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
