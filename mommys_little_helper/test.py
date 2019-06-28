#!/usr/bin/env python3
"""tests for helper.py"""

import re
import os
import random
import string
from subprocess import getstatusoutput

prg = './helper.py'


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
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """steed"""

    rv, out = getstatusoutput('{} _t_ed'.format(prg))
    assert rv == 0
    assert out.rstrip() == '  1: steed'

# --------------------------------------------------
def test_02():
    """another test"""

    rv, out = getstatusoutput('{} ex___s'.format(prg))
    assert rv == 0
    expected = """  1: excess
  2: excuss
  3: exitus
  4: exodos
  5: exodus
  6: exomis
    """.rstrip()
    assert out.rstrip() == expected
