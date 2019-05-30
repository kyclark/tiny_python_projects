#!/usr/bin/env python3

import argparse
import random
import sys

adjectives = """
bankrupt base caterwauling corrupt cullionly detestable dishonest
false filthsome filthy foolish foul gross heedless indistinguishable
infected insatiate irksome lascivious lecherous loathsome lubbery old
peevish rascaly rotten ruinous scurilous scurvy slanderous
sodden-witted thin-faced toad-spotted unmannered vile wall-eyed
""".strip().split()

nouns = """
Judas Satan ape ass barbermonger beggar block boy braggart butt
carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
gull harpy jack jolthead knave liar lunatic maw milksop minion
ratcatcher recreant rogue scold slave swine traitor varlet villain worm
""".strip().split()


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='int',
                        type=int,
                        default=2)

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='int',
                        type=int,
                        default=3)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    num_adj = args.adjectives
    num_insults = args.number

    random.seed(args.seed)

    for _ in range(num_insults):
        adjs = random.sample(adjectives, k=num_adj)
        noun = random.choice(nouns)
        print('You {} {}!'.format(', '.join(adjs), noun))


# --------------------------------------------------
if __name__ == '__main__':
    main()
