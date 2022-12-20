#!/usr/bin/env python3
"""
Author : haemin <haemin@localhost>
Date   : 2022-12-06
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+', # 이를 통해 하나 이상의 위치 인수(문자열)를 받을 수 있다.
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    num = len(items)
    
    if args.sorted:
        items.sort()
        
    bringing = ''
    if num == 1:
        bringing = items[0]
    elif num == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' +items[-1]
        bringing = ', '.join(items)
    
    print('You are bringing {}.'.format(bringing))
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
