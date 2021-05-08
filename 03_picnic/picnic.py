#!/usr/bin/env python3
"""Picnic game"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # nargs+ forces at least on argument
    parser.add_argument('item',
                        nargs='+',
                        help='Item(s) to bring')

    # dashes make the argument optional
    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    parser.add_argument('-no',
                        '--nooxford',
                        default=False,
                        action='store_true',
                        help='Turn off oxford commas')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    num = len(items)

    if args.sorted:
        items.sort()

    bringing = ''
    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = ' and '.join(items)
    else:
        if args.nooxford:
            join = ' and '
        else:
            join = ', and '
        items[-1] = join + items[-1]
        bringing = ', '.join(items[:-1]) + items[-1]
    print('You are bringing {}.'.format(bringing))


# --------------------------------------------------
if __name__ == '__main__':
    main()
