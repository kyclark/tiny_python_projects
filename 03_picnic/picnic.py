#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
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
    str_arg = args.item

    if args.sorted:
        str_arg.sort()


    text = ''

    if len(str_arg) == 1:
        text = str_arg[0]
    elif len(str_arg) == 2:
        text =' and '.join(str_arg)
    else:
        str_arg[-1] = 'and '+ str_arg[-1]
        text = ', '.join(str_arg)
        
 

    print(f'You are bringing {text}.')
    #print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
