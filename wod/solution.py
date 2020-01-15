#!/usr/bin/env python3
"""Create Workout Of (the) Day (WOD)"""

import argparse
import csv
import io
import random
from itertools import starmap
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='str',
                        type=argparse.FileType('r'),
                        default='wod.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num_exercises',
                        help='Number of exercises',
                        metavar='int',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Make it easy',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file)

    def mk_exercise(name, low, high):
        if args.easy:
            low, high = int(low / 2), int(high / 2)
        return (name, random.randint(low, high))

    wod = starmap(mk_exercise, random.sample(exercises, k=args.num_exercises))
    print(tabulate(wod, headers=('Exercise', 'Reps')))


# --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""
    exercises = []

    for row in csv.DictReader(fh, delimiter=','):
        name = row['exercise']
        low, high = row['reps'].split('-')
        exercises.append((name, int(low), int(high)))

    return exercises


# --------------------------------------------------
def test_read_csv():
    """Test read_csv"""

    text = io.StringIO('exercise,reps\nfoo,10-20\nbar,30-40')
    assert read_csv(text) == [('foo', 10, 20), ('bar', 30, 40)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
