#!/usr/bin/env python3
"""tests for rot13.py"""

import os
from subprocess import getstatusoutput

prg = "./rot13.py"
sonnet = '../inputs/sonnet-29.txt'
fox = '../inputs/fox.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_text():
    """command-line text"""

    rv1, out1 = getstatusoutput('{} {}'.format(prg, 'AbcD'))
    assert rv1 == 0
    assert out1 == 'NOPQ'

    rv2, out2 = getstatusoutput('{} -s 3 {}'.format(prg, 'AbcD'))
    assert rv2 == 0
    assert out2 == 'DEFG'

    rv3, out3 = getstatusoutput('{} {} --shift -5'.format(prg, 'AbcD'))
    assert rv3 == 0
    assert out3 == 'VWXY'


# --------------------------------------------------
def run_file(file, args, expected):
    """file input"""

    assert os.path.isfile(file)

    expected = os.path.join('test-out', expected)
    assert os.path.isfile(expected)

    rv, out = getstatusoutput('{} {} {}'.format(prg, args, file))
    assert rv == 0
    assert out.rstrip() == open(expected).read().rstrip()


# --------------------------------------------------
def test_fox():
    """fox"""

    run_file(fox, '-S 1', 'fox.txt.out.S1')
    run_file(fox, '-S 2 -w 30', 'fox.txt.out.S2.w30')
    run_file(fox, '-S 3 -p 5 -w 25', 'fox.txt.out.S3.p5.w25')
    run_file(fox, '-S 4 -s 5', 'fox.txt.out.S4.s5')


# --------------------------------------------------
def test_sonnet():
    """sonnet 29"""

    run_file(sonnet, '-S 1', 'sonnet.txt.out.S1')
    run_file(sonnet, '-S 2 -w 30', 'sonnet.txt.out.S2.w30')
    run_file(sonnet, '-S 3 -p 5 -w 25', 'sonnet.txt.out.S3.p5.w25')
    run_file(sonnet, '-S 4 -s 5', 'sonnet.txt.out.S4.s5')


# --------------------------------------------------
def test_stdin():
    """stdin"""

    expected = open(os.path.join('test-out/fox.txt.out.S1')).read().rstrip()
    rv, out = getstatusoutput('{} -S 1 < {}'.format(prg, fox))
    assert rv == 0
    assert out.rstrip() == expected
