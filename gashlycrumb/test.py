#!/usr/bin/env python3
"""tests for gashlycrumb.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput

prg = './gashlycrumb.py'


# --------------------------------------------------
def file_flag():
    """Either -f or --file"""

    return '-f' if random.randint(0, 1) else '--file'


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
def test_a():
    """Test for 'a'"""

    rv, out = getstatusoutput('{} a'.format(prg))
    assert rv == 0
    expected = 'A is for Amy who fell down the stairs.'
    assert out.strip() == expected


# --------------------------------------------------
def test_y():
    """Test for 'y'"""

    rv, out = getstatusoutput('{} Y'.format(prg))
    assert rv == 0
    expected = 'Y is for Yorick whose head was bashed in.'
    assert out.strip() == expected


# --------------------------------------------------
def test_number():
    """Test for a number"""

    rv, out = getstatusoutput('{} 5'.format(prg))
    assert rv == 0
    expected = 'I do not know "5".'
    assert out.strip() == expected


# --------------------------------------------------
def test_too_long():
    """Test for too long"""

    rv, out = getstatusoutput('{} ch'.format(prg))
    assert rv != 0
    expected = '"ch" is not 1 character'
    assert re.search(expected, out)

# --------------------------------------------------
def test_bad_file():
    """Test for bad --file"""

    bad_file = random_string()
    letter = random.choice(string.ascii_lowercase)
    rv, out = getstatusoutput('{} {} -f {}'.format(prg, letter, bad_file))
    assert rv != 0
    expected = "No such file or directory: '{}'".format(bad_file)
    assert re.search(expected, out)

# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
