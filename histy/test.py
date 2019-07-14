#!/usr/bin/env python3
"""tests for histy.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './histy.py'
sonnet = '../inputs/sonnet-29.txt'
fox = '../inputs/fox.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert (rv > 0) if flag == '' else (rv == 0)
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_symbol():
    """test bad symbol"""

    rv, out = getstatusoutput('{} -s XX {}'.format(prg, fox))
    assert rv != 0
    assert re.search('--symbol "XX" must be one character', out)


# --------------------------------------------------
def run(file, args, expected_out):
    """test"""

    assert os.path.isfile(file)
    expected = open(os.path.join('test-outs', expected_out)).read().rstrip()
    rv, out = getstatusoutput('{} {} {}'.format(prg, args, file))
    assert rv == 0
    assert expected == out.rstrip()


# --------------------------------------------------
def test_01():
    """test"""

    run(fox, '', 'fox.txt.1')


# --------------------------------------------------
def test_02():
    """test"""

    run(fox, '-i', 'fox.txt.2')


# --------------------------------------------------
def test_03():
    """test"""

    run(fox, "-s '!'", 'fox.txt.3')


# --------------------------------------------------
def test_04():
    """test"""

    run(sonnet, "-m 2", 'sonnet-29.txt.1')


# --------------------------------------------------
def test_05():
    """test"""

    run(sonnet,
        "--width 50 --minimum 2 --frequency_sort --symbol '$'",
        'sonnet-29.txt.2')
