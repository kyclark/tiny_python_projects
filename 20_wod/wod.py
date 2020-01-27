#!/usr/bin/env python3
"""Create Workout Of (the) Day (WOD)"""

import argparse
import csv
import io
import re
import random
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
                        '--num',
                        help='Number of exercises',
                        metavar='int',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()

    if args.num < 1:
        parser.error('--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file)

    if exercises:
        for name, low, high in random.sample(exercises, k=args.num):
            reps = random.randint(low, high)
            if args.easy:
                reps = int(reps / 2)
            wod.append((name, reps))

        print(tabulate(wod, headers=('Exercise', 'Reps')))
    else:
        print(f'No usable data in --file "{args.file.name}"')


# --------------------------------------------------
def read_csv(fh):
    """Read the CSV input"""

    exercises = []
    for row in csv.DictReader(fh, delimiter=','):
        name, reps = row.get('exercise'), row.get('reps')
        if name and reps:
            match = re.match(r'(\d+)-(\d+)', reps)
            if match:
                low, high = map(int, match.groups())
                exercises.append((name, low, high))

    return exercises


# --------------------------------------------------
if __name__ == '__main__':
    main()
