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
def run(file, args, expected_out):
    """test"""

    in_file = os.path.join('../inputs', '{}'.format(file))
    expected = open(os.path.join('test-outs', expected_out)).read().rstrip()
    rv, out = getstatusoutput('{} {} {}'.format(prg, args, in_file))
    assert rv == 0
    assert expected == out.rstrip()


# --------------------------------------------------
def test_01():
    """test"""

    run('fox.txt', '', 'fox.txt.1')


# --------------------------------------------------
def test_02():
    """test"""

    run('fox.txt', '-i', 'fox.txt.2')


# --------------------------------------------------
def test_03():
    """test"""

    run('fox.txt', "-c '!'", 'fox.txt.3')

# --------------------------------------------------
def test_04():
    """test"""

    run('sonnet-29.txt', "-m 2", 'sonnet-29.txt.1')

# --------------------------------------------------
def test_05():
    """test"""

    run('sonnet-29.txt', "-w 50 -m 2 -f -c '$'", 'sonnet-29.txt.2')
