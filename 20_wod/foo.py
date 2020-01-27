#!/usr/bin/env python3
"""Create Workout Of (the) Day (WOD)"""

import argparse
import csv
import io
import os
import random
from itertools import starmap
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='str',
                        type=argparse.FileType('r'),
                        default='exercises.csv')

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
    wod = []

    for name, low, high in read_csv(args.file):
        reps = random.randint(low, high)
        if args.easy:
            reps = int(reps / 2)
        wod.append((name, reps))

    wod = random.sample(wod, k=args.num_exercises)
    print(tabulate(wod, headers=('Exercise', 'Reps')))


# --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""

    exercises = []
    for row in csv.DictReader(fh, delimiter=','):
        low, high = row['reps'].split('-')
        if low.isdigit() and high.isdigit():
            exercises.append((row['exercise'], int(low), int(high)))

    return exercises


# --------------------------------------------------
def test_read_csv():
    """Test read_csv"""

    text = io.StringIO('exercise,reps\nfoo,10-20\nbar,30-40')
    assert read_csv(text) == [('foo', 10, 20), ('bar', 30, 40)]


# --------------------------------------------------
def make_exercise(name, low, high, easy):
    """Make an exercise"""

    if easy:
        low, high = int(low / 2), int(high / 2)

    return (name, random.randint(low, high))


# --------------------------------------------------
def test_make_exercise():
    """Test make_exercise"""

    random.seed(1)
    assert make_exercise('foo', 10, 20, False) == ('foo', 12)
    assert make_exercise('bar', 5, 30, True) == ('bar', 11)
    assert make_exercise('baz', 0, 50, False) == ('baz', 48)
    assert make_exercise('quux', 0, 50, True) == ('quux', 2)
    random.seed(None)


# --------------------------------------------------
if __name__ == '__main__':
    main()
