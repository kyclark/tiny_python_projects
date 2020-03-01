#!/usr/bin/env python3
"""Choices"""

import argparse


# --------------------------------------------------
def get_args():
    """get args"""

    parser = argparse.ArgumentParser(
        description='Choices',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('color',
                        metavar='color',
                        help='Color',
                        choices=['red', 'yellow', 'blue'])

    parser.add_argument('size',
                        metavar='size',
                        type=int,
                        choices=range(1, 11),
                        help='The size of the garment')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""

    args = get_args()
    print('color =', args.color)
    print('size =', args.size)


# --------------------------------------------------
if __name__ == '__main__':
    main()
