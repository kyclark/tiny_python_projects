#!/usr/bin/env python3
"""tests for order.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './order.py'


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
def test_nothing():
    """nothing"""

    rv, out = getstatusoutput(f'{prg}')
    assert rv == 0
    assert out.rstrip() == 'You have failed me for the last time, Commander.'


# --------------------------------------------------
def test_one_element():
    """one element"""

    rv, out = getstatusoutput(f'{prg} foo')
    assert rv == 0
    assert out.rstrip() == '  1: foo'


# --------------------------------------------------
def test_two_elements():
    """two elements"""

    rv, out = getstatusoutput(f'{prg} foo bar')
    assert rv == 0
    assert out.rstrip() == '  1: bar\n  2: foo'


# --------------------------------------------------
def test_two_elements_reversed():
    """two elements reversed"""

    rev = '-r' if random.choice([0, 1]) else '--reverse'
    rv, out = getstatusoutput(f'{prg} foo bar {rev}')
    assert rv == 0
    assert out.rstrip() == '  1: foo\n  2: bar'


# --------------------------------------------------
def test_more():
    """MOAR"""

    items = 'one two three four five six seven eight nine ten zero'
    rv, out = getstatusoutput(f'{prg} {items}')
    assert rv == 0
    expected = '\n'.join([
        '  1: eight', '  2: five', '  3: four', '  4: nine', '  5: one',
        '  6: seven', '  7: six', '  8: ten', '  9: three', ' 10: two',
        ' 11: zero'
    ])
    assert out.rstrip() == expected


# --------------------------------------------------
def test_more_reverse():
    """MOAR"""

    items = 'one two three four five six seven eight nine ten zero'
    rev = '-r' if random.choice([0, 1]) else '--reverse'
    rv, out = getstatusoutput(f'{prg} {items} {rev}')
    assert rv == 0
    expected = '\n'.join([
        '  1: zero', '  2: two', '  3: three', '  4: ten', '  5: six',
        '  6: seven', '  7: one', '  8: nine', '  9: four', ' 10: five',
        ' 11: eight'
    ])
    assert out.rstrip() == expected
