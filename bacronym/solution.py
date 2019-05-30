#!/usr/bin/env python3
"""Make guesses about acronyms"""

import argparse
import sys
import os
import random
import re
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Explain acronyms',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('acronym', help='Acronym', type=str, metavar='STR')

    parser.add_argument('-n',
                        '--num',
                        help='Maximum number of definitions',
                        type=int,
                        metavar='NUM',
                        default=5)

    parser.add_argument('-w',
                        '--wordlist',
                        help='Dictionary/word file',
                        type=str,
                        metavar='STR',
                        default='/usr/share/dict/words')

    parser.add_argument('-x',
                        '--exclude',
                        help='List of words to exclude',
                        type=str,
                        metavar='STR',
                        default='a,an,the')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        type=int,
                        metavar='INT',
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""

    args = get_args()
    acronym = args.acronym
    wordlist = args.wordlist
    limit = args.num
    goodword = r'^[a-z]{2,}$'
    badwords = set(re.split(r'\s*,\s*', args.exclude.lower()))

    random.seed(args.seed)

    if not re.match(goodword, acronym.lower()):
        print('"{}" must be >1 in length, only use letters'.format(acronym))
        sys.exit(1)

    if not os.path.isfile(wordlist):
        print('"{}" is not a file.'.format(wordlist))
        sys.exit(1)

    seen = set()
    words_by_letter = defaultdict(list)
    for word in open(wordlist).read().lower().split():
        clean = re.sub('[^a-z]', '', word)
        if not clean:  # nothing left?
            continue

        if re.match(goodword,
                    clean) and clean not in seen and clean not in badwords:
            seen.add(clean)
            words_by_letter[clean[0]].append(clean)

    len_acronym = len(acronym)
    definitions = []
    for i in range(0, limit):
        definition = []
        for letter in acronym.lower():
            possible = words_by_letter.get(letter, [])
            if len(possible) > 0:
                definition.append(
                    random.choice(possible).title() if possible else '?')

        if len(definition) == len_acronym:
            definitions.append(' '.join(definition))

    if len(definitions) > 0:
        print(acronym.upper() + ' =')
        for definition in definitions:
            print(' - ' + definition)
    else:
        print('Sorry I could not find any good definitions')


# --------------------------------------------------
if __name__ == '__main__':
    main()
