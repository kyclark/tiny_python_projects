#!/usr/bin/env python3
"""tests for rhymer.py"""

import os
from subprocess import getoutput

prg = './rhymer.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_take():
    """one item"""

    out = getoutput('{} take'.format(prg)).splitlines()
    assert len(out) == 54
    assert out[0] == 'bake'
    assert out[-1] == 'thrake'


# --------------------------------------------------
def test_chair():
    """one item"""

    out = getoutput('{} chair'.format(prg)).splitlines()
    assert len(out) == 54
    assert out[1] == 'cair'
    assert out[-2] == 'strair'


# --------------------------------------------------
def test_bad():
    """bad"""

    out = getoutput('{} bbb'.format(prg))
    assert out == 'Cannot rhyme "bbb"'
