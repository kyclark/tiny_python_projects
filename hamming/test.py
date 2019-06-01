#!/usr/bin/env python3
"""tests for hamm.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re
import string
import hamm

prg = "./hamm.py"


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_usage():
    """usage"""
    rv1, out1 = getstatusoutput(prg)
    assert rv1 > 0
    assert re.match("usage", out1, re.IGNORECASE)

    rv2, out2 = getstatusoutput('{} fox.txt'.format(prg))
    assert rv2 > 0
    assert re.match("usage", out2, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input():
    """bad_input"""
    bad_file = random_string()
    rv, out = getstatusoutput('{} {} {}'.format(prg, 'fox.txt', bad_file))
    assert rv > 0
    assert out == '"{}" is not a file'.format(bad_file)


# --------------------------------------------------
def test_dist():
    """dist ok"""
    tests = [('foo', 'boo', '1'), ('foo', 'faa', '2'), ('foo', 'foobar', '3'),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              '9'), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', '10')]

    for s1, s2, n in tests:
        d = hamm.dist(s1, s2)
        assert d == int(n)


# --------------------------------------------------
def test_runs_ok():
    log = '.log'

    for f1, f2, n in [
        ('fox.txt', 'fox.txt', '0'),
        ('american.txt', 'british.txt', '28'),
        ('american.txt', 'american.txt', '0'),
        ('sample1.fa', 'sample2.fa', '6'),
    ]:
        for debug in [True, False]:
            if os.path.isfile(log):
                os.remove(log)

            rv, out = getstatusoutput('{} {} {} {}'.format(
                prg, '-d' if debug else '', f1, f2))

            if debug:
                assert os.path.isfile(log)

            assert rv == 0
            assert out.rstrip() == n


# --------------------------------------------------
def test_log():
    f1 = 'american.txt'
    f2 = 'british.txt'
    log = '.log'

    if os.path.isfile(log):
        os.remove(log)

    rv, out = getstatusoutput('{} -d {} {}'.format(prg, f1, f2))

    assert os.path.isfile(log)

    lines = open(log).read().splitlines()
    assert len(lines) == 64

    not_zero = list(filter(lambda l: l.split()[-1] != '0', lines))
    assert len(not_zero) == 16
