#!/usr/bin/env python3
"""tests for bacronym.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput

prg = './bacronym.py'


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
def test_bad_acronym():
    """bad acronym"""

    bad1 = ''.join(random.sample(string.digits, k=1))
    bad2 = random.choice(string.ascii_letters)
    err = 'Acronym "{}" must be >1 in length, only use letters'

    for bad in [bad1, bad2]:
        rv, out = getstatusoutput('{} "{}"'.format(prg, bad))
        assert rv != 0
        assert re.search(err.format(bad), out)


# --------------------------------------------------
def test_bad_num():
    """bad --num"""

    bad = random.choice(range(-10, 1))
    rv, out = getstatusoutput('{} -n {} AAA'.format(prg, bad))
    assert rv != 0
    assert re.search('--num "{}" must be > 0'.format(bad), out)


# --------------------------------------------------
def test_bad_wordlist():
    """bad --wordlist"""

    bad = random_string()
    rv, out = getstatusoutput('{} -w {} AAA'.format(prg, bad))
    assert rv != 0
    assert re.search("No such file or directory: '{}'".format(bad), out)

# --------------------------------------------------
def test_play01():
    """test"""

    out = getoutput('{} --seed 9 -n 1 MIB'.format(prg))
    expected = """
MIB =
 - Miseducate Interparliamentary Bethlehemite
""".strip()

    assert out.strip() == expected

# --------------------------------------------------
def test_play02():
    """test"""

    out = getoutput('{} -s 1 FBI'.format(prg))
    expected = """
FBI =
 - Fecundity Brokage Imitant
 - Figureless Basketmaking Ismailite
 - Frumpery Bonedog Irregardless
 - Foxily Blastomyces Inedited
 - Fastland Bouncingly Idiospasm
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play03():
    """test"""

    out = getoutput('{} --seed 2 --num 3 FBI'.format(prg))
    expected = """
FBI =
 - Fanaticism Bark Impecuniary
 - Flapper Bedlids Instinctively
 - Fightingly Buckstay Inelaborated
""".strip()
    assert out.strip() == expected

# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
