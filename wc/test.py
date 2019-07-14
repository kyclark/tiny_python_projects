#!/usr/bin/env python3
"""tests for wc.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './wc.py'
fox = '../inputs/fox.txt'
sonnet = '../inputs/sonnet-29.txt'


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
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_bad_file():
    """bad_file"""

    bad = random_string()
    rv, out = getstatusoutput('{} {}'.format(prg, bad))
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_fox():
    """Test on fox"""

    rv, out = getstatusoutput('{} {}'.format(prg, fox))

    assert rv == 0
    assert out.rstrip() == '       1       9      45 ../inputs/fox.txt'


# --------------------------------------------------
def test_more():
    """Test on more than one file"""

    rv, out = getstatusoutput('{} {} {}'.format(prg, fox, sonnet))

    expected = ('       1       9      45 ../inputs/fox.txt\n'
                '      17     118     661 ../inputs/sonnet-29.txt')
    assert rv == 0
    assert out.rstrip() == expected
