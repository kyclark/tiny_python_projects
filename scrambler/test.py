#!/usr/bin/env python3
"""tests for scrambler.py"""

import os
import re
from subprocess import getstatusoutput, getoutput

prg = './scrambler.py'
fox = '../inputs/fox.txt'
bustle = '../inputs/the-bustle.txt'
spiders = '../inputs/spiders.txt'


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
def test_text1():
    """Text"""

    out = getoutput('{} foobar -s 1'.format(prg))
    assert out.strip() == 'faobor'


# --------------------------------------------------
def test_text2():
    """Text"""

    text = 'The quick brown fox jumps over the lazy dog.'
    expected = 'The qicuk bworn fox jpmus oevr the lzay dog.'
    out = getoutput('{} "{}" -s 2'.format(prg, text))
    assert out.strip() == expected


# --------------------------------------------------
def test_file_bustle():
    """File input"""

    expected = """
The blutse in a hosue
The mrinong afetr daeth
Is seosnmelt of iinuetdrss
Etecand uopn eatrh,--

The sweenpig up the hraet,
And pttinug lvoe aawy
We slhal not wnat to use aagin
Utnil enterity.
    """.strip()

    out = getoutput('{} --seed 3 {}'.format(prg, bustle))
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_file_fox():
    """File input"""

    out = getoutput('{} --seed 4 {}'.format(prg, fox))
    assert out.strip() == 'The qciuk bworn fox jpums oevr the lzay dog.'


# --------------------------------------------------
def test_file_spiders():
    """File input"""

    out = getoutput('{} --seed 9 {}'.format(prg, spiders))
    assert out.strip() == 'Don’t wrory, sedrpis,\nI keep huose\ncaslaluy.'
