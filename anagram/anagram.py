#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-19
Purpose: Find anagrams
"""

import argparse
import logging
import os
import re
import sys
from collections import Counter
from itertools import combinations


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find anagrams',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text')

    parser.add_argument('-w',
                        '--wordlist',
                        help='Wordlist',
                        metavar='str',
                        type=str,
                        default='/usr/share/dict/words')

    parser.add_argument(
        '-n',
        '--num_combos',
        help='Number of words combination to test',
        metavar='int',
        type=int,
        default=1)

    parser.add_argument(
        '-d', '--debug', help='Debug', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    text = args.text
    word_list = args.wordlist

    if not os.path.isfile(word_list):
        die('--wordlist "{}" is not a file'.format(word_list))

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    words = set()
    for line in open(word_list):
        for word in line.split():
            words.add(re.sub('[^a-z0-9]', '', word.lower()))

    # p = filter(lambda w: w != text and Counter(w) == counts, words)

    text_len = len(text)
    counts = Counter(text)
    anagrams = []
    for i in range(1, args.num_combos + 1):
        for t in map(lambda x: ' '.join(x), combinations(words, i)):
            logging.debug(t)
            if t != text and Counter(t.replace(' ', '')) == counts:
                anagrams.append(t)

    if anagrams:
        print('{} = {}'.format(text, ', '.join(anagrams)))
    else:
        print('No anagrams for "{}".'.format(text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
