#!/usr/bin/env python3
"""
Tut author: Ken Youens-Clark
Author: Petra Power
Purpose: Say hello
"""

import argparse


# ----------------- Ken likes to put lines to visually identify individual functions
def get_args():
    """
    Get command line arguments
    """
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """
    Pylint will require docstring at top of function to document what it does
    """
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
