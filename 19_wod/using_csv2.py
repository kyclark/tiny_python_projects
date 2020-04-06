#!/usr/bin/env python3

import csv
from pprint import pprint

with open('inputs/exercises.csv') as fh:
    reader = csv.DictReader(fh, delimiter=',')
    records = list(reader)
    pprint(records)
