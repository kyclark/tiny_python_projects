#!/usr/bin/env python3
"""Tests for piggy.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput
from shutil import rmtree

prg = './piggy.py'
nobody = '../inputs/nobody.txt'
gettysburg = '../inputs/gettysburg.txt'
decl = '../inputs/usdeclar.txt'


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
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_bad_input():
    """Test bad"""

    bad = random_string()
    rv, out = getstatusoutput('{} {}'.format(prg, bad))
    assert rv != 0
    assert re.search("No such file or directory: '{}'".format(bad), out)


# --------------------------------------------------
def run(file):
    """Run any one file"""

    basename = os.path.basename(file)
    flip = random.choice([True, False])
    out_flag = '-o ' if flip else '--outdir '
    out_dir = random_string() if flip else ''

    if out_dir and os.path.isdir(out_dir):
        rmtree(out_dir)

    try:
        out_dir_arg = out_flag + out_dir if out_dir else ''
        rv, _ = getstatusoutput('{} {} "{}"'.format(prg, out_dir_arg, file))

        assert rv == 0

        out_path = os.path.join(out_dir or 'out-yay', basename)
        assert os.path.isfile(out_path)

        prg_out = open(out_path).read()
        expected_file = os.path.join('test-outs', basename)
        expected_out = open(expected_file).read()
        assert expected_out == prg_out

    finally:
        if out_dir and os.path.isdir(out_dir):
            rmtree(out_dir)


# --------------------------------------------------
def test_nobody():
    """Test nobody"""

    run(nobody)


# --------------------------------------------------
def test_gettysburg():
    """Test gettysburg"""

    run(gettysburg)


# --------------------------------------------------
def test_decl():
    """Test Decl of Ind"""

    run(decl)


# --------------------------------------------------
def test_all():
    """Test multiple"""

    out_dir = random_string()

    if os.path.isdir(out_dir):
        rmtree(out_dir)

    try:
        all_files = [gettysburg, nobody, decl]
        rv, out = getstatusoutput('{} --outdir {} {}'.format(
            prg, out_dir, ' '.join(all_files)))

        assert rv == 0

        out = out.split('\n')
        assert len(out) == 4
        assert out[-1] == 'Done, wrote 3 files to "{}".'.format(out_dir)

        assert os.path.isdir(out_dir)

        out_files = os.listdir(out_dir)
        assert len(out_files) == 3

        for file in all_files:
            basename = os.path.basename(file)
            out_path = os.path.join(out_dir, basename)
            assert os.path.isfile(out_path)

            prg_out = open(out_path).read()
            expected_file = os.path.join('test-outs', basename)
            expected_out = open(expected_file).read()
            assert expected_out == prg_out

    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)
