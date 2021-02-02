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
    bringing = ''

    if args.sorted:
        items.sort()

    if len(items) == 1:
        bringing = items[0]
    elif len(items) == 2:
        bringing = ' and '.join(items)
    else:
        bringing = ', '.join(items[:len(items)-1]) + ', and ' + items[-1]

    print(f'You are bringing {bringing}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
