#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-12-21
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
from turtle import turtle


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='str',
                        type=str,
                        default='plot.png')

    parser.add_argument('-n',
                        '--num',
                        help='Number of days',
                        metavar='int',
                        type=int,
                        default=12)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    turtle.forward(10)
    turtle.done()

    # turtle.color('red', 'yellow')
    # begin_fill()
    # while True:
    #     forward(200)
    #     left(170)
    #     if abs(pos()) < 1:
    #         break
    # end_fill()
    # done()



# --------------------------------------------------
if __name__ == '__main__':
    main()
