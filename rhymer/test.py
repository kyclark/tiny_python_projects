#!/usr/bin/env python3
"""tests for rhymer.py"""

from subprocess import getoutput

prg = './rhymer.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """one item"""

    out = getoutput('{} take'.format(prg)).splitlines()
    assert len(out) == 55
    assert out[0] == 'bake'
    assert out[-1] == 'thrake'
