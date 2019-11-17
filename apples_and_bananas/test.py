#!/usr/bin/env python3
"""tests for apples.py"""

import re
import os
import random
from subprocess import getstatusoutput, getoutput

prg = './apples.py'
fox = '../inputs/fox.txt'


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
def test_bad_vowel():
    """Should fail on a bad vowel"""

    rv, out = getstatusoutput('{} -v x foo'.format(prg))
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_command_line():
    """ foo -> faa """

    out = getoutput('{} foo'.format(prg))
    assert out.strip() == 'faa'


# --------------------------------------------------
def test_command_line_with_vowel():
    """ foo -> fii """

    out = getoutput('{} -v i foo'.format(prg))
    assert out.strip() == 'fii'

# --------------------------------------------------
def test_command_line_with_vowel_preserve_case():
    """ foo -> fii """

    out = getoutput('{} "APPLES AND BANANAS" --vowel i'.format(prg))
    assert out.strip() == 'IPPLIS IND BININIS'


# --------------------------------------------------
def test_file():
    """ fox.txt """

    out = getoutput('{} {}'.format(prg, fox))
    assert out.strip() == 'Tha qaack brawn fax jamps avar tha lazy dag.'


# --------------------------------------------------
def test_file_with_vowel():
    """ fox.txt """

    out = getoutput('{} --vowel o {}'.format(prg, fox))
    assert out.strip() == 'Tho qoock brown fox jomps ovor tho lozy dog.'
