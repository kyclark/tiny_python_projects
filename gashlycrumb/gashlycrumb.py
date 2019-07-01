#!/usr/bin/env python3
"""Lookup tables"""

import argparse


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter', help='Letter', metavar='str', type=str)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='str',
                        type=argparse.FileType('r'),
                        default='gashlycrumb.txt')

    args = parser.parse_args()

    if len(args.letter) != 1:
        parser.error('"{}" is not 1 character.'.format(args.letter))

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    letter = args.letter.upper()

    # lookup = {}
    # for line in args.file:
    #     lookup[line[0]] = line.rstrip()

    lookup = {line[0]: line.rstrip() for line in args.file}

    if letter in lookup:
        print(lookup[letter])
    else:
        print('I do not know "{}".'.format(letter))


# --------------------------------------------------
if __name__ == '__main__':
    main()
