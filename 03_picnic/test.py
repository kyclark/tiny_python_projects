#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

prg = './picnic.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_one():
    """one item"""

    arg = 'chips'
    out = getoutput(f'{prg} {arg}')
    assert out.strip() == 'You are bringing chips.'

# --------------------------------------------------
def test_one_separator():
    """one item with separator"""

    arg = 'chips --listseparator ";"'
    out = getoutput(f'{prg} {arg}')
    assert out.strip() == 'You are bringing chips.'


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(f'{prg} soda "french fries"')
    assert out.strip() == 'You are bringing soda and french fries.'

# --------------------------------------------------
def test_two_separator():
    """two items with separator"""

    out = getoutput(f'{prg} soda "french fries" -l ";"')
    assert out.strip() == 'You are bringing soda and french fries.'


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} {arg}')
    expected = ('You are bringing potato chips, coleslaw, '
                'cupcakes, and French silk pie.')
    assert out.strip() == expected

# --------------------------------------------------
def test_more_than_two_separator():
    """more than two items with separator"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} {arg} --listseparator ";"')
    expected = ('You are bringing potato chips; coleslaw; '
                'cupcakes; and French silk pie.')
    assert out.strip() == expected

# --------------------------------------------------
def test_more_than_two_no_oxford_comma():
    """more than two items and no Oxford comma"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} {arg} --omitoxfordcomma')
    expected = ('You are bringing potato chips, coleslaw, '
                'cupcakes and French silk pie.')
    assert out.strip() == expected


# --------------------------------------------------
def test_more_than_two_no_oxford_comma_separator():
    """more than two items and no Oxford comma with separator"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f'{prg} {arg} --omitoxfordcomma -l ";"')
    expected = ('You are bringing potato chips; coleslaw; '
                'cupcakes and French silk pie.')
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f'{prg} -s soda candy')
    assert out.strip() == 'You are bringing candy and soda.'


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'{prg} {arg} --sorted')
    expected = ('You are bringing apples, bananas, cherries, and dates.')
    assert out.strip() == expected

# --------------------------------------------------
def test_more_than_two_sorted_no_oxford_comma():
    """more than two items sorted output and no Oxford comma"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'{prg} {arg} --sorted -o')
    expected = ('You are bringing apples, bananas, cherries and dates.')
    assert out.strip() == expected

# --------------------------------------------------
def test_more_than_two_sorted_no_oxford_comma_separator():
    """more than two items sorted output and no Oxford comma with separator"""

    arg = 'bananas apples dates cherries'
    out = getoutput(f'{prg} {arg} --sorted -o -l ":"')
    expected = ('You are bringing apples: bananas: cherries and dates.')
    assert out.strip() == expected
