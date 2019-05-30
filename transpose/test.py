#!/usr/bin/env python3
"""tests for transpose.py"""

import os
import random
import string
from subprocess import getstatusoutput

prg = "./transpose.py"
legacy = 'songs/legacy.abc'
paddy = 'songs/paddy.abc'


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))

        if flag == '':
            assert rv > 0
        else:
            assert rv == 0

        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_input():
    """file input"""
    bad = random_string()

    rv, out = getstatusoutput('{} {}'.format(prg, bad))

    assert rv > 0
    assert out == '"{}" is not a file'.format(bad)

# --------------------------------------------------
def test_file():
    """file input"""

    for in_file in [legacy, paddy]:
        for interval in ['2', '4', '-5']:
            rv, out = getstatusoutput('{} -s {} {}'.format(
                prg, interval, in_file))
            expected = open('.'.join([in_file, interval, 'out'])).read()
            assert rv == 0
            assert out.rstrip() == expected.rstrip()
