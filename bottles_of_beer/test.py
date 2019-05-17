#!/usr/bin/env python3
"""tests for bottles.py"""

import re
import random
import hashlib
from subprocess import getstatusoutput, getoutput

prg = './bottles.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_one():
    expected = ('1 bottle of beer on the wall,\n'
                '1 bottle of beer,\n'
                'Take one down, pass it around,\n'
                '0 bottles of beer on the wall!')

    rv, out = getstatusoutput('{} -n 1'.format(prg))
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_two():
    expected = ('2 bottles of beer on the wall,\n'
                '2 bottles of beer,\n'
                'Take one down, pass it around,\n'
                '1 bottle of beer on the wall!\n\n'
                '1 bottle of beer on the wall,\n'
                '1 bottle of beer,\n'
                'Take one down, pass it around,\n'
                '0 bottles of beer on the wall!')

    rv, out = getstatusoutput('{} -n 2'.format(prg))
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_random():
    sums = dict(
        map(lambda x: x.split('\t'),
            open('sums.txt').read().splitlines()))

    for n in random.choices(list(sums.keys()), k=10):
        flag = '-n' if random.choice([0, 1]) == 1 else '--num_bottles'
        rv, out = getstatusoutput('{} {} {}'.format(prg, flag, n))
        out += '\n'  # because the last newline is removed
        assert rv == 0
        assert hashlib.md5(out.encode('utf-8')).hexdigest() == sums[n]
