#!/usr/bin/env python3
"""Rummikub"""

import argparse
import os
import sys
import random
from itertools import product


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rummikub',
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
def make_tiles():
    """Make tiles"""

    return list(product(list('BYRK'), range(1, 14))) * 2

# --------------------------------------------------
def test_make_tiles():
    """Test make_tiles"""

    tiles = make_tiles()
    assert len(tiles) == 104
    assert len(list(filter(lambda tile: tile[0] == 'R', tiles))) == 26
    assert len(list(filter(lambda tile: tile[1] == 1, tiles))) == 8


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    tiles = random.sample(make_tiles(), k=14)
    print(tiles)


# --------------------------------------------------
if __name__ == '__main__':
    main()
