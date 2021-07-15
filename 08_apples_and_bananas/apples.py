#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-15
Purpose: Rock the Casbah
"""

import argparse


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-a',
                        '--arg',
                        default='',
                        type=str,
                        help='A named string argument',
                        metavar='str',


    parser.add_argument('-i',
                        '--int',
                        default=0,
                        type=int,
                        help='A named integer argument',
                        metavar='int')


    parser.add_argument('-f',
                        '--file',
                        default=None,
                        type=argparse.FileType('rt'),
                        help='A readable file',
                        metavar='FILE')


    parser.add_argument('-o',
                        '--on',
                        action='store_true',
                        help='A boolean flag')


    parser.add_argument('positional',
                        nargs='+',
                        help='A positional argument',
                        metavar='str')


    return parser.parse_args()


def main():
    """Main program"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')


if __name__ == '__main__':
    main()
