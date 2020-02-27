#!/usr/bin/env python3
"""tests for days.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './days.py'


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
        assert out.lower().startswith('usage')


# --------------------------------------------------
def run_day(day, expected):
    """Run a day"""

    rv, out = getstatusoutput(f'{prg} {day}')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_monday():
    """Monday"""

    run_day('Monday', 'On Mondays I never go to work')


# --------------------------------------------------
def test_tuesday():
    """Tuesday"""

    run_day('Tuesday', 'On Tuesdays I stay at home')


# --------------------------------------------------
def test_wednesday():
    """Wednesday"""

    run_day('Wednesday', 'On Wednesdays I never feel inclined')


# --------------------------------------------------
def test_thursday():
    """Thursday"""

    run_day('Thursday', "On Thursdays, it's a holiday")


# --------------------------------------------------
def test_friday():
    """Friday"""

    run_day('Friday', 'And Fridays I detest')


# --------------------------------------------------
def test_saturday():
    """Saturday"""

    run_day('Saturday', "Oh, it's much too late on a Saturday")


# --------------------------------------------------
def test_sunday():
    """Sunday"""

    run_day('Sunday', 'And Sunday is the day of rest')


# --------------------------------------------------
def test_lower():
    """monday"""

    for day in [
            'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
            'sunday'
    ]:
        rv, out = getstatusoutput(f'{prg} {day}')
        assert rv == 0
        assert out == f'Can\'t find "{day}"'


# --------------------------------------------------
def test_monday_tuesday():
    """Monday Tuesday"""

    run_day(
        'Monday Tuesday', '\n'.join(
            ['On Mondays I never go to work', 'On Tuesdays I stay at home']))


# --------------------------------------------------
def test_mix():
    """Mix good and bad"""

    run_day(
        'Sunday Odinsday Thorsday Friday', '\n'.join([
            'And Sunday is the day of rest', "Can't find \"Odinsday\"",
            "Can't find \"Thorsday\"", 'And Fridays I detest'
        ]))
