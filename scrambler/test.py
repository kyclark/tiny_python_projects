#!/usr/bin/env python3
"""tests for scrambler.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput

prg = './scrambler.py'
fox = '../inputs/fox.txt'
bustle = '../inputs/the-bustle.txt'


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
    expected = 'The qicuk bworn fox jpmus over the lzay dgo.'
    out = getoutput('{} "{}" -s 2'.format(prg, text))
    assert out.strip() == expected


# --------------------------------------------------
def test_file_fox():
    """File input"""

    expected = """
The blutse in a hosue
The mrinong afetr daeth
Is seosnmelt of iinuetdrss
Etecand upon e,hrta—

The sweeipng up the hreta,
And ptnitug love away
We shall not want to use again
Until erttenyi.
    """.strip()
    out = getoutput('{} --seed 3 {}'.format(prg, bustle))
    assert out.strip() == expected
# --------------------------------------------------
def test_file_bustle():
    """File input"""

    out = getoutput('{} --seed 4 {}'.format(prg, fox))
    assert out.strip() == 'The qciuk bworn fox jpums oevr the lzay dgo.'
