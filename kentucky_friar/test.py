#!/usr/bin/env python3
"""tests for friar.py"""

import re
import random
from subprocess import getstatusoutput, getoutput

prg = './friar.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_ing_words():
    """ing words"""

    tests = [("hunting", "huntin'"), ("Fishing", "Fishin'")]
    for given, expected in tests:
        out = getoutput('{} {}'.format(prg, given))
        assert out.strip() == expected.strip()


# --------------------------------------------------
def test_you_yall():
    """you/y'all"""

    tests = [("you", "y'all"), ("You", "Y'all")]
    for given, expected in tests:
        out = getoutput('{} {}'.format(prg, given))
        assert out.strip() == expected.strip()


# --------------------------------------------------
def test_file_01():
    """test1"""

    in_file = 'tests/input1.txt'
    expected = open(in_file + '.out').read()
    out = getoutput('{} {}'.format(prg, in_file))
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_file_02():
    """test2"""

    in_file = 'tests/input2.txt'
    expected = open(in_file + '.out').read()
    out = getoutput('{} {}'.format(prg, in_file))
    assert out.strip() == expected.strip()
