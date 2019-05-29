#!/usr/bin/env python3
"""tests for presto.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

prg = './presto.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_01():
    out = getoutput('{} presto'.format(prg))
    expected = """
presto =
   1. poster
   2. repost
   3. respot
   4. stoper
   """.strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_02():
    out = getoutput('{} parliament -w t/words1.txt --num_combos 2'.format(prg))
    expected = """
parliament =
   1. ailment rap
   2. rap ailment
    """.strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_03():
    out = getoutput('{} presto -n 2'.format(prg)).splitlines()
    assert len(out) == 101
    assert out[1] == '   1. er post'
    assert out[-1] == ' 100. tor pes'
