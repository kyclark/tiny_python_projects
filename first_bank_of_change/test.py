#!/usr/bin/env python3
"""tests for fboc.py"""

import os
import re
import random
from subprocess import getstatusoutput, getoutput

prg = './fboc.py'


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
def test_runs01():
    out = getoutput('{} 1'.format(prg))
    out_ok(out, 1, 2, ['1 penny'])


# --------------------------------------------------
def test_runs02():
    out = getoutput('{} 5'.format(prg))
    out_ok(out, 5, 3, ['5 pennies', '1 nickel'])


# --------------------------------------------------
def test_runs03():
    out = getoutput('{} 26'.format(prg))
    wanted = [
        '26 pennies',
        '1 quarter, 1 penny',
        '1 dime, 16 pennies',
        '2 dimes, 6 pennies',
        '1 nickel, 21 pennies',
        '1 dime, 1 nickel, 11 pennies',
        '2 dimes, 1 nickel, 1 penny',
        '2 nickels, 16 pennies',
        '1 dime, 2 nickels, 6 pennies',
        '3 nickels, 11 pennies',
        '1 dime, 3 nickels, 1 penny',
        '4 nickels, 6 pennies',
        '5 nickels, 1 penny',
    ]

    out_ok(out, 26, 14, wanted)


# --------------------------------------------------
def out_ok(out, value, num_lines, lines):
    """Parse the output, test for header, num_lines, values"""

    out_lines = out.splitlines()
    assert len(out_lines) == num_lines

    hdr = 'If you give me {} cent{}, I can give you:'.format(
        value, '' if value == 1 else 's')
    assert out_lines[0] == hdr

    for expected in lines:
        assert any(map(lambda l: re.search(expected, l), out_lines))
