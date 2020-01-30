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
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file():
    """Test for bad --file"""

    bad = random_string()
    letter = random.choice(string.ascii_lowercase)
    rv, out = getstatusoutput(f'{prg} {letter} -f {bad}')
    assert rv != 0
    expected = f"No such file or directory: '{bad}'"
    assert re.search(expected, out)


# --------------------------------------------------
def test_a():
    """Test for 'a'"""

    rv, out = getstatusoutput(f'{prg} a')
    assert rv == 0
    expected = 'A is for Amy who fell down the stairs.'
    assert out.strip() == expected


# --------------------------------------------------
def test_b_c():
    """Test for 'b c'"""

    rv, out = getstatusoutput(f'{prg} b c')
    assert rv == 0
    expected = ('B is for Basil assaulted by bears.\n'
                'C is for Clara who wasted away.')
    assert out.strip() == expected


# --------------------------------------------------
def test_y():
    """Test for 'y'"""

    rv, out = getstatusoutput(f'{prg} Y')
    assert rv == 0
    expected = 'Y is for Yorick whose head was bashed in.'
    assert out.strip() == expected


# --------------------------------------------------
def test_o_alternate():
    """ Test for 'o' from 'alternate.txt' """

    rv, out = getstatusoutput(f'{prg} o P q -f alternate.txt')
    assert rv == 0
    expected = ('O is for Orville, who fell in a canyon.\n'
                'P is for Paul, strangled by his banyan.\n'
                'Q is for Quintanna, flayed in the night.')
    assert out.strip() == expected


# --------------------------------------------------
def test_bad_letter():
    """Test for bad input"""

    rv, out = getstatusoutput(f'{prg} 5 CH')
    assert rv == 0
    expected = ('I do not know "5".\n' 'I do not know "CH".')
    assert out.strip() == expected


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
