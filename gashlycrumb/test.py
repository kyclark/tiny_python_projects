#!/usr/bin/env python3
"""tests for gashlycrumb.py"""

import re
import random
from subprocess import getstatusoutput, getoutput

prg = './gashlycrumb.py'


# --------------------------------------------------
def file_flag():
    return '-f' if random.randint(0, 1) else '--file'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_a():
    out = getoutput('{} a'.format(prg))
    expected = 'A is for Amy who fell down the stairs.'
    assert out.strip() == expected


# --------------------------------------------------
def test_y():
    out = getoutput('{} Y'.format(prg))
    expected = 'Y is for Yorick whose head was bashed in.'
    assert out.strip() == expected


# --------------------------------------------------
def test_number():
    out = getoutput('{} 5'.format(prg))
    expected = 'I do not know "5".'
    assert out.strip() == expected


# --------------------------------------------------
def test_too_long():
    out = getoutput('{} ch'.format(prg))
    expected = '"CH" is not 1 character.'
    assert out.strip() == expected
