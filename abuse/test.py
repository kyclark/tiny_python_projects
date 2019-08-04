#!/usr/bin/env python3
"""tests for abuse.py"""

import os
import random
import re
from subprocess import getstatusoutput, getoutput

prg = './abuse.py'


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
def test_bad_number():
    """bad_number"""

    n = random.choice(range(-10, 0))
    rv, out = getstatusoutput('{} -n {}'.format(prg, n))
    assert rv != 0
    assert re.search('--number "{}" must be > 1'.format(n), out)


# --------------------------------------------------
def test_01():
    """test"""

    out = getoutput('{} -s 1 -n 1'.format(prg))
    assert out.strip() == 'You filthsome, cullionly fiend!'


# --------------------------------------------------
def test_02():
    """test"""

    out = getoutput('{} --seed 2'.format(prg))
    expected = """
You corrupt, detestable beggar!
You peevish, foolish gull!
You insatiate, heedless worm!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_03():
    """test"""

    out = getoutput('{} -s 3 -n 5 -a 1'.format(prg))
    expected = """
You infected villain!
You vile braggart!
You peevish worm!
You sodden-witted villain!
You cullionly worm!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_04():
    """test"""

    out = getoutput('{} --seed 4 --number 2 --adjectives 4'.format(prg))
    expected = """
You infected, lecherous, dishonest, rotten recreant!
You filthy, detestable, cullionly, base lunatic!
""".strip()
    assert out.strip() == expected
