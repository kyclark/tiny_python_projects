#!/usr/bin/env python3
"""tests for telephone.py"""

from subprocess import getstatusoutput, getoutput
import os
import re

prg = "./telephone.py"
fox = '../inputs/fox.txt'
now = '../inputs/now.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match('usage', out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_mutation():
    """bad mutation values"""

    for val in ['-1.0', '10.0']:
        rv, out = getstatusoutput('{} -m {} {}'.format(prg, val, fox))
        assert rv > 0
        assert re.search('--mutations "{}" must be b/w 0 and 1'.format(val),
                         out)


# --------------------------------------------------
def test_text01():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput('{} -s 1 "{}"'.format(prg, txt))
    assert rv == 0
    expected = """
    Now ao the time for all good-men to came to the aid of Whe pa*ty
    """.strip()
    assert out.rstrip() == expected


# --------------------------------------------------
def test_text02():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput('{} -s 2 -m .4 "{}"'.format(prg, txt))
    assert rv == 0
    expected = """
    NUw iVKPqe time fErXal; gPod"'en to come`Do *Dl aFd of!the Yabta
    """.strip()
    assert out.rstrip() == expected


# --------------------------------------------------
def test_file01():
    """test"""

    rv, out = getstatusoutput('{} --seed 1 {}'.format(prg, fox))
    assert rv == 0
    assert out.rstrip() == 'Tho quick brown foa jumps oWer*the lazy dog.'


# --------------------------------------------------
def test_file02():
    """test"""

    rv, out = getstatusoutput('{} --seed 2 --mutations .6 {}'.format(prg, fox))
    assert rv == 0
    assert out.rstrip() == 'UheK+u*ckXbrPw~ fox Du*#FT{ver f~e}|Uzy (T?l'
