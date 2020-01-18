#!/usr/bin/env python3
"""tests for wod.py"""

import os
import random
from subprocess import getstatusoutput

prg = './wod.py'
input1 = 'exercises.csv'
input2 = 'silly-exercises.tab'


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
def test_runs01():
    """Runs OK"""

    expected = """
Exercise         Reps
-------------  ------
Pushups            32
Jumping Jacks      56
Situps             88
Pullups            24
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    rv, out = getstatusoutput(f'{prg} {seed_flag} 1')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_runs02():
    """Runs OK"""

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
    rv, out = getstatusoutput(f'{prg} {easy_flag} {seed_flag} 1')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_runs03():
    """Runs OK"""

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
    rv, out = getstatusoutput(f'{prg} {num_flag} 8 {seed_flag} 2 -f {input1}')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_runs04():
    """Runs OK"""

    expected = """
Exercise                  Reps
----------------------  ------
Hanging Chads               86
Masochistic Elbowdowns      50
Squatting Chinups           35
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    num_flag = '-n' if random.choice([0, 1]) else '--num_exercises'
    rv, out = getstatusoutput(f'{prg} {num_flag} 3 {seed_flag} 4 -f {input2}')
    assert rv == 0
    assert out.strip() == expected.strip()
