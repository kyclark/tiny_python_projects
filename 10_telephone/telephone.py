#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-23
Purpose: Tiny Python Projcts telephone exercise
"""

import argparse
import os
import random
import string
import sys
import re


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Telephone with mutations, insertions and deletions",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-s", "--seed", default=None, type=int, help="Random seed", metavar="seed"
    )

    parser.add_argument(
        "-m",
        "--mutations",
        default=0.1,
        type=float,
        help="Percent mutations",
        metavar="mutations",
    )

    parser.add_argument(
        "-i",
        "--insertions",
        default=0.0,
        type=float,
        help="Percent insertions",
        metavar="insertions",
    )

    parser.add_argument(
        "-d",
        "--deletions",
        default=0.0,
        type=float,
        help="Percent deletions",
        metavar="deletions",
    )

    parser.add_argument(
        "-w",
        "--words",
        default=1.0,
        type=float,
        help="Percent words",
        metavar="words",
    )

    parser.add_argument(
        "-c",
        "--characters",
        action="store_true",
        help="Substitute only characters (no punctuation)",
    )

    parser.add_argument(
        "-o",
        "--output",
        default=sys.stdout,
        type=argparse.FileType("wt"),
        help="Output file",
        metavar="FILE",
    )

    parser.add_argument("text", help="Input text or file", metavar="text")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    if args.mutations < 0.0 or args.mutations > 1.0:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if args.insertions < 0.0 or args.insertions > 1.0:
        parser.error(f'--insertions "{args.insertions}" must be between 0 and 1')

    if args.deletions < 0.0 or args.deletions > 1.0:
        parser.error(f'--deletions "{args.deletions}" must be between 0 and 1')

    if args.words < 0.0 or args.words > 1.0:
        parser.error(f'--words "{args.words}" must be between 0 and 1')

    return args


def main():
    """Main program"""

    args = get_args()

    alpha = string.ascii_letters
    if not args.characters:
        alpha += string.punctuation
    alpha = "".join(sorted(alpha))
    
    random.seed(args.seed)

    text = args.text
    args.output.write(f'You said: "{text}"\nI heard : "')
    re_S = re.compile(r'(\S+)')
    words = re_S.split(text)
    num_words_to_modify = round(len(words) * args.words)
    word_indexes = random.sample(range(len(words)), num_words_to_modify)
    text = []
    
    for word_index, word in enumerate(words):
        if word_index in word_indexes: 
            num_mutations = round(len(word) * args.mutations)
            num_insertions = round(len(word) * args.insertions)
            num_deletions = round(len(word) * args.deletions)

            # mutations
            word = list(word)
            for index in random.sample(range(len(word)), num_mutations):
                word[index] = random.choice(alpha.replace(word[index], ""))

            # insertions
            insertion_indexes = random.sample(range(len(word) + 1), num_insertions)
            new_length = len(word) + num_insertions
            word_copy = word.copy()
            word = []
            # can insert before first element (index == 0) or after last element (index == len(word) + 1)
            for index in range(new_length):
                if index in insertion_indexes:
                    word.append(random.choice(alpha))
                if len(word_copy) > 0:
                    word.append(word_copy.pop(0))

            # deletions
            for index in random.sample(range(len(word)), num_deletions):
                word[index] = ""
            word = "".join(word)
        
        text.append(word)
    
    args.output.write(f'{"".join(text)}"\n')
    args.output.close()


if __name__ == "__main__":
    main()
