#!/usr/bin/env python3
"""tests for chain.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './chain.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert (rv > 0) if flag == '' else (rv == 0)
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_word():
    """test"""
    rv, out = getstatusoutput('{} foobar'.format(prg))
    assert rv != 0
    assert out == 'Unknown word "foobar"'

# --------------------------------------------------
def test_01():
    """test"""

    rv, out = getstatusoutput('{} -s 1 bike'.format(prg))
    expected = """
Failed to find more words!
bike ->
  1: bile
  2: vile
  3: lile
  4: line
  5: like
  6: Mike
  7: Miki
  8: Mimi
  9: Mime
 10: Mixe
    """.strip()
    assert rv == 1
    assert expected == out.strip()

# --------------------------------------------------
def test_02():
    """test"""

    rv, out = getstatusoutput('{} --seed 2 --max_distance 2 bike'.format(prg))
    expected = """bike ->
  1: bider
  2: bidet
  3: beret
  4: besit
  5: bejig
  6: redig
  7: retin
  8: recon
  9: reck
 10: seak
 11: reek
 12: roe
 13: bae
 14: buy
 15: mu
 16: r
 17: rox
 18: wo
 19: toy
 20: tad
    """.rstrip()
    assert rv == 0
    assert expected == out.rstrip()
