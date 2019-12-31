#!/usr/bin/env python3
"""tests for friar.py"""

import os
import re
from subprocess import getstatusoutput, getoutput

prg = './friar.py'


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
def test_two_syllable_ing_words():
    """two-syllable ing words"""

    tests = [("cooking", "cookin'"), ("Fishing", "Fishin'")]
    for given, expected in tests:
        out = getoutput(f'{prg} {given}')
        assert out.strip() == expected.strip()


# --------------------------------------------------
def test_one_syllable_ing_words():
    """one syllable ing words"""

    tests = [("sing", "sing"), ("Fling", "Fling")]
    for given, expected in tests:
        out = getoutput(f'{prg} {given}')
        assert out.strip() == expected.strip()


# --------------------------------------------------
def test_you_yall():
    """you/y'all"""

    tests = [("you", "y'all"), ("You", "Y'all")]
    for given, expected in tests:
        out = getoutput(f'{prg} {given}')
        assert out.strip() == expected.strip()


# --------------------------------------------------
def run_file(file):
    """run with file"""

    assert os.path.isfile(file)
    expected_file = file + '.out'

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read()

    out = getoutput(f'{prg} {file}')
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_blake():
    """blake"""

    run_file('inputs/blake.txt')


# --------------------------------------------------
def test_banner():
    """banner"""

    run_file('inputs/banner.txt')


# --------------------------------------------------
def test_raven():
    """raven"""

    run_file('inputs/raven.txt')


# --------------------------------------------------
def test_dickinson():
    """dickinson"""

    run_file('inputs/dickinson.txt')


# --------------------------------------------------
def test_shakespeare():
    """shakespeare"""

    run_file('inputs/shakespeare.txt')
