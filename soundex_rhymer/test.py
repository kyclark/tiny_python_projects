#!/usr/bin/env python3
"""tests for rhymer.py"""

import re
import random
from subprocess import getstatusoutput, getoutput

prg = './rhymer.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_play01():
    out = getoutput('{} listen'.format(prg)).splitlines()
    assert len(out) == 161
    assert ('wisdom' in out)


# --------------------------------------------------
def test_play02():
    out = getoutput('{} orange'.format(prg))
    assert len(out.splitlines()) == 150
