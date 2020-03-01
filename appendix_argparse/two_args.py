#!/usr/bin/env python3
"""Two positional arguments"""

import argparse


# --------------------------------------------------
def get_args():
    """get args"""

    parser = argparse.ArgumentParser(
        description='Two positional arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('color',
                        metavar='color',
                        type=str,
                        help='The color of the garment')

    parser.add_argument('size',
                        metavar='size',
                        type=int,
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
