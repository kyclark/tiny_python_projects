#!/usr/bin/env python3
"""tests for twelve_days.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

prg = './twelve_days.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_01():
    out = getoutput('{}'.format(prg)).splitlines()
    assert len(out) == 113
    assert out[0] == 'On the first day of Christmas,'
    assert out[-1] == 'And a partridge in a pear tree.'


# --------------------------------------------------
def test_02():
    out_file = random_string()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        out = getoutput('{} -n 4 -o {}'.format(prg, out_file))
        assert os.path.isfile(out_file)
        output = open(out_file).read().splitlines()
        assert len(output) == 22
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)
