#!/usr/bin/env python3
"""Shakespearean insult generator"""

import sys
import random

adjectives = """
scurvy old filthy scurilous lascivious foolish rascaly gross rotten
corrupt foul loathsome irksome heedless unmannered whoreson cullionly
false filthsome toad-spotted caterwauling wall-eyed insatiate vile
peevish infected sodden-witted lecherous ruinous indistinguishable
dishonest thin-faced slanderous bankrupt base detestable rotten
dishonest lubbery
""".strip().split()

nouns = """
knave coward liar swine villain beggar slave scold jolthead whore
barbermonger fishmonger carbuncle fiend traitor block ape braggart
jack milksop boy harpy recreant degenerate Judas butt cur Satan ass
coxcomb dandy gull minion ratcatcher maw fool rogue lunatic varlet
worm
""".strip().split()


def main():
    """main"""
    args = sys.argv[1:]
    num = int(args[0]) if len(args) > 0 and args[0].isdigit() else 5

    for _ in range(num):
        adjs = [random.choice(adjectives) for _ in range(3)]
        noun = random.choice(nouns)
        print('You {} {}!'.format(', '.join(adjs), noun))


if __name__ == '__main__':
    main()
