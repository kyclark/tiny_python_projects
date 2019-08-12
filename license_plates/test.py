#!/usr/bin/env python3
"""tests for license.py"""

import os
import re
from subprocess import getstatusoutput, getoutput

prg = './license.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_accept_01():
    """runs"""

    out = getoutput('{} ABC1234'.format(prg))
    expected = """
plate = "ABC1234"
regex = "^ABC[1I][27][3E]4$"
ABC1234 Match
ABC12E4 Match
ABC1734 Match
ABC17E4 Match
ABCI234 Match
ABCI2E4 Match
ABCI734 Match
ABCI7E4 Match
    """.strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_accept_02():
    """runs"""

    out = getoutput('{} 123456'.format(prg))
    expected = """
plate = "123456"
regex = "^[1I][27][3E]4[5S]6$"
123456 Match
1234S6 Match
12E456 Match
12E4S6 Match
173456 Match
1734S6 Match
17E456 Match
17E4S6 Match
I23456 Match
I234S6 Match
I2E456 Match
I2E4S6 Match
I73456 Match
I734S6 Match
I7E456 Match
I7E4S6 Match
    """.strip()
    assert out.strip() == expected
