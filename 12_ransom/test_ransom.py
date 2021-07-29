#!/usr/bin/env python3
"""tests for ransom.py"""

import os
import re
import random
from subprocess import getstatusoutput

prg = "./ransom.py"
fox = "../inputs/fox.txt"
now = "../inputs/now.txt"


# --------------------------------------------------
def seed_flag():
    return "-s" if random.randint(0, 1) else "--seed"


# --------------------------------------------------
def ascii_flag():
    return "-a" if random.randint(0, 1) else "--ascii"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{prg} {flag}")
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_text1():
    """Test"""

    in_text = "The quick brown fox jumps over the lazy dog."
    tests = [
        ("1", "thE QUICk BrOWn Fox jumpS OveR tHe LAzY dOg."),
        ("3", "thE quICk BROwn Fox jUmPS OVEr the lAZY DOG."),
    ]

    for seed, expected in tests:
        rv, out = getstatusoutput(f'{prg} {seed_flag()} {seed} "{in_text}"')
        assert rv == 0
        assert out.strip() == expected


# --------------------------------------------------
def test_ascii1():
    """Test ascii"""

    in_text = "The quick brown fox jumps over the lazy dog."
    expected = "+|-|3 QU1(|< |3RO\\/\\/|\\| |=OX _|U|\\/||`5 O\\/3R +|-|3 |_4ZY |)O(-."
    rv, out = getstatusoutput(f'{prg} {ascii_flag()} "{in_text}"')
    assert rv == 0
    assert out.strip() == expected


# --------------------------------------------------
def test_text2():
    """Test"""

    in_text = "Now is the time for all good men to come to the aid of the party."
    tests = [
        ("2", "now iS the TIME fOR ALl good meN TO COMe To THE AID oF THE PArTY."),
        ("5", "NOw is tHE Time FOr all good men To coME TO tHe AiD OF THe ParTy."),
    ]

    for seed, expected in tests:
        rv, out = getstatusoutput(f'{prg} {seed_flag()} {seed} "{in_text}"')
        assert rv == 0
        assert out.strip() == expected


# --------------------------------------------------
def test_ascii2():
    """Test ascii"""

    in_text = "Now is the time for all good men to come to the aid of the party."
    expected = "|\\|O\\/\\/ 15 +|-|3 +1|\\/|3 |=OR 4|_|_ (-OO|) |\\/|3|\\| +O (O|\\/|3 +O +|-|3 41|) O|= +|-|3 |`4R+Y."

    rv, out = getstatusoutput(f'{prg} {ascii_flag()} "{in_text}"')
    assert rv == 0
    assert out.strip() == expected


# --------------------------------------------------
def test_file1():
    """Test"""

    tests = [
        ("1", "thE QUICk BrOWn Fox jumpS OveR tHe LAzY dOg."),
        ("3", "thE quICk BROwn Fox jUmPS OVEr the lAZY DOG."),
    ]

    for seed, expected in tests:
        rv, out = getstatusoutput(f"{prg} {seed_flag()} {seed} {fox}")
        assert rv == 0
        assert out.strip() == expected


# --------------------------------------------------
def test_file2():
    """Test"""

    tests = [
        ("2", "now iS the TIME fOR ALl good meN TO COMe To THE AID oF THE PArTY."),
        ("5", "NOw is tHE Time FOr all good men To coME TO tHe AiD OF THe ParTy."),
    ]

    for seed, expected in tests:
        rv, out = getstatusoutput(f"{prg} {seed_flag()} {seed} {now}")
        assert rv == 0
        assert out.strip() == expected


# --------------------------------------------------
def test_ascii_file1():
    """Test ascii file"""

    expected = "+|-|3 QU1(|< |3RO\\/\\/|\\| |=OX _|U|\\/||`5 O\\/3R +|-|3 |_4ZY |)O(-."
    rv, out = getstatusoutput(f"{prg} {ascii_flag()} {fox}")
    assert rv == 0
    assert out.strip() == expected


# --------------------------------------------------
def test_ascii_file2():
    """Test ascii file"""

    expected = "|\\|O\\/\\/ 15 +|-|3 +1|\\/|3 |=OR 4|_|_ (-OO|) |\\/|3|\\| +O (O|\\/|3 +O +|-|3 41|) O|= +|-|3 |`4R+Y."
    rv, out = getstatusoutput(f"{prg} {ascii_flag()} {now}")
    assert rv == 0
    assert out.strip() == expected
