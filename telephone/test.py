#!/usr/bin/env python3
"""tests for telephone.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re
import string

prg = "./telephone.py"
fox = '../inputs/fox.txt'
now = '../inputs/now.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match('usage', out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_seed_str():
    """bad seed str value"""

    bad = random_string()
    rv, out = getstatusoutput('{} -s {} {}'.format(prg, bad, fox))
    assert rv > 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_mutation_str():
    """bad mutation str value"""

    bad = random_string()
    rv, out = getstatusoutput('{} -m {} {}'.format(prg, bad, fox))
    assert rv > 0
    assert re.search(f"invalid float value: '{bad}'", out)


# --------------------------------------------------
def test_bad_mutation():
    """bad mutation values"""

    for val in ['-1.0', '10.0']:
        rv, out = getstatusoutput('{} -m {} {}'.format(prg, val, fox))
        assert rv > 0
        assert re.search('--mutations "{}" must be b/w 0 and 1'.format(val),
                         out)


# --------------------------------------------------
def test_for_echo():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput('{} -m 0 "{}"'.format(prg, txt))
    assert rv == 0
    assert out.rstrip() == txt


# --------------------------------------------------
def test_now_cmd_s1():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput('{} -s 1 "{}"'.format(prg, txt))
    assert rv == 0
    expected = """
    Now is B*e time X'r all good mem to come to the ,id of the party.
    """.strip()
    assert out.rstrip() == expected


# --------------------------------------------------
def test_now_cmd_s2_m4():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput('{} -s 2 -m .4 "{}"'.format(prg, txt))
    assert rv == 0
    expected = """
    Nod ie .he(JiFe ?orvalldg/osxmenUt? cxxe.t$PtheOaidWEV:the xa/ty.
    """.strip()
    assert out.rstrip() == expected


# --------------------------------------------------
def test_fox_file_s1():
    """test"""

    rv, out = getstatusoutput('{} --seed 1 {}'.format(prg, fox))
    assert rv == 0
    assert out.rstrip() == "The 'uicq brown *ox jumps over the l-zy dog."


# --------------------------------------------------
def test_fox_file_s2_m6():
    """test"""

    rv, out = getstatusoutput('{} --seed 2 --mutations .6 {}'.format(prg, fox))
    assert rv == 0
    assert out.rstrip() == "V;xvq?ic# E]'Qy x/xdjumFs.o/U? th!Ulv'yrVox."


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
