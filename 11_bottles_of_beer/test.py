#!/usr/bin/env python3
"""tests for bottles.py"""

import os
import re
import random
import hashlib
from subprocess import getstatusoutput

prg = './bottles.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_int():
    """Bad integer value"""

    rv, out = getstatusoutput(f'{prg} -n -1')
    assert rv != 0
    assert re.search(r'--num \(-1\) must > 0', out)


# --------------------------------------------------
def test_float():
    """float value"""

    rv, out = getstatusoutput(f'{prg} --num 2.1')
    assert rv != 0
    assert re.search(r"invalid int value: '2.1'", out)


# --------------------------------------------------
def test_str():
    """str value"""

    rv, out = getstatusoutput(f'{prg} -n lsdfkl')
    assert rv != 0
    assert re.search(r"invalid int value: 'lsdfkl'", out)


# --------------------------------------------------
def test_one():
    """One bottle of beer"""

    expected = ('1 bottle of beer on the wall,\n'
                '1 bottle of beer,\n'
                'Take one down, pass it around,\n'
                'No more bottles of beer on the wall!')

    rv, out = getstatusoutput(f'{prg} --num 1')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_two():
    """Two bottles of beer"""

    expected = ('2 bottles of beer on the wall,\n'
                '2 bottles of beer,\n'
                'Take one down, pass it around,\n'
                '1 bottle of beer on the wall!\n\n'
                '1 bottle of beer on the wall,\n'
                '1 bottle of beer,\n'
                'Take one down, pass it around,\n'
                'No more bottles of beer on the wall!')

    rv, out = getstatusoutput(f'{prg} -n 2')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_random():
    """Random number"""

    sums = dict(
        map(lambda x: x.split('\t'),
            open('sums.txt').read().splitlines()))

    for n in random.choices(list(sums.keys()), k=10):
        flag = '-n' if random.choice([0, 1]) == 1 else '--num'
        rv, out = getstatusoutput(f'{prg} {flag} {n}')
        out += '\n'  # because the last newline is removed
        assert rv == 0
        assert hashlib.md5(out.encode('utf-8')).hexdigest() == sums[n]
