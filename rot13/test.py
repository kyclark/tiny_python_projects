#!/usr/bin/env python3
"""tests for rot13.py"""

import os
import random
import string
from subprocess import getstatusoutput

prg = "./rot13.py"
sonnet = 'files/sonnet-29.txt'
fox = 'files/fox.txt'


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))

        if flag == '':
            assert rv > 0
        else:
            assert rv == 0

        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_text():
    """command-line text"""

    rv1, out1 = getstatusoutput('{} {}'.format(prg, 'AbcD'))
    assert rv1 == 0
    assert out1 == 'NopQ'

    rv2, out2 = getstatusoutput('{} -s 3 {}'.format(prg, 'AbcD'))
    assert rv2 == 0
    assert out2 == 'DefG'

    rv3, out3 = getstatusoutput('{} {} --shift -5'.format(prg, 'AbcD'))
    assert rv3 == 0
    assert out3 == 'VwxY'


# --------------------------------------------------
def test_file():
    """file input"""

    for in_file in [fox, sonnet]:
        rv, out = getstatusoutput('{} {}'.format(prg, in_file))
        expected = open(in_file + '.out').read()
        assert rv == 0
        assert out.rstrip() == expected.rstrip()


# --------------------------------------------------
def test_roundtrip_text():
    """round trip"""

    shift = random.randint(-10, 10)
    unshift = shift * -1
    text = ' '.join([random_string() for _ in range(random.randint(5, 10))])
    rv, out = getstatusoutput('{} -s {} "{}" | {} --shift {} -'.format(
        prg, shift, text, prg, unshift))
    assert rv == 0
    assert out.rstrip() == text.rstrip()


# --------------------------------------------------
def test_roundtrip_file():
    """round trip file input"""

    for in_file in [fox, sonnet]:
        shift = random.randint(-10, 10)
        unshift = shift * -1
        rv, out = getstatusoutput('{} --shift {} "{}" | {} -s {} -'.format(
            prg, shift, in_file, prg, unshift))
        expected = open(in_file).read()
        assert rv == 0
        assert out.rstrip() == expected.rstrip()
