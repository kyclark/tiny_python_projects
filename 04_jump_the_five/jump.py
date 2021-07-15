#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-11
Purpose: Tiny Python Projects jump the five encoding exercise
"""

import argparse
from cgitb import lookup


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the five encoding',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s', '--substitutestring',
                        action='store_true',
                        help='Substitute characters for numerals')


    parser.add_argument('text',
                        metavar='str',
                        help='String to be encoded')

    return parser.parse_args()


def main():
    """Main program"""

    jumper = {'1':'9', '2':'8', '3':'7', '4':'6', '5':'0', '6':'4', '7':'3', '8':'2', '9':'1', '0':'5'}
    jumper_string= {'1':'one ', '2':'two ', '3':'three ', '4':'four ', '5':'five ',
                    '6':'six ', '7':'seven ', '8':'eight ', '9':'nine ', '0':'zero ',
                    '-':'- '}
    args = get_args()
    if not args.substitutestring:
        print(args.text.translate(str.maketrans(jumper)))
    else:
        print(args.text.translate(str.maketrans(jumper_string)))

if __name__ == '__main__':
    main()
