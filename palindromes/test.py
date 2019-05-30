#!/usr/bin/env python3
"""tests for palindromic.py"""

import re
import random
from subprocess import getstatusoutput, getoutput

prg = './palindromic.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_str():
    s = 'wow are you my mom?'
    out = getoutput('{} "Wow, are you my Mom?"'.format(prg)).splitlines()
    assert out == ['wow', 'mom']


# --------------------------------------------------
def test_file():
    out = getoutput('{} input.txt'.format(prg))
    expected = """
anna
civic
kayak
madam
mom
wow
level
noon
racecar
radar
redder
refer
rotator
rotor
solos
stats
tenet
    """.strip()
    assert out.strip() == expected
