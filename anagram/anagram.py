#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-19
Purpose: Find anagrams
"""

import argparse
import logging
import os
import re
import sys
from collections import defaultdict, Counter
from itertools import combinations, permutations, product, chain
from dire import warn, die


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

    parser.add_argument('-n',
                        '--num_combos',
                        help='Number of words combination to test',
                        metavar='int',
                        type=int,
                        default=1)

    parser.add_argument('-d', '--debug', help='Debug', action='store_true')

    return parser.parse_args()


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

    words = defaultdict(set)
    for line in open(word_list):
        for word in line.split():
            clean = re.sub('[^a-z0-9]', '', word.lower())
            if len(clean) == 1 and clean not in 'ai':
                continue
            words[len(clean)].add(clean)

    text_len = len(text)
    counts = Counter(text)
    anagrams = set()
    lengths = list(words.keys())
    for i in range(1, args.num_combos + 1):
        key_combos = list(
            filter(
                lambda t: sum(t) == text_len,
                set(
                    map(lambda t: tuple(sorted(t)),
                        combinations(chain(lengths, lengths), i)))))

        for keys in key_combos:
            logging.debug('Searching keys {}'.format(keys))
            word_combos = list(product(*list(map(lambda k: words[k], keys))))

            for t in word_combos:
                if Counter(''.join(t)) == counts:
                    for p in filter(
                            lambda x: x != text,
                            map(lambda x: ' '.join(x), permutations(t))):
                        anagrams.add(p)

            logging.debug('# anagrams = {}'.format(len(anagrams)))

    logging.debug('Finished searching')

    if anagrams:
        print('{} = '.format(text))
        for i, t in enumerate(sorted(anagrams), 1):
            print('{:4}. {}'.format(i, t))
    else:
        print('No anagrams for "{}".'.format(text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
