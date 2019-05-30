#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-08
Purpose: Create Workout Of (the) Day (WOD)
"""

import argparse
import csv
import os
import random
import sys
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-f',
        '--file',
        help='CSV input file of exercises',
        metavar='str',
        type=str,
        default='wod.csv')

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

    parser.add_argument(
        '-n',
        '--num_exercises',
        help='Number of exercises',
        metavar='int',
        type=int,
        default=4)

    parser.add_argument(
        '-e', '--easy', help='Make it easy', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def read_csv(file):
    """Read the CSV input"""

    if not os.path.isfile(file):
        die('"{}" is not a file'.format(file))

    exercises = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        required = ['exercise', 'reps']

        if not all(map(lambda f: f in reader.fieldnames, required)):
            die('"{}" is missing required fields: {}'.format(
                file, ', '.join(required)))

        for row in reader:
            name = row['exercise']
            low, high = row['reps'].split('-')
            exercises.append((name, int(low), int(high)))

    return exercises


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file)
    table = []

    for name, low, high in random.sample(exercises, k=args.num_exercises):
        if args.easy:
            low = int(low / 2)
            high = int(high / 2)

        table.append((name, '{}'.format(random.randint(low, high))))

    print(tabulate(table, headers=('Exercise', 'Reps')))


# --------------------------------------------------
if __name__ == '__main__':
    main()
