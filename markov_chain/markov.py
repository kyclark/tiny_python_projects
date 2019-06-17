#!/usr/bin/env python3
"""Markov Chain"""

import argparse
import logging
import random
import textwrap
from pprint import pformat as pf
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
    char_max = args.length
    random.seed(args.seed)
    num_words = args.num_words

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    training = read_training(args.training, num_words)
    logging.debug('training = %s', pf(training))

    # Find a word starting with a capital letter
    words = list(
        random.choice(
            list(filter(lambda t: t[0][0].isupper(), training.keys()))))

    logging.debug('starting with "%s"', words)
    logging.debug(training[tuple(words)])

    while True:
        # get last two words
        prev = tuple(words[-1 * num_words:])

        # bail if dead end
        if not prev in training:
            break

        new_word = random.choice(training[prev])
        logging.debug('chose "{}" from {}'.format(new_word, training[prev]))
        words.append(new_word)

        # try to find ending punctuation if we've hit wanted char count
        char_count = sum(map(len, words)) + len(words)
        if char_count >= char_max and new_word[-1] in '.!?':
            break

    print('\n'.join(textwrap.wrap(' '.join(words), width=args.text_width)))
    logging.debug('Finished')


# --------------------------------------------------
def read_training(fhs, num_words):
    """Read training files, return dict of chains"""

    all_words = defaultdict(list)
    for fh in fhs:
        words = fh.read().split()

        for i in range(0, len(words) - num_words):
            l = words[i:i + num_words + 1]
            all_words[tuple(l[:-1])].append(l[-1])

    return all_words


# --------------------------------------------------
if __name__ == '__main__':
    main()
