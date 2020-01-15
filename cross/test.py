#!/usr/bin/env python3
"""tests for cross.py"""

import re
import os
import random
import string
from subprocess import getstatusoutput

prg = './cross.py'


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
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_wordlist():
    """bad wordlist"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -w {bad} _t_ed')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_01():
    """steed"""

    rv, out = getstatusoutput(f'{prg} _t_ed')
    assert rv == 0
    assert out.rstrip() == '  1: steed'


# --------------------------------------------------
def test_02():
    """another test"""

    rv, out = getstatusoutput(f'{prg} ex___s')
    assert rv == 0
    expected = """  1: excess
  2: excuss
  3: exitus
  4: exodos
  5: exodus
  6: exomis
    """.rstrip()
    assert out.rstrip() == expected


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
