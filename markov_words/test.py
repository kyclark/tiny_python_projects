#!/usr/bin/env python3
"""tests for markov.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput

prg = './markov.py'
const = '../inputs/const.txt'
dickinson = '../inputs/dickinson.txt'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_01():
    """Test"""

    out = getoutput('{} -s 2 {}'.format(prg, const))
    expected = """
  1: extri
  2: uirepres
  3: yonstorsonf
  4: endangr
  5: mordiclym
  6: asenertio
  7: lotwerma
  8: parandentri
  9: quiresid
 10: gailighted
    """.strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_02():
    """Test"""
    args = '--seed 1 --kmer_size 4 --num_words 5 --max_word 8'
    out = getoutput('{} {} {}'.format(prg, args, dickinson))
    expected = """
  1: liriou
  2: savious
  3: untrys
  4: hempen
  5: urday
    """.strip()
    assert out.strip() == expected
