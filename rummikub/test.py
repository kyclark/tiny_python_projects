#!/usr/bin/env python3
"""tests for rummikub.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput

prg = './rummikub.py'


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
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_nothing_found():
    """runs"""

    for seed in [0, 10]:
        rv, out = getstatusoutput('{} -s {}'.format(prg, seed))
        assert rv == 0
        assert out == 'Found no sets.'


# --------------------------------------------------
def test_runs1():
    """runs"""

    rv, out = getstatusoutput('{} --seed 1'.format(prg))
    assert rv == 0
    sets = parse_sets(out)
    assert len(sets) == 1
    assert ('B3 K3 Y3') in sets


# --------------------------------------------------
def test_runs2():
    """runs"""

    rv, out = getstatusoutput('{} -s2'.format(prg))
    print(out)
    assert rv == 0
    sets = parse_sets(out)
    assert len(sets) == 3
    assert ('K8 K9 K10') in sets
    assert ('K9 K10 K11') in sets
    assert ('K8 K9 K10 K11') in sets


# --------------------------------------------------
def test_runs5():
    """runs"""

    rv, out = getstatusoutput('{} -s 5'.format(prg))
    print(out)
    assert rv == 0
    sets = parse_sets(out)
    assert len(sets) == 5
    assert ('K11 K12 K13') in sets
    assert ('B2 B3 B4') in sets
    assert ('B3 B4 B5') in sets
    assert ('B2 K2 Y2') in sets
    assert ('B2 B3 B4 B5') in sets


# --------------------------------------------------
def parse_sets(out):
    """parse_sets"""

    sets = list()
    regex = re.compile(r'\d+:\s+(.+)')
    for line in out.splitlines():
        match = regex.search(line)
        if match:
            sets.append(match.group(1))

    return sets
