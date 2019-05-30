#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-09
Purpose: Diplay delimited text files as ASCII tables
"""

import argparse
import csv
import os
import sys
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Diplay delimited text files as ASCII tables',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file',
        metavar='FILE',
        nargs='+',
        type=argparse.FileType('r', encoding='UTF-8'),
        help='Input file(s)')

    parser.add_argument(
        '-d',
        '--delimiter',
        help='Delimiter',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-s',
        '--style',
        help='Tabulate table style',
        metavar='str',
        type=str,
        choices=[
            'plain', 'simple', 'github', 'grid', 'fancy_grid', 'pipe',
            'orgtbl', 'jira', 'presto', 'psql', 'rst', 'mediawiki', 'moinmoin',
            'youtrack', 'html', 'latex', 'latex_raw', 'latex_booktabs',
            'textile'
        ],
        default='psql')

    parser.add_argument(
        '-l',
        '--limit',
        help='Limit display to number records',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-n', '--no_headers', help='No headers in file', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    file_hdr = '/ ' + ('*' * 10) + ' {} ' + ('*' * 10) + ' /'

    for fh in args.file:
        if len(args.file) > 1:
            print(file_hdr.format(os.path.basename(fh.name)))

        _, ext = os.path.splitext(fh.name)
        delimiter = args.delimiter if args.delimiter else ',' \
            if ext == '.csv' else '\t'
        data = list(csv.reader(fh, delimiter=delimiter))

        if not data:
            warn('No data in "{}"'.format(fh.name))
            continue

        headers = []
        if args.no_headers:
            num_fields = len(data[0])
            headers = map(lambda i: 'Field {}'.format(i + 1),
                          range(num_fields))
        else:
            headers = data.pop(0)

        if args.limit:
            data = data[:args.limit]

        print(tabulate(data, headers=headers, tablefmt=args.style))


# --------------------------------------------------
if __name__ == '__main__':
    main()
