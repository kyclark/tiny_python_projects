#!/usr/bin/env python3
"""tests for histy.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './histy.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert (rv > 0) if flag == '' else (rv == 0)
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def run(n):
    """test"""

    in_file = os.path.join('out', '{}.in'.format(n))
    out_file = os.path.join('out', '{}.out'.format(n))
    given = open(in_file).read().rstrip()
    expected = open(out_file).read().rstrip()
    cmd = '{} {}'.format(prg, given)
    rv, out = getstatusoutput(cmd)
    assert rv == 0
    assert expected == out


# --------------------------------------------------
def test_01():
    """test"""

    run('1')


# --------------------------------------------------
def test_02():
    """test"""

    run('2')


# --------------------------------------------------
def test_03():
    """test"""

    run('3')


# --------------------------------------------------
def test_04():
    """test"""

    run('4')


# --------------------------------------------------
def test_05():
    """test"""

    run('5')
