#!/usr/bin/env python3
"""tests for wod.py"""

import re
import os
import random
from subprocess import getstatusoutput

prg = './wod.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_runs01():
    expected = """
Exercise         Reps
-------------  ------
Pushups            32
Jumping Jacks      56
Situps             88
Pullups            24
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    rv, out = getstatusoutput('{} {} {}'.format(prg, seed_flag, 1))
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_runs02():
    expected = """
Exercise         Reps
-------------  ------
Pushups            15
Jumping Jacks      27
Situps             44
Pullups            12
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    easy_flag = '-e' if random.choice([0, 1]) else '--easy'
    rv, out = getstatusoutput('{} {} {} {}'.format(prg, easy_flag, seed_flag,
                                                   1))
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_runs03():
    expected = """
Exercise      Reps
----------  ------
Burpees         28
Situps          78
Crunches        23
HSPU             6
Pushups         62
Jumprope        93
Lunges          25
Plank           43
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    num_flag = '-n' if random.choice([0, 1]) else '--num_exercises'
    rv, out = getstatusoutput('{} {} 8 {} 2 -f wod.csv'.format(
        prg, num_flag, seed_flag))
    assert rv == 0
    assert out.strip() == expected.strip()

# --------------------------------------------------
def test_runs04():
    expected = """
Exercise                  Reps
----------------------  ------
Hanging Chads               86
Masochistic Elbowdowns      50
Squatting Chinups           35
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    num_flag = '-n' if random.choice([0, 1]) else '--num_exercises'
    rv, out = getstatusoutput('{} {} 3 {} 4 -f wod2.csv'.format(
        prg, num_flag, seed_flag))
    assert rv == 0
    assert out.strip() == expected.strip()
