#!/usr/bin/env python3
"""tests for password.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './password.py'
words = '../inputs/words.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)
    assert os.path.isfile(words)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_file():
    """Dies on bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_num():
    """Dies on bad num"""

    bad = random_string()
    flag = '-n' if random.choice([0, 1]) else '--num'
    rv, out = getstatusoutput(f'{prg} {flag} {bad} {words}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_num_words():
    """Dies on bad num"""

    bad = random_string()
    flag = '-w' if random.choice([0, 1]) else '--num_words'
    rv, out = getstatusoutput(f'{prg} {flag} {bad} {words}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_min_word_len():
    """Dies on bad min_word_len"""

    bad = random_string()
    flag = '-m' if random.choice([0, 1]) else '--min_word_len'
    rv, out = getstatusoutput(f'{prg} {flag} {bad} {words}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_max_word_len():
    """Dies on bad max_word_len"""

    bad = random_string()
    flag = '-m' if random.choice([0, 1]) else '--max_word_len'
    rv, out = getstatusoutput(f'{prg} {flag} {bad} {words}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_seed():
    """Dies on bad seed"""

    bad = random_string()
    flag = '-s' if random.choice([0, 1]) else '--seed'
    rv, out = getstatusoutput(f'{prg} {flag} {bad} {words}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_defaults():
    """Test"""

    rv, out = getstatusoutput(f'{prg} -s 1 {words}')
    assert rv == 0
    assert out.strip() == '\n'.join([
        'DuniteBoonLociDefat', 'WegaTitmalUnplatSatire', 'IdeanClipsVitiArriet'
    ])


# --------------------------------------------------
def test_num():
    """Test"""

    rv, out = getstatusoutput(f'{prg} -s 1 -n 1 {words}')
    assert rv == 0
    assert out.strip() == 'DuniteBoonLociDefat'


# --------------------------------------------------
def test_num_words():
    """Test"""

    rv, out = getstatusoutput(f'{prg} -s 1 -w 2 {words}')
    assert rv == 0
    assert out.strip() == '\n'.join(['DuniteBoon', 'LociDefat', 'WegaTitmal'])


# --------------------------------------------------
def test_min_word_len():
    """Test"""

    rv, out = getstatusoutput(f'{prg} -s 1 -m 5 {words}')
    assert rv == 0
    assert out.strip() == '\n'.join([
        'CarneyRapperWabenoUndine', 'BabaiFarerBugleOnlepy',
        'UnbittMinnyNatalSkanda'
    ])


# --------------------------------------------------
def test_max_word_len():
    """Test"""

    rv, out = getstatusoutput(f'{prg} -s 1 -x 10 {words}')
    assert rv == 0
    assert out.strip() == '\n'.join([
        'DicemanYardwandBoeberaKismetic', 'CubiculumTilsitSnowcapSuer',
        'ProhasteHaddockChristmasyTenonitis'
    ])


# --------------------------------------------------
def test_l33t():
    """Test"""

    rv, out = getstatusoutput(f'{prg} -s 1 -l {words}')
    assert rv == 0
    assert out.strip() == '\n'.join([
        'DUn1Teb0onloCiDef4T/', 'Weg4TiTm@LuNPl4T54+1r3_',
        'iD3@Ncl1P5v1+14rrie+/'
    ])


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
