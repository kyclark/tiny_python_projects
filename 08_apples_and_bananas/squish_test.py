#!/usr/bin/env python3
"""tests for squish.py"""

import re
import os
from subprocess import getstatusoutput, getoutput

prg = './squish.py'
fox = '../inputs/fox.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_vowel():
    """Should fail on a bad vowel"""

    rv, out = getstatusoutput(f'{prg} -v x foo')
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_command_line():
    """ foo -> fa """

    out = getoutput(f'{prg} foo')
    assert out.strip() == 'fa'


# --------------------------------------------------
def test_command_line_with_vowel():
    """ foo -> fi """

    out = getoutput(f'{prg} -v i foo')
    assert out.strip() == 'fi'


# --------------------------------------------------
def test_command_line_with_vowel_preserve_case():
    """ FOO AND FAA -> FE END FE """

    out = getoutput(f'{prg} "FOO AND FAA" --vowel e')
    assert out.strip() == 'FE END FE'


# --------------------------------------------------
def test_file():
    """ fox.txt """

    out = getoutput(f'{prg} {fox}')
    assert out.strip() == 'Tha qack brawn fax jamps avar tha lazy dag.'


# --------------------------------------------------
def test_file_with_vowel():
    """ fox.txt """

    out = getoutput(f'{prg} --vowel o {fox}')
    assert out.strip() == 'Tho qock brown fox jomps ovor tho lozy dog.'
