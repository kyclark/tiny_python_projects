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
    out_ok(out, 1, ['1 penny'])


# --------------------------------------------------
def test_runs02():
    out = getoutput('{} 6'.format(prg))
    out_ok(out, 6, ['6 pennies', '1 nickel and 1 penny'])


# --------------------------------------------------
def test_runs03():
    out = getoutput('{} 26'.format(prg))
    wanted = [
        '26 pennies',
        '1 quarter and 1 penny',
        '1 dime and 16 pennies',
        '2 dimes and 6 pennies',
        '1 nickel and 21 pennies',
        '1 dime, 1 nickel, and 11 pennies',
        '2 dimes, 1 nickel, and 1 penny',
        '2 nickels and 16 pennies',
        '1 dime, 2 nickels, and 6 pennies',
        '3 nickels and 11 pennies',
        '1 dime, 3 nickels, and 1 penny',
        '4 nickels and 6 pennies',
        '5 nickels and 1 penny',
    ]

    out_ok(out, 26, wanted)


# --------------------------------------------------
def out_ok(out, value, lines):
    """Parse the output, test for header, num_lines, values"""

    out_lines = out.splitlines()

    num_lines = len(lines) + 1
    assert len(out_lines) == num_lines

    hdr = 'If you give me {} cent{}, I can give you:'.format(
        value, '' if value == 1 else 's')
    assert out_lines[0] == hdr

    for expected in lines:
        assert any(map(lambda l: re.search(expected, l), out_lines))
