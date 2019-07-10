#!/usr/bin/env python3
"""Tests for hangman.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './hangman.py'


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
def test_bad_wordfile():
    """bad_wordfile"""

    bad = random_string()
    rv, out = getstatusoutput('{} --wordlist "{}"'.format(prg, bad))
    assert rv != 0
    assert re.search("No such file or directory: '{}'".format(bad), out)


# --------------------------------------------------
def test_bad_minlen():
    """bad minlen"""

    bad = random.choice(range(-10, 1))
    rv, out = getstatusoutput('{} --minlen "{}"'.format(prg, bad))
    assert rv != 0
    assert re.search('--minlen "{}" must be positive'.format(bad), out)


# --------------------------------------------------
def test_bad_maxlen():
    """bad maxlen"""

    bad = random.choice(range(20, 50))
    rv, out = getstatusoutput('{} --maxlen "{}"'.format(prg, bad))
    assert rv != 0
    assert re.search('--maxlen "{}" must be < 20'.format(bad), out)


# --------------------------------------------------
def test_switch_minmax():
    """switch_minmax"""

    min_len = random.choice(range(10, 20))
    max_len = random.choice(range(10))

    rv, out = getstatusoutput('{} -l {} -n {}'.format(prg, max_len, min_len))
    assert rv != 0
    assert re.search(
        '--minlen "{}" is greater than --maxlen "{}"'.format(min_len, max_len),
        out)


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_wins():
    """Test runs"""

    rv, out = getstatusoutput('{} --seed 1 -i etlai'.format(prg))
    assert rv == 0
    assert re.search('You win!', out)

# --------------------------------------------------
def test_loses():
    """Test runs"""

    rv, out = getstatusoutput('{} -s 1 -m 1 -i xx'.format(prg))
    assert rv == 0
    assert re.search('You lose, loser!', out)
