#!/usr/bin/env python3
"""tests for addressbook.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput

prg = "./addressbook.py"
mary_lebow = "Mary\ Lebow"
uncle_paul = "Uncle\ Paul"
tom_upbridge = "Tom\ Upbridge"


# --------------------------------------------------
def file_flag():
    """Either -f or --file"""

    return "-f" if random.randint(0, 1) else "--file"


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
        rv, out = getstatusoutput(f"{prg} {flag}")
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file():
    """Test for bad --file"""

    bad = random_string()
    letter = random.choice(string.ascii_lowercase)
    rv, out = getstatusoutput(f"{prg} {letter} -f {bad}")
    assert rv != 0
    expected = f"No such file or directory: '{bad}'"
    assert re.search(expected, out)


# --------------------------------------------------
def test_mary():
    """Test for 'Mary Lebow'"""

    rv, out = getstatusoutput(f"{prg} {mary_lebow}")
    assert rv == 0
    expected = "lebow@example.com\n619 332-3452"
    assert out.strip() == expected


# --------------------------------------------------
def test_tom():
    """Test for 'Tom Upbridge'"""

    rv, out = getstatusoutput(f'{prg} {tom_upbridge}')
    assert rv == 0
    expected = "tup@example.com\n118 885-6687"
    assert out.strip() == expected


# --------------------------------------------------
def test_no_uncle_paul():
    """Test for 'Uncle Paul' (not present)"""

    rv, out = getstatusoutput(f'{prg} {uncle_paul}')
    assert rv == 0
    expected = 'I do not have an entry for "Uncle Paul".'
    assert out.strip() == expected


# --------------------------------------------------
def test_alternate():
    """Test for 'Uncle Paul' from 'alternate.json'"""

    rv, out = getstatusoutput(f"{prg} {uncle_paul} -f alternate.json")
    assert rv == 0
    expected = 'pminor@example.com\n688 397-2232'
    assert out.strip() == expected
