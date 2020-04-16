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
        out = getoutput(f'{prg} {flag}')
        assert re.match('usage', out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_seed_str():
    """bad seed str value"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -s {bad} {fox}')
    assert rv > 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_mutation_str():
    """bad mutation str value"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -m {bad} {fox}')
    assert rv > 0
    assert re.search(f"invalid float value: '{bad}'", out)


# --------------------------------------------------
def test_bad_mutation():
    """bad mutation values"""

    for val in ['-1.0', '10.0']:
        rv, out = getstatusoutput(f'{prg} -m {val} {fox}')
        assert rv > 0
        assert re.search(f'--mutations "{val}" must be between 0 and 1', out)


# --------------------------------------------------
def test_for_echo():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(f'{prg} -m 0 "{txt}"')
    assert rv == 0
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{txt}"'


# --------------------------------------------------
def test_now_cmd_s1():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(f'{prg} -s 1 "{txt}"')
    assert rv == 0
    expected = """
    Now is Ege time [dr all good me- to come to the jid of the party.
    """.strip()
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_now_cmd_s2_m4():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(f'{prg} -s 2 -m .4 "{txt}"')
    assert rv == 0
    expected = """
    No$ i% khefMiIe sor@all$glo<BmenYts cAAeltaTtheSaid[HYnthe Aalty.
    """.strip()
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_fox_file_s1():
    """test"""

    rv, out = getstatusoutput(f'{prg} --seed 1 {fox}')
    assert rv == 0
    txt = open(fox).read().rstrip()
    expected = "The duic: brown hox jumps over the lkzy dog."
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_fox_file_s2_m6():
    """test"""

    rv, out = getstatusoutput(f'{prg} --seed 2 --mutations .6 {fox}')
    assert rv == 0
    txt = open(fox).read().rstrip()
    expected = "ZoA@qric` HwdTB Alx$jumIslolXs th^Yl?dy<YoA."
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
