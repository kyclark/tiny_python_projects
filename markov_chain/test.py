#!/usr/bin/env python3
"""tests for markov.py"""

import os
import re
import random
from subprocess import getstatusoutput, getoutput

prg = './markov.py'
const = '../inputs/const.txt'
dickinson = '../inputs/dickinson.txt'


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
def test_runs01():
    """runs"""

    out = getoutput('{} -s 3 {}'.format(prg, const))
    expected = open('test-outs/const.seed3.width70.len500').read()
    assert out.rstrip() == expected.rstrip()


# --------------------------------------------------
def test_runs02():
    """runs"""

    args = '{} --seed 4 --length 300 --text_width 50 {}'
    out = getoutput(args.format(prg, const))
    expected = open('test-outs/const.seed4.width50.len300').read()
    assert out.rstrip() == expected.rstrip()


# --------------------------------------------------
def test_runs03():
    """runs"""

    args = '{} --seed 4 --length 300 --text_width 50 --num_words 3 {}'
    out = getoutput(args.format(prg, const))
    expected = open('test-outs/const.seed4.width50.len300.words3').read()
    assert out.rstrip() == expected.rstrip()


# --------------------------------------------------
def test_runs04():
    """runs"""

    args = '{} -s 1 -l 100 -w 30 {}'
    out = getoutput(args.format(prg, dickinson))
    expected = open('test-outs/dickinson.seed1.width30.len100').read()
    assert out.rstrip() == expected.rstrip()
