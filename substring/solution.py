#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-08
Purpose: Find words sharing a substring
"""

import argparse
import os
import random
import re
import sys
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find words sharing a substring',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-f',
        '--file',
        metavar='str',
        help='Input file',
        type=str,
        default='/usr/share/dict/words')

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

    parser.add_argument(
        '-m',
        '--min_words',
        help='Minimum number of words for a given kmer',
        metavar='int',
        type=int,
        default=3)

    parser.add_argument(
        '-k', '--ksize', help='Size of k', metavar='int', type=int, default=4)

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
def get_words(file):
    """Get words from input file"""

    if not os.path.isfile(file):
        die('"{}" is not a file')

    words = set()
    for line in open(file):
        for word in line.split():
            words.add(re.sub('[^a-zA-Z0-9]', '', word.lower()))

    if not words:
        die('No usable words in "{}"'.format(file))

    return words


# --------------------------------------------------
def get_kmers(words, k, min_words):
    """ Find all words sharing kmers"""

    if k <= 1:
        die('-k "{}" must be greater than 1'.format(k))

    shared = defaultdict(list)
    for word in words:
        for kmer in [word[i:i + k] for i in range(len(word) - k + 1)]:
            shared[kmer].append(word)

    # Select kmers having enough words (can't use `pop`!)

    # Method 1: for loop
    ok = dict()
    for kmer in shared:
        if len(shared[kmer]) >= min_words:
            ok[kmer] = shared[kmer]

    # Method 2: list comprehension
    # ok = dict([(kmer, shared[kmer]) for kmer in shared
    #            if len(shared[kmer]) >= min_words])

    # Method 3: map/filter
    # ok = dict(
    #     map(lambda kmer: (kmer, shared[kmer]),
    #         filter(lambda kmer: len(shared[kmer]) >= min_words,
    #                shared.keys())))

    return ok


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    random.seed(args.seed)

    shared = get_kmers(get_words(args.file), args.ksize, args.min_words)

    # Choose a kmer, setup game state
    kmer = random.choice(list(shared.keys()))
    guessed = set()
    found = []
    prompt = 'Name a word that contains "{}" [!=quit, ?=hint] '.format(kmer)
    compliments = ['Nice', 'Rock on', 'Totes', 'Fantastic', 'Excellent']
    taunts = [
        'Surely you jest!', 'Are you kidding me?',
        'You must have rocks for brains.', 'What is wrong with you?'
    ]

    #print(kmer, shared[kmer])

    while True:
        num_left = len(shared[kmer])
        if num_left == 0:
            print('No more words!')
            break

        guess = input(prompt + '({} left) '.format(num_left)).lower()

        if guess == '?':
            # Provide a hint
            pos = random.choice(range(len(shared[kmer])))
            word = shared[kmer].pop(pos)
            print('For instance, "{}"...'.format(word))

        elif guess == '!':
            # Bail
            print('Quitter!')
            break

        elif guess in guessed:
            # Chastise
            print('You have already guessed "{}"'.format(guess))

        elif guess in shared[kmer]:
            # Remove the word, feedback with compliment
            pos = shared[kmer].index(guess)
            word = shared[kmer].pop(pos)
            print('{}! "{}" is found!'.format(
                random.choice(compliments), word))
            found.append(word)
            guessed.add(guess)

        else:
            # Taunt
            print(random.choice(taunts))

    # Game over, man!
    if found:
        n = len(found)
        print('Hey, you found {} word{}! Not bad.'.format(
            n, '' if n == 1 else 's'))
    else:
        print('Wow, you found no words. You suck!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
