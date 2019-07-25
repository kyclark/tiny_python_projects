#!/usr/bin/env python3
"""tests for boggle.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput

prg = './boggle.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_runs1():
    """runs"""

    rv, out = getstatusoutput('{} -s 1'.format(prg))
    assert rv == 0
    lines = out.splitlines()
    assert len(lines) == 1014
    table = '\n'.join(['B  A  N  H', 'S  E  N  L', 'O  Y  O  N', 'H  L  E  M'])
    assert '\n'.join(map(str.strip, lines[:4])) == table
    assert lines[-1] == 'Total points = 2208'


# --------------------------------------------------
def test_runs2():
    """runs"""

    outfile = random_string()

    if os.path.isfile(outfile):
        os.remove(outfile)

    try:
        rv, out = getstatusoutput('{} -s 1 -o {}'.format(prg, outfile))
        assert rv == 0

        expected = '\n'.join([
            'B  A  N  H', 'S  E  N  L', 'O  Y  O  N', 'H  L  E  M',
            'Total points = 2208'
        ])

        assert '\n'.join(map(str.strip, out.splitlines())) == expected
        assert os.path.isfile(outfile)
        words = open(outfile).read().splitlines()
        assert len(words) == 1009

    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)


# --------------------------------------------------
def test_runs3():
    """runs"""

    outfile = random_string()

    if os.path.isfile(outfile):
        os.remove(outfile)

    try:
        rv, out = getstatusoutput('{} -s 2 -o {}'.format(prg, outfile))
        assert rv == 0

        expected = '\n'.join([
            'O  F  N  H', 'O  L  L  V', 'I  S  O  E', 'R  R  I  QU',
            'Total points = 1889'
        ])

        assert '\n'.join(map(str.strip, out.splitlines())) == expected
        assert os.path.isfile(outfile)
        words = open(outfile).read().splitlines()
        assert len(words) == 748

    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)
