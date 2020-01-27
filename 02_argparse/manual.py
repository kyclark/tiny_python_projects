#!/usr/bin/env python3
"""Manually check an argument"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Manually check an argument',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-v',
                        '--val',
                        help='Integer value between 1 and 10',
                        metavar='int',
                        type=int,
                        default=5)

    args = parser.parse_args()  # <1>
    if not 1 <= args.val <= 10: # <2>
        parser.error(f'--val "{args.val}" must be between 1 and 10') # <3>

    return args # <4>


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(f'val = "{args.val}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
