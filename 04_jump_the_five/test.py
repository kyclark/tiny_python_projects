#!/usr/bin/env python3
"""tests for jump.py"""

import os
from subprocess import getstatusoutput

prg = './jump.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """test"""

    rv, out = getstatusoutput(f'{prg} 123-456-7890')
    assert rv == 0
    assert out == '987-604-3215'


# --------------------------------------------------
def test_02():
    """test"""

    rv, out = getstatusoutput(f'{prg} "That number to call is 098-765-4321."')
    assert rv == 0
    assert out.rstrip() == 'That number to call is 512-340-6789.'

# --------------------------------------------------
def test_03():
    """test convert to string"""

    rv, out = getstatusoutput(f'{prg} 123-456-7890 -s')
    assert rv == 0
    assert out == 'one two three - four five six - seven eight nine zero '


# --------------------------------------------------
def test_04():
    """test convert to string"""

    rv, out = getstatusoutput(f'{prg} --substitutestring "That number to call is 098-765-4321."')
    assert rv == 0
    assert out.rstrip() == 'That number to call is zero nine eight - seven six five - four three two one .'
