#!/usr/bin/env python3
"""Rock, Paper, Scissors"""

import argparse
import os
import random
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock, Paper, Scissors',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def insult():
    adjective = """
    truculent fatuous vainglorious fatuous petulant moribund jejune
    feckless antiquated rambunctious mundane misshapen glib dreary
    dopey devoid deleterious degrading clammy brazen indiscreet
    indecorous imbecilic dysfunctional dubious drunken disreputable
    dismal dim deficient deceitful damned daft contrary churlish
    catty banal asinine infantile lurid morbid repugnant unkempt
    vapid decrepit malevolent impertinent decrepit grotesque puerile
    """.split()

    noun = """
    abydocomist bedswerver bespawler bobolyne cumberworld dalcop
    dew-beater dorbel drate-poke driggle-draggle fopdoodle fustylugs
    fustilarian gillie-wet-foot gnashgab gobermouch
    gowpenful-o’-anything klazomaniac leasing-monger loiter-sack
    lubberwort muck-spout mumblecrust quisby raggabrash rakefire
    roiderbanks saddle-goose scobberlotcher skelpie-limmer
    smell-feast smellfungus snoutband sorner stampcrab stymphalist
    tallowcatch triptaker wandought whiffle-whaffle yaldson zoilist
    """.split()

    return ' '.join([random.choice(adjective), random.choice(noun)])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    valid = set('rps')
    beats = {'r': 's', 's': 'p', 'p': 'r'}
    display = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

    while True:
        play = input('1-2-3-Go! [rps|q] ').lower()

        if play.startswith('q'):
            print('Bye, you {}!'.format(insult()))
            sys.exit(0)

        if play not in valid:
            print('You {}! Please choose from: {}.'.format(
                insult(), ', '.join(sorted(valid))))
            continue

        computer = random.choice(list(valid))

        print('You: {}\nMe : {}'.format(display[play], display[computer]))

        if beats[play] == computer:
            print('You win. You are a {}.'.format(insult()))
        elif beats[computer] == play:
            print('You lose, {}!'.format(insult()))
        else:
            print('Draw, you {}.'.format(insult()))


# --------------------------------------------------
if __name__ == '__main__':
    main()
