#!/usr/bin/env python3
"""tests for abuse.py"""

import re
import random
from subprocess import getstatusoutput, getoutput

prg = './abuse.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_01():
    out = getoutput('{} -s 1'.format(prg))
    expected = """
You filthsome, whoreson barbermonger!
You insatiate, false rogue!
You scurvy, sodden-witted liar!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_02():
    out = getoutput('{} --seed 2 -n 4'.format(prg))
    expected = """
You corrupt, detestable beggar!
You peevish, foolish gull!
You insatiate, heedless whore!
You caterwauling, foolish milksop!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_03():
    out = getoutput('{} -s 3 -n 5 -a 1'.format(prg))
    expected = """
You infected villain!
You vile braggart!
You peevish whore!
You sodden-witted villain!
You cullionly whore!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_04():
    out = getoutput('{} --seed 4 --number 2 --adjectives 4'.format(prg))
    expected = """
You infected, lecherous, dishonest, rotten recreant!
You filthy, detestable, cullionly, base lunatic!
""".strip()
    assert out.strip() == expected
