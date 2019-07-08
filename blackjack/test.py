#!/usr/bin/env python3
"""tests for blackjack.py"""

import os
import re
import random
from subprocess import getstatusoutput, getoutput

prg = './blackjack.py'


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
def test_play01():
    out = getoutput('{} {} 42'.format(prg, seed_flag()))
    expected = """
Dealer [17]: S8 D9
Player [ 4]: D2 S2
Dealer should hit.
Player should hit.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play02():
    out = getoutput('{} {} 7'.format(prg, seed_flag()))
    expected = """
Dealer [ 4]: SA D3
Player [18]: C8 CQ
Dealer should hit.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play03():
    out = getoutput('{} {} 1 {}'.format(prg, seed_flag(), player_hits_flag()))
    expected = """
Dealer [15]: HJ S5
Player [14]: S9 DA C4
Dealer should hit.
Player should hit.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play04():
    out = getoutput('{} {} 5 {}'.format(prg, seed_flag(), player_hits_flag()))
    expected = """
Dealer [ 5]: C4 CA
Player [25]: D10 D9 D6
Player busts! You lose, loser!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play05():
    out = getoutput('{} {} 15 {}'.format(prg, seed_flag(), player_hits_flag()))
    expected = """
Dealer [19]: S10 D9
Player [21]: C10 H8 S3
Player wins. You probably cheated.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play06():
    out = getoutput('{} {} 92 {}'.format(prg, seed_flag(), dealer_hits_flag()))
    expected = """
Dealer [10]: H8 HA DA
Player [20]: H10 HJ
Dealer should hit.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play07():
    out = getoutput('{} {} 16 {}'.format(prg, seed_flag(), dealer_hits_flag()))
    expected = """
Dealer [21]: H5 C6 H10
Player [20]: CJ DK
Dealer wins!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play08():
    out = getoutput('{} -s 33 {} {}'.format(prg, player_hits_flag(),
                                            dealer_hits_flag()))
    expected = """
Dealer [17]: SJ C2 H5
Player [17]: HJ D2 C5
Dealer should hit.
Player should hit.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play09():
    out = getoutput('{} -s 15 {} {}'.format(prg, player_hits_flag(),
                                            dealer_hits_flag()))
    expected = """
Dealer [29]: S10 D9 SJ
Player [21]: C10 H8 S3
Dealer busts.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play10():
    out = getoutput('{} -s 19 {} {}'.format(prg, player_hits_flag(),
                                            dealer_hits_flag()))
    expected = """
Dealer [21]: S3 S8 SQ
Player [20]: D5 H8 H7
Dealer wins!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play11():
    out = getoutput('{} -s 31 {} {}'.format(prg, player_hits_flag(),
                                            dealer_hits_flag()))
    expected = """
Dealer [ 7]: H5 DA SA
Player [28]: S10 S8 CQ
Player busts! You lose, loser!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play12():
    out = getoutput('{} -s 77 {} {}'.format(prg, player_hits_flag(),
                                            dealer_hits_flag()))
    expected = """
Dealer [15]: C4 SQ DA
Player [21]: DQ C8 C3
Player wins. You probably cheated.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def seed_flag():
    return '-s' if random.randint(0, 1) else '--seed'


# --------------------------------------------------
def player_hits_flag():
    return '-p' if random.randint(0, 1) else '--player_hits'


# --------------------------------------------------
def dealer_hits_flag():
    return '-d' if random.randint(0, 1) else '--dealer_hits'
