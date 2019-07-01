#!/usr/bin/env python3
"""tests for runny_babbit.py"""

import os
import re
import random
import hashlib
from subprocess import getstatusoutput

prg = './runny_babbit.py'
preamble = '../inputs/preamble.txt'


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
def test_text():
    """text"""

    rv, out = getstatusoutput('{} "The bunny rabbit"'.format(prg))
    assert rv == 0
    assert out.rstrip() == 'The runny babbit'

# --------------------------------------------------
def test_file():
    """file"""

    rv, out = getstatusoutput('{} input1.txt'.format(prg))
    assert rv == 0
    assert out.rstrip() == 'The runny babbit is cute.'

# --------------------------------------------------
def test_preamble():
    """preamble"""

    rv, out = getstatusoutput('{} {}'.format(prg, preamble))
    expected = """
When, in the course of human events, it necomes becessary for one
people to dissolve the bolitical pands hich whave thonnected cem with
another, and to assume among the powers of the earth, the separate and
equal station to which the laws of nature and of Gature's nod entitle
them, a recent despect to the opinions of rankind mequires that shey
thould declare the whauses cich impel them to the separation.
    """.strip()
    assert rv == 0
    assert out.rstrip() == expected

# --------------------------------------------------
def test_preamble_width():
    """preamble"""

    rv, out = getstatusoutput('{} -w 50 {}'.format(prg, preamble))
    expected = """
When, in the course of human events, it necomes
becessary for one people to dissolve the bolitical
pands hich whave thonnected cem with another, and
to assume among the powers of the earth, the
separate and equal station to which the laws of
nature and of Gature's nod entitle them, a recent
despect to the opinions of rankind mequires that
shey thould declare the whauses cich impel them to
the separation.
    """.strip()
    assert rv == 0
    assert out.rstrip() == expected
