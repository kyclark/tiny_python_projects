#!/usr/bin/env python3
"""One positional argument"""

import argparse


# --------------------------------------------------
def get_args():
    """get args"""

    parser = argparse.ArgumentParser(
        description='One positional argument',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('name', metavar='str', help='A name')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""

    args = get_args()
    print(f'Hello, {args.name}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
