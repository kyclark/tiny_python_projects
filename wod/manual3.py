#!/usr/bin/env python3

from pprint import pprint

with open('exercises.csv') as fh:
    headers = fh.readline().rstrip().split(',')
    records = list(
        map(lambda line: dict(zip(headers,
                                  line.rstrip().split(','))), fh))
    pprint(records)
