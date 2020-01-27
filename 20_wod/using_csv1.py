#!/usr/bin/env python3

import csv
from pprint import pprint

with open('exercises.csv') as fh:
    reader = csv.DictReader(fh, delimiter=',')
    records = []
    for rec in reader:
        records.append(rec)

    pprint(records)
