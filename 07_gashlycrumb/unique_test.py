#!/usr/bin/env python3
"""tests for unique.py"""

import os
import re
import random
import string
from subprocess import getoutput, getstatusoutput, run

prg = "./unique.py"
helper = "./unique_helper"
empty = '../inputs/empty.txt'
one_line = '../inputs/now.txt'
two_lines = '../inputs/out.txt'
fox = '../inputs/fox.txt'
sonnet = '../inputs/sonnet-29.txt'
long_sonnet = '../inputs/sonnets.txt'


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

for flag in ["-h", "--help"]:
    cp = run([f"{prg}", f"{flag}"], capture_output=True, text=True)
    assert cp.returncode == 0
    assert re.match("usage", cp.stdout, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file():
    """Test for bad file"""

    bad = random_string()
    letter = random.choice(string.ascii_lowercase)
    cp = run([f"{prg}", f"{bad}"], capture_output=True, text=True)
    assert cp.returncode != 0
    expected = f"No such file or directory: '{bad}'"
    assert re.search(expected, cp.stderr)


# --------------------------------------------------
def test_empty():
    """Test for empty file'"""

    cp = run([f"{prg}", f"{empty}"], capture_output=True, text=True)
    assert cp.returncode == 0
    expected = run([f"{helper}", "<", f"{empty}"], capture_output=True, text=True, shell=True)
    assert cp.stdout.strip() == expected.stdout.strip()


# --------------------------------------------------
def test_one():
    """Test for one line file'"""

    rv, out = getstatusoutput(f'{prg} {one_line}')
    assert rv == 0
    expected = getoutput(f'{helper} < {one_line}')
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_two():
    """Test for two line file"""

    rv, out = getstatusoutput(f'{prg} {two_lines}')
    assert rv == 0
    expected = getoutput(f'{helper} < {two_lines}')
    assert out.strip() == expected.strip()

# --------------------------------------------------
def test_fox():
    """Test for fox"""

    rv, out = getstatusoutput(f'{prg} {fox}')
    assert rv == 0
    expected = getoutput(f'{helper} < {fox}')
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_short():
    """Test for short file"""

    rv, out = getstatusoutput(f"{prg} {sonnet}")
    assert rv == 0
    expected = getoutput(f'{helper} < {sonnet}')
    assert out.strip() == expected.strip()

# --------------------------------------------------
def test_long():
    """Test for long file"""

    rv, out = getstatusoutput(f"{prg} {long_sonnet}")
    assert rv == 0
    expected = getoutput(f'{helper} < {long_sonnet}')
    assert out.strip() == expected.strip()
