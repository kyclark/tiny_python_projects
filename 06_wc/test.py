#!/usr/bin/env python3
"""tests for wc.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './wc.py'
empty = './inputs/empty.txt'
one_line = './inputs/one.txt'
two_lines = './inputs/two.txt'
fox = '../inputs/fox.txt'
sonnet = '../inputs/sonnet-29.txt'


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
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_bad_file():
    """bad_file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_empty():
    """Test on empty"""

    rv, out = getstatusoutput(f'{prg} {empty}')
    assert rv == 0
    assert out.rstrip() == '       0       0       0 ./inputs/empty.txt'


# --------------------------------------------------
def test_one():
    """Test on one"""

    rv, out = getstatusoutput(f'{prg} {one_line}')
    assert rv == 0
    assert out.rstrip() == '       1       1       2 ./inputs/one.txt'


# --------------------------------------------------
def test_two():
    """Test on two"""

    rv, out = getstatusoutput(f'{prg} {two_lines}')
    assert rv == 0
    assert out.rstrip() == '       2       2       4 ./inputs/two.txt'


# --------------------------------------------------
def test_fox():
    """Test on fox"""

    rv, out = getstatusoutput(f'{prg} {fox}')
    assert rv == 0
    assert out.rstrip() == '       1       9      45 ../inputs/fox.txt'


# --------------------------------------------------
def test_more():
    """Test on more than one file"""

    rv, out = getstatusoutput(f'{prg} {fox} {sonnet}')
    expected = ('       1       9      45 ../inputs/fox.txt\n'
                '      17     118     661 ../inputs/sonnet-29.txt\n'
                '      18     127     706 total')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_stdin():
    """Test on stdin"""

    rv, out = getstatusoutput(f'{prg} < {fox}')
    assert rv == 0
    assert out.rstrip() == '       1       9      45 <stdin>'
