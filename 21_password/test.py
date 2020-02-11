#!/usr/bin/env python3
"""tests for password.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './password.py'
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
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_num():
    """Dies on bad num"""

    bad = random_string()
    flag = '-n' if random.choice([0, 1]) else '--num'
    rv, out = getstatusoutput(f'{prg} {flag} {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_num_words():
    """Dies on bad num"""

    bad = random_string()
    flag = '-w' if random.choice([0, 1]) else '--num_words'
    rv, out = getstatusoutput(f'{prg} {flag} {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_min_word_len():
    """Dies on bad min_word_len"""

    bad = random_string()
    flag = '-m' if random.choice([0, 1]) else '--min_word_len'
    rv, out = getstatusoutput(f'{prg} {flag} {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_seed():
    """Dies on bad seed"""

    bad = random_string()
    flag = '-s' if random.choice([0, 1]) else '--seed'
    rv, out = getstatusoutput(f'{prg} {flag} {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
