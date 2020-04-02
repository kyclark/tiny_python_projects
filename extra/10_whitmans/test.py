#!/usr/bin/env python3
"""tests for sampler.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput
from Bio import SeqIO
from Bio.SeqUtils import GC
from numpy import mean
from itertools import chain
from shutil import rmtree

prg = './sampler.py'
n1k = './n1k.fa'
n10k = './n10k.fa'
n100k = './n100k.fa'
n1m = './n1m.fa'


# --------------------------------------------------
def random_string():
    """generate a random string"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


# --------------------------------------------------
def test_exists():
    """usage"""

    for file in [prg, n1k, n10k, n100k, n1m]:
        assert os.path.isfile(file)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file():
    """die on bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.match('usage:', out, re.I)
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_pct():
    """die on bad pct"""

    bad = random.randint(1, 10)
    rv, out = getstatusoutput(f'{prg} -p {bad} {n1k}')
    assert rv != 0
    assert re.match('usage:', out, re.I)
    assert re.search(f'--pct "{float(bad)}" must be between 0 and 1', out)


# --------------------------------------------------
def test_defaults():
    """runs on good input"""

    out_dir = 'out'
    try:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

        rv, out = getstatusoutput(f'{prg} -s 10 {n1k}')
        assert rv == 0
        expected = ('  1: n1k.fa\n'
                    'Wrote 108 sequences from 1 file to directory "out"')
        assert out == expected
        assert os.path.isdir(out_dir)

        files = os.listdir(out_dir)
        assert len(files) == 1

        out_file = os.path.join(out_dir, 'n1k.fa')
        assert os.path.isfile(out_file)

        # correct number of seqs
        seqs = list(SeqIO.parse(out_file, 'fasta'))
        assert len(seqs) == 108

    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)


# --------------------------------------------------
def test_options():
    """runs on good input"""

    out_dir = random_string()
    try:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

        cmd = f'{prg} -s 4 -o {out_dir} -p .25 {n1k} {n10k} {n100k}'
        print(cmd)
        rv, out = getstatusoutput(cmd)
        assert rv == 0

        assert re.search('1: n1k.fa', out)
        assert re.search('2: n10k.fa', out)
        assert re.search('3: n100k.fa', out)
        assert re.search(
            f'Wrote 27,688 sequences from 3 files to directory "{out_dir}"',
            out)

        assert os.path.isdir(out_dir)

        files = os.listdir(out_dir)
        assert len(files) == 3

        seqs_written = 0
        for file in files:
            seqs_written += len(
                list(SeqIO.parse(os.path.join(out_dir, file), 'fasta')))

        assert seqs_written == 27688
    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)
