#!/usr/bin/env python3

from pprint import pprint

with open('inputs/exercises.csv') as fh:
    headers = fh.readline().rstrip().split(',')
    records = [dict(zip(headers, line.rstrip().split(','))) for line in fh]
    pprint(records)
