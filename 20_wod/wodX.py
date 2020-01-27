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
    exercises = read_csv(args.file)

    wod = starmap(mk_exercise, random.sample(exercises, k=args.num_exercises))
    print(tabulate(wod, headers=('Exercise', 'Reps')))


# --------------------------------------------------
def parse_row(row):
    """Parse a row"""

    name = row.get('exercise')
    reps = row.get('reps')

    if name and '-' in reps:
        low, high = row['reps'].split('-')

        if low.isdigit() and high.isdigit():
            return (name, int(low), int(high))

    return None


# --------------------------------------------------
def test_parse_row():
    """Test parse_row"""

    assert parse_row({}) is None
    assert parse_row({'exercise': 'foo', 'reps': '10'}) is None
    assert parse_row({'exercise': 'foo', 'reps': '10.5-11'}) is None
    assert parse_row({'exercise': 'bar', 'reps': '10-20'}) == ('bar', 10, 20)


# --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""

    return list(map(parse_row, csv.DictReader(fh, delimiter=',')))


# --------------------------------------------------
def make_exercise(name, low, high, easy):
    """Make an exercise"""

    if easy:
        low, high = int(low / 2), int(high / 2)

    return (name, random.randint(low, high))


# --------------------------------------------------
def test_read_csv():
    """Test read_csv"""

    text1 = io.StringIO('exercise,reps\nfoo,10-20\nbar,30-40')
    assert read_csv(text1) == [('foo', 10, 20), ('bar', 30, 40)]

    text2 = io.StringIO('exercise,reps\nfoo,10.5-20\nbar,30')
    assert read_csv(text) == [('foo', 10, 20), ('bar', 30, 40)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
