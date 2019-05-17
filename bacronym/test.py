#!/usr/bin/env python3
"""tests for bacronym.py"""

import re
import random
from subprocess import getstatusoutput, getoutput

prg = './bacronym.py'


# --------------------------------------------------
def seed_flag():
    return '-s' if random.randint(0, 1) else '--seed'


# --------------------------------------------------
def number_flag():
    return '-n' if random.randint(0, 1) else '--number'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_play01():
    out = getoutput('{} {} 1 FBI'.format(prg, seed_flag()))
    expected = """
FBI =
 - Fecundity Brokage Imitant
 - Figureless Basketmaking Ismailite
 - Frumpery Bonedog Irregardless
 - Foxily Blastomyces Inedited
 - Fastland Bouncingly Idiospasm
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play02():
    out = getoutput('{} {} 2 {} 3 FBI'.format(prg, seed_flag(), number_flag()))
    expected = """
FBI =
 - Fanaticism Bark Impecuniary
 - Flapper Bedlids Instinctively
 - Fightingly Buckstay Inelaborated
""".strip()
    assert out.strip() == expected
