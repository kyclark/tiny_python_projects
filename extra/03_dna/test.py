#!/usr/bin/env python3
"""tests for dna.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

prg = './dna.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_no_arg_and_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert out.lower().startswith('usage')


# --------------------------------------------------
def run_single(base):
    """Run a single base test"""

    num = random.randint(1, 10)
    given = base * num
    rv, out = getstatusoutput(f'{prg} {given}')
    assert rv == 0
    cmp = base.upper()
    expected = f'{num} 0 0 0' if cmp == 'A' else \
        f'0 {num} 0 0' if cmp == 'C' else \
        f'0 0 {num} 0' if cmp == 'G' else \
        f'0 0 0 {num}'
    assert out == expected


# --------------------------------------------------
def test_a_upper():
    """A"""

    run_single('A')


# --------------------------------------------------
def test_a_lower():
    """a"""

    run_single('a')


# --------------------------------------------------
def test_c_upper():
    """C"""

    run_single('C')


# --------------------------------------------------
def test_c_lower():
    """c"""

    run_single('c')


# --------------------------------------------------
def test_g_upper():
    """G"""

    run_single('G')


# --------------------------------------------------
def test_g_lower():
    """g"""

    run_single('g')


# --------------------------------------------------
def test_t_upper():
    """T"""

    run_single('T')


# --------------------------------------------------
def test_t_lower():
    """t"""

    run_single('t')

# --------------------------------------------------
def test_rosalind_example():
    """From http://rosalind.info/problems/dna/"""

    dna = ('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATT'
           'AAAAAAAGAGTGTCTGATAGCAGC')

    rv, out = getstatusoutput(f'{prg} {dna}')
    assert rv == 0
    assert out == '20 12 17 21'
