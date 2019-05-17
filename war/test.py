#!/usr/bin/env python3
"""tests for war.py"""

import re
import random
from subprocess import getstatusoutput, getoutput

prg = './war.py'


# --------------------------------------------------
def seed_flag():
    return '-s' if random.randint(0, 1) else '--seed'

# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_play01():
    out = getoutput('{} {} 1'.format(prg, seed_flag()))
    expected = """
 ♠9  ♥J P2
 ♦A  ♠5 P1
 ♣4  ♠8 P2
 ♥6  ♥3 P1
 ♥5  ♦3 P1
 ♣K ♣10 P1
 ♠7  ♦7 WAR!
 ♠2  ♦4 P2
 ♥2 ♠10 P2
 ♦6  ♣5 P1
 ♣2  ♣6 P2
 ♠4  ♥8 P2
 ♠J  ♥9 P1
♥10  ♣Q P2
 ♣8  ♥7 P1
 ♦K  ♠Q P1
♦10  ♦2 P1
 ♣9  ♦9 WAR!
 ♦8  ♣J P2
 ♣3  ♦5 P2
 ♦Q  ♥4 P1
 ♠6  ♥A P2
 ♠K  ♣7 P1
 ♥Q  ♠3 P1
 ♣A  ♥K P1
 ♠A  ♦J P1
P1 14 P2 10: Player 1 wins
""".strip()
    assert out.strip() == expected

# --------------------------------------------------
def test_play02():
    out = getoutput('{} {} 2'.format(prg, seed_flag()))
    expected = """
 ♠4  ♠6 P2
 ♦K  ♣J P1
 ♠J  ♦4 P1
 ♣7  ♣4 P1
 ♥Q ♣10 P1
 ♦5  ♠3 P1
 ♥K  ♦9 P1
 ♥2  ♣Q P2
 ♥7  ♦A P2
 ♥3  ♥A P2
 ♣5  ♥8 P2
 ♠2 ♦10 P2
♠10  ♠K P2
 ♣2  ♦3 P2
 ♠Q  ♦8 P1
 ♦6  ♦J P2
 ♥6  ♣8 P2
 ♠8  ♦7 P1
 ♥5  ♦2 P1
 ♣6  ♥J P2
 ♥9  ♠9 WAR!
 ♣K  ♣A P2
♥10  ♦Q P2
 ♠7  ♠5 P1
 ♣9  ♠A P2
 ♥4  ♣3 P1
P1 11 P2 14: Player 2 wins
""".strip()
    assert out.strip() == expected

# --------------------------------------------------
def test_play03():
    out = getoutput('{} {} 10'.format(prg, seed_flag()))
    expected = """
 ♥J  ♠3 P1
 ♥2  ♥5 P2
 ♦Q ♠10 P1
♣10  ♥4 P1
 ♥6  ♣5 P1
 ♦3  ♠J P2
 ♦K  ♥8 P1
 ♦5  ♣8 P2
 ♠5  ♣3 P1
 ♣J ♦10 P1
♥10  ♦J P2
 ♥A  ♣7 P1
 ♠K  ♠Q P1
 ♦7  ♠A P2
 ♣9  ♠9 WAR!
 ♣2  ♠6 P2
 ♣K  ♦A P2
 ♦6  ♥Q P2
 ♠8  ♥9 P2
 ♥3  ♠7 P2
 ♦8  ♣Q P2
 ♣6  ♠4 P1
 ♥7  ♠2 P1
 ♣4  ♦4 WAR!
 ♦9  ♦2 P1
 ♥K  ♣A P2
P1 12 P2 12: DRAW
""".strip()
    assert out.strip() == expected
