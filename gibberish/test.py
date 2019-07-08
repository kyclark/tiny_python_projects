#!/usr/bin/env python3
"""tests for gibberish.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput

prg = './gibberish.py'
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
def test_01():
    """Test"""

    out = getoutput('{} -s 2 {}'.format(prg, const))
    expected = """
  1: extri
  2: uirepres
  3: rceptityfi
  4: ighersonsta
  5: titson
  6: btsoneven
  7: hundentiver
  8: zatesside
  9: bjectivente
 10: manceediat
    """.strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_02():
    """Test"""

    args = '--seed 1 --kmer_size 4 --num_words 5 --max_word 8'
    out = getoutput('{} {} {}'.format(prg, args, dickinson))
    expected = """
  1: miled
  2: iliar
  3: noticin
  4: venture
  5: nelled
    """.strip()
    assert out.strip() == expected
