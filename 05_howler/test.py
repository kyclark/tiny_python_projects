#!/usr/bin/env python3
"""tests for howler.py"""

import os
from posixpath import basename
import re
import random
import string
from subprocess import getstatusoutput, getoutput

prg = "./howler.py"


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def out_flag():
    """Either -o or --outdir"""

    return "-o" if random.randint(0, 1) else "--outdir"


# --------------------------------------------------
def lowercase_flag():
    """Either -l or --lowercase"""

    return "-l" if random.randint(0, 1) else "--lowercase"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{prg} {flag}")
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_text_stdout():
    """Test STDIN/STDOUT"""

    out = getoutput(f'{prg} "foo bar baz"')
    assert out.strip() == "FOO BAR BAZ"


# --------------------------------------------------
def test_text_stdout_lowercase():
    """Test STDIN/STDOUT lowercase"""

    out = getoutput(f'{prg} {lowercase_flag()} "FOO BAR BAZ"')
    assert out.strip() == "foo bar baz"


# --------------------------------------------------
def test_file():
    """Test file in/out"""

    files = ['fox.txt', '../inputs/the-bustle.txt', '../inputs/sonnet-29.txt', 'test-outs-lowercase/preamble.txt']
    out_directory = random_string()
    expected_directory = 'test-outs'
    try:
        if not os.path.isdir(out_directory):
            os.mkdir(out_directory)
        out = getoutput(f"{prg} {out_flag()} {out_directory} {' '.join(files)}")
        assert out.strip() == ""
        for expected_file in files:
            basename = os.path.basename(expected_file)
            produced = open(os.path.join(out_directory, basename)).read().rstrip()
            os.remove(os.path.join(out_directory, basename))
            expected = open(os.path.join(expected_directory, basename)).read().strip()
            assert expected == produced
    finally:
        if os.path.isdir(out_directory):
            os.rmdir(out_directory)


# --------------------------------------------------
def test_file_lowercase():
    """Test file in/out lowercase"""

    files = ['fox.txt', '../inputs/the-bustle.txt', '../inputs/sonnet-29.txt', 'test-outs-lowercase/preamble.txt']
    out_directory = random_string()
    expected_directory = 'test-outs-lowercase'
    try:
        if not os.path.isdir(out_directory):
            os.mkdir(out_directory)
        out = getoutput(f"{prg} {out_flag()} {out_directory} {lowercase_flag()} {' '.join(files)}")
        assert out.strip() == ""
        for expected_file in files:
            basename = os.path.basename(expected_file)
            produced = open(os.path.join(out_directory, basename)).read().rstrip()
            os.remove(os.path.join(out_directory, basename))
            expected = open(os.path.join(expected_directory, basename)).read().strip()
            assert expected == produced
    finally:
        if os.path.isdir(out_directory):
            os.rmdir(out_directory)


