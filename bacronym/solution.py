#!/usr/bin/env python3
"""Explain acronyms"""

import argparse
import random
import re
from collections import defaultdict
from functools import partial


# --------------------------------------------------
def get_args():
    """get arguments"""

    parser = argparse.ArgumentParser(
        description="Explain acronyms",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("acronym", help="Acronym", type=str, metavar="STR")

    parser.add_argument("-n",
                        "--num",
                        help="Maximum number of definitions",
                        type=int,
                        metavar="NUM",
                        default=5)

    parser.add_argument("-w",
                        "--wordlist",
                        help="Dictionary/word file",
                        type=argparse.FileType("r"),
                        metavar="STR",
                        default="/usr/share/dict/words")

    parser.add_argument("-x",
                        "--exclude",
                        help="List of words to exclude",
                        type=str,
                        metavar="STR",
                        nargs="+",
                        default="a an the".split())

    parser.add_argument("-s",
                        "--seed",
                        help="Random seed",
                        type=int,
                        metavar="INT",
                        default=None)

    args = parser.parse_args()

    if args.num < 1:
        parser.error('--num "{}" must be > 0'.format(args.num))

    if not re.search(r"^[A-Z]{2,}$", args.acronym.upper()):
        msg = 'Acronym "{}" must be >1 in length, only use letters'.format(
            args.acronym)
        parser.error(msg)

    return args


# --------------------------------------------------
def group_words(file, stop_words=()):
    """Groups words in file by first letter"""

    good = partial(re.search, r'^[a-z]{2,}$')
    seen = set()
    words_by_letter = defaultdict(list)
    clean = lambda word: re.sub('[^a-z]', '', word)

    for word in filter(good, map(clean, file.read().lower().split())):
        if word not in seen and word not in stop_words:
            seen.add(word)
            words_by_letter[word[0]].append(word)

    return words_by_letter


# --------------------------------------------------
def make_definitions(acronym, words_by_letter, limit=1):
    """Find definitions an acronym given groupings of words by letters"""

    definitions = []
    for _ in range(limit):
        definition = []
        for letter in acronym.lower():
            opts = words_by_letter.get(letter.lower(), [])
            definition.append(random.choice(opts).title() if opts else "?")
        definitions.append(" ".join(definition))

    return definitions


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    acronym = args.acronym
    stop = set(map(str.lower, args.exclude))
    random.seed(args.seed)

    words_by_letter = group_words(args.wordlist, stop)
    definitions = make_definitions(acronym, words_by_letter, args.num)

    if definitions:
        print(acronym.upper() + " =")
        for definition in definitions:
            print(" - " + definition)
    else:
        print("Sorry I could not find any good definitions")


# --------------------------------------------------
if __name__ == "__main__":
    main()
