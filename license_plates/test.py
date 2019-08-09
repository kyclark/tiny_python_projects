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
ABC1234 OK
ABC12E4 OK
ABC1734 OK
ABC17E4 OK
ABCI234 OK
ABCI2E4 OK
ABCI734 OK
ABCI7E4 OK
    """.strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_accept_02():
    """runs"""

    out = getoutput('{} 123456'.format(prg))
    expected = """
plate = "123456"
regex = "^[1I][27][3E]4[5S]6$"
123456 OK
1234S6 OK
12E456 OK
12E4S6 OK
173456 OK
1734S6 OK
17E456 OK
17E4S6 OK
I23456 OK
I234S6 OK
I2E456 OK
I2E4S6 OK
I73456 OK
I734S6 OK
I7E456 OK
I7E4S6 OK
    """.strip()
    assert out.strip() == expected
