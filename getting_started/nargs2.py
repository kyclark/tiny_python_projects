#!/usr/bin/env python3
"""nargs=2"""

import argparse


# --------------------------------------------------
def get_args():
    """get args"""

    parser = argparse.ArgumentParser(
        description='nargs=2',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        metavar='INT',
                        nargs=2,
                        type=int,
                        help='Two numbers')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""

    args = get_args()
    n1, n2 = args.numbers
    print('n1 =', n1)
    print('n2 =', n2)


# --------------------------------------------------
if __name__ == '__main__':
    main()
