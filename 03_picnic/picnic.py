#!/usr/bin/env python3
"""
Author : petra <petra@localhost>
Date   : 2021-01-30
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        nargs='+',           # one or more expected
                        type=str,
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')    # if option is used by user, set to True, default is False

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.str
    sort = args.sorted
    comma_space = ', '

    if sort:
        items.sort()

    if len(items) == 1:
        print(f'You are bringing {items[0]}.')
    elif len(items) == 2:
        print(f'You are bringing {items[0]} and {items[1]}.')
    else:
        print(f'You are bringing {comma_space.join(items[:len(items)-1])}, and {items[len(items)-1]}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
