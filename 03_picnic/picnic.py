#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-10
Purpose: Tiny Python Projects Picnic Example
"""

import argparse


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='List items for picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s', '--sorted',
                        action='store_true',
                        help='Sort the items')
    
    parser.add_argument('-o', '--omitoxfordcomma',
                        action='store_true',
                        help="Don't print Oxford comma")
    
    parser.add_argument('-l', '--listseparator',
                        help="Specify list separator, default is comma",
                        metavar='char',
                        type=str,
                        default=',')

    parser.add_argument('items',
                        nargs='+',
                        metavar='item',
                        help='An item for the picnic')

    return parser.parse_args()

def main():
    """Print the list"""

    args = get_args()
    items = args.items
    if args.sorted:
        items.sort()
    print(f'You are bringing ', end='')
    num_items = len(items)
    for index in range(num_items):
        print (items[index], end='')
        if index <  num_items - 2:
            print(f'{args.listseparator} ', end='')
        if index == num_items - 2:
            if num_items == 2:
                print(' and ', end='')
            else:
                if (args.omitoxfordcomma):
                    print(' and ', end='')
                else: 
                    print(f'{args.listseparator} and ', end='') 
    print('.')

if __name__ == '__main__':
    main()
