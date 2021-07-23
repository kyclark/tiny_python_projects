#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-21
Purpose: Tiny Python Programs generate abuse exercise
"""

import argparse
import random


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Heap abuse",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )


    parser.add_argument(
        "-a",
        "--adjectives",
        default=2,
        type=int,
        help="Number of adjectives",
        metavar="adjectives",
    )

    parser.add_argument(
        "-n",
        "--number",
        default=3,
        type=int,
        help="Number of insults",
        metavar="insults",
    )

    parser.add_argument(
        "-s", "--seed", default=None, type=int, help="Random seed", metavar="seed"
    )

    parser.add_argument('-f',
                        '--adjective_file',
                        default=None,
                        type=argparse.FileType('rt'),
                        help='Text file containing adjectives',
                        required=True,
                        metavar='FILE')

    parser.add_argument('-g',
                        '--noun_file',
                        default=None,
                        type=argparse.FileType('rt'),
                        help='Text file containing nouns',
                        required=True,
                        metavar='FILE')


    args = parser.parse_args()

    if args.adjectives <= 0:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number <= 0:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


def main():
    """Main program"""

    # adjectives = """
    # bankrupt base caterwauling corrupt cullionly detestable dishonest false filthsome filthy foolish 
    # foul gross heedless indistinguishable infected insatiate irksome lascivious lecherous loathsome 
    # lubbery old peevish rascaly rotten ruinous scurilous scurvy slanderous sodden-witted thin-faced 
    # toad-spotted unmannered vile wall-eyed
    # """.split()
    # assert len(adjectives) == 36
    # nouns = """
    # Judas Satan ape ass barbermonger beggar block boy braggart butt carbuncle coward coxcomb cur dandy 
    # degenerate fiend fishmonger fool gull harpy jack jolthead knave liar lunatic maw milksop minion 
    # ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    # """.split()
    # assert len(nouns) == 39

    args = get_args()
    random.seed(args.seed)
    adjectives = []
    for line in  args.adjective_file:
        adjectives.append(line.rstrip())
    nouns = []
    for line in args.noun_file:
        nouns.append(line.rstrip())

    for _ in range(args.number):
        print(f"You ", end="")
        print(", ".join(random.sample(adjectives, args.adjectives)), end="")
        print(f" {random.choice(nouns)}!")


if __name__ == "__main__":
    main()
