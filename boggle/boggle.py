#!/usr/bin/env python3
"""Boggle"""

import argparse
import os
import random
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Boggle',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('positional',
    #                     metavar='str',
    #                     help='A positional argument')

    # parser.add_argument('-a',
    #                     '--arg',
    #                     help='A named string argument',
    #                     metavar='str',
    #                     type=str,
    #                     default='')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    # parser.add_argument('-f',
    #                     '--file',
    #                     help='A readable file',
    #                     metavar='FILE',
    #                     type=argparse.FileType('r'),
    #                     default=None)

    # parser.add_argument('-o',
    #                     '--on',
    #                     help='A boolean flag',
    #                     action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    dice = ['U Qu H M N I',
            'O B J A O B',
            'F F S K A P',
            'N S I E U E',
            'E G H W E N',
            'S O A C H P',
            'T T R E Y L',
            'R N Z N H L',
            'R E V L Y D',
            'T U I C M O',
            'T D T Y S I',
            'O O W T T A',
            'N A E A E G',
            'R V T H E W',
            'L X E D R I',
            'O T S E S I']

    show = list(map(lambda s: random.choice(s.split()), dice))

    print(len(show))


# --------------------------------------------------
if __name__ == '__main__':
    main()
