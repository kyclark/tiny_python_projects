#!/usr/bin/env python3
"""tests for wod.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './wod.py'
input1 = 'exercises.csv'
input2 = 'silly-exercises.csv'


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
def test_bad_file():
    """Dies on bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -f {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_seed1():
    """Runs OK"""

    expected = """
Exercise      Reps
----------  ------
Plank           54
Lunges          35
Crunches        27
Situps          76
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    rv, out = getstatusoutput(f'{prg} {seed_flag} 1')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_seed1_easy():
    """Runs OK"""

    expected = """
Exercise      Reps
----------  ------
Plank           27
Lunges          17
Crunches        13
Situps          38
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    easy_flag = '-e' if random.choice([0, 1]) else '--easy'
    rv, out = getstatusoutput(f'{prg} {easy_flag} {seed_flag} 1')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_seed2_num8():
    """Runs OK"""

    expected = """
Exercise      Reps
----------  ------
Pullups         12
Crunches        30
Plank           53
Situps          95
Lunges          25
Burpees         50
Pushups         28
Squats          22
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    num_flag = '-n' if random.choice([0, 1]) else '--num'
    rv, out = getstatusoutput(f'{prg} {num_flag} 8 {seed_flag} 2 -f {input1}')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_seed4_num3_input2():
    """Runs OK"""

    expected = """
Exercise                Reps
--------------------  ------
Squatting Chinups         27
Existential Earflaps      24
Erstwhile Lunges          20
"""

    seed_flag = '-s' if random.choice([0, 1]) else '--seed'
    num_flag = '-n' if random.choice([0, 1]) else '--num'
    rv, out = getstatusoutput(f'{prg} {num_flag} 3 {seed_flag} 4 -f {input2}')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
