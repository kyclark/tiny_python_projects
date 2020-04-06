#!/usr/bin/env python3

from pprint import pprint

with open('inputs/exercises.csv') as fh:
    headers = fh.readline().rstrip().split(',')
    records = []
    for line in fh:
        rec = dict(zip(headers, line.rstrip().split(',')))
        records.append(rec)

    pprint(records)
