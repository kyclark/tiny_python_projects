#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-07-12
Purpose: Rock the Casbah
"""

import argparse
import os
import random
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--actors',
                        help='Number of actors',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-u',
                        '--units',
                        help='Number of units',
                        metavar='int',
                        type=int,
                        default=500)

    parser.add_argument('-r',
                        '--rounds',
                        help='Number of rounds',
                        metavar='int',
                        type=int,
                        default=100)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    actors = list(range(1, args.actors + 1))
    units = args.units
    rounds = args.rounds
    units_per_actor = int(units / len(actors))
    dist = {actor: units_per_actor for actor in actors}

    for i in range(rounds):
        random.shuffle(actors)
        for i in range(0, len(actors), 2):
            a1, a2 = actors[i], actors[i+1]
            if dist[a1] and dist[a2]:
                res = random.choice([0,1])
                dist[a1] += 1 if res else -1
                dist[a2] += 1 if res else -1

    for units, actor in sorted([(v,k) for k,v in dist.items()]):
        print('{:3}: {:3} {}'.format(actor, units, '#' * units))

# --------------------------------------------------
if __name__ == '__main__':
    main()
