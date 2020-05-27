#!/usr/bin/env python3
"""nargs=+"""

import argparse


# --------------------------------------------------
def get_args():
    """get args"""

    parser = argparse.ArgumentParser(
        description='nargs=+',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        metavar='int',
                        nargs='+',
                        type=int,
                        help='Numbers')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""

    args = get_args()
    numbers = args.numbers

    print('{} = {}'.format(' + '.join(map(str, numbers)), sum(numbers)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
