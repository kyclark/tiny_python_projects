#!/usr/bin/env python3
"""
Author : matt <matt@localhost>
Date   : 2021-05-18
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        nargs='+',
                        type=str,
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='sort the items',
                        action='store_true')

    return parser.parse_args()


def create_picnic_list(items):
    i = len(items)
    if i == 1:
        result = 'You are bringing ' + items[0] + '.'
        
    elif i == 2:
        result = 'You are bringing ' + items[0] + ' and ' + items[1] + '.'     
    else:
        last_item = items.pop()
        all_items = (', '.join(items))
        result = ('You are bringing ' + all_items + ', and ' + last_item + '.')
    
    return result


# --------------------------------------------------
def main():
    """add items to picnic list"""

    args = get_args()
    #flag_arg = args.on
    pos_arg = args.positional

    picnic_items = create_picnic_list(pos_arg)
    print(picnic_items)


# --------------------------------------------------
if __name__ == '__main__':
    main()
