#!/usr/bin/env python3
"""tests for blackjack.py"""

import re
import random
from subprocess import getstatusoutput, getoutput

prg = './blackjack.py'


# --------------------------------------------------
def seed_flag():
    return '-s' if random.randint(0, 1) else '--seed'

# --------------------------------------------------
def player_hits_flag():
    return '-p' if random.randint(0, 1) else '--player_hits'


# --------------------------------------------------
def dealer_hits_flag():
    return '-d' if random.randint(0, 1) else '--dealer_hits'


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
D [17]: ♠8 ♦9
P [ 4]: ♦2 ♠2
Dealer should hit.
Player should hit.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play02():
    out = getoutput('{} {} 7'.format(prg, seed_flag()))
    expected = """
D [ 4]: ♠A ♦3
P [18]: ♣8 ♣Q
Dealer should hit.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play03():
    out = getoutput('{} {} 1 {}'.format(prg, seed_flag(), player_hits_flag()))
    expected = """
D [15]: ♥J ♠5
P [14]: ♠9 ♦A ♣4
Dealer should hit.
Player should hit.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play04():
    out = getoutput('{} {} 5 {}'.format(prg, seed_flag(), player_hits_flag()))
    expected = """
D [ 5]: ♣4 ♣A
P [25]: ♦10 ♦9 ♦6
Player busts! You lose, loser!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play05():
    out = getoutput('{} {} 15 {}'.format(prg, seed_flag(), player_hits_flag()))
    expected = """
D [19]: ♠10 ♦9
P [21]: ♣10 ♥8 ♠3
Player wins. You probably cheated.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play06():
    out = getoutput('{} {} 92 {}'.format(prg, seed_flag(), dealer_hits_flag()))
    expected = """
D [10]: ♥8 ♥A ♦A
P [20]: ♥10 ♥J
Dealer should hit.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play07():
    out = getoutput('{} {} 16 {}'.format(prg, seed_flag(), dealer_hits_flag()))
    expected = """
D [21]: ♥5 ♣6 ♥10
P [20]: ♣J ♦K
Dealer wins!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play08():
    out = getoutput('{} -s 33 {} {}'.format(prg, player_hits_flag(),
                                            dealer_hits_flag()))
    expected = """
D [17]: ♠J ♣2 ♥5
P [17]: ♥J ♦2 ♣5
Dealer should hit.
Player should hit.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play09():
    out = getoutput('{} -s 15 {} {}'.format(prg, player_hits_flag(),
                                            dealer_hits_flag()))
    expected = """
D [29]: ♠10 ♦9 ♠J
P [21]: ♣10 ♥8 ♠3
Dealer busts.
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play10():
    out = getoutput('{} -s 19 {} {}'.format(prg, player_hits_flag(),
                                            dealer_hits_flag()))
    expected = """
D [21]: ♠3 ♠8 ♠Q
P [20]: ♦5 ♥8 ♥7
Dealer wins!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play11():
    out = getoutput('{} -s 31 {} {}'.format(prg, player_hits_flag(),
                                            dealer_hits_flag()))
    expected = """
D [ 7]: ♥5 ♦A ♠A
P [28]: ♠10 ♠8 ♣Q
Player busts! You lose, loser!
""".strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_play12():
    out = getoutput('{} -s 77 {} {}'.format(prg, player_hits_flag(),
                                            dealer_hits_flag()))
    expected = """
D [15]: ♣4 ♠Q ♦A
P [21]: ♦Q ♣8 ♣3
Player wins. You probably cheated.
""".strip()
    assert out.strip() == expected
