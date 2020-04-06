#!/usr/bin/env python3

import csv
from pprint import pprint

with open('inputs/exercises.csv') as fh:
    reader = csv.DictReader(fh, delimiter=',')
    exercises = []
    for rec in reader:
        name, reps = rec['name'], rec['reps']
        low, high = 0, 0 # what goes here?
        exercises.append((name, low, high))
