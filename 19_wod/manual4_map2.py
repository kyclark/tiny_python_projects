#!/usr/bin/env python3

from pprint import pprint

with open('inputs/exercises.csv') as fh:
    headers = fh.readline().rstrip().split(',')
    mk_rec = lambda line: dict(zip(headers, line.rstrip().split(',')))
    records = map(mk_rec, fh)
    pprint(list(records))
