#!/usr/bin/env python3
"""
Author : petra <petra@localhost>
Date   : 2021-01-26
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    print('Ahoy, Captain, a ' + word + ' off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
