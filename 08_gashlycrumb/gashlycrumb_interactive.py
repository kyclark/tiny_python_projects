#!/usr/bin/env python3
"""Interactive Gashlycrumb"""

import argparse


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='str',
                        type=argparse.FileType('r'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    lookup = {line[0]: line.rstrip() for line in args.file}

    while True:
        letter = input('Please provide a letter [! to quit]: ')

        if letter == '!':
            print('Bye')
            break
        elif letter.upper() in lookup:
            print(lookup[letter.upper()])
        else:
            print('I do not know "{}".'.format(letter))


# --------------------------------------------------
if __name__ == '__main__':
    main()
