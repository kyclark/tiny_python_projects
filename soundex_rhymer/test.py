#!/usr/bin/env python3
"""tests for rhymer.py"""

import os
import random
import re
from subprocess import getstatusoutput, getoutput

prg = './rhymer.py'


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
def test_no_vowel():
    """test"""

    word = ''.join(random.sample('bcdtprhmntghqw', k=5))
    rv, out = getstatusoutput('{} {}'.format(prg, word))
    assert rv != 0
    expected = 'word "{}" must contain at least one vowel'.format(word)
    assert re.search(expected, out)


# --------------------------------------------------
def test_01():
    """test"""

    out = getoutput('{} -s listen'.format(prg)).splitlines()
    assert len(out) == 196
    assert 'wisdom' in out


# --------------------------------------------------
def test_02():
    """test"""

    out = getoutput('{} listen'.format(prg)).splitlines()
    assert len(out) == 37
    assert 'lighten' in out


# --------------------------------------------------
def test_03():
    """test"""

    out = getoutput('{} orange'.format(prg))
    assert len(out.splitlines()) == 7
