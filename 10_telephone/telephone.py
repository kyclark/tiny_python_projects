#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-23
Purpose: Tiny Python Projcts telephone exercise
"""

import argparse
from asyncio.subprocess import STDOUT
from asyncore import write
import os
from pydoc import text
import random
import string
import sys


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-s',
                        '--seed',
                        default=None,
                        type=int,
                        help='Random seed',
                        metavar='seed')


    parser.add_argument('-m',
                        '--mutations',
                        default=0.1,
                        type=float,
                        help='Percent mutations',
                        metavar='mutations')


    parser.add_argument('-o',
                        '--output',
                        default=sys.stdout,
                        type=argparse.FileType('wt'),
                        help='Output file',
                        metavar='FILE')


    # parser.add_argument('-o',
    #                     '--on',
    #                     action='store_true',
    #                     help='A boolean flag')


    parser.add_argument('text',
                        help='Input text or file',
                        metavar='text')


    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    if args.mutations < 0.0 or args.mutations > 1.0:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


def main():
    """Main program"""

    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    args = get_args()
    random.seed(args.seed)
    text = args.text
    num_mutations = round(len(text) * args.mutations)
    args.output.write(f'You said: "{text}"\n')
    text = list(text)
    for index in random.sample(range(len(text)), num_mutations):
        text[index] = random.choice(alpha.replace(text[index], ''))
    text = ''.join(text)
    args.output.write(f'I heard : "{text}"\n')
    args.output.close()

if __name__ == '__main__':
    main()
