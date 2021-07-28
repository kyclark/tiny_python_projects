#!/usr/bin/env python3
"""tests for bottles.py"""

import hashlib
import os
import random
import re
import string
from subprocess import getstatusoutput

prg = "./bottles.py"


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
def test_bad_num():
    """Bad integer value for num"""

    bad = random.randint(-10, 1)
    rv, out = getstatusoutput(f"{prg} -n {bad}")
    assert rv != 0
    assert re.search(f'--num "{bad}" must be greater than 0', out)


# --------------------------------------------------
def test_bad_step():
    """Bad integer value for step"""

    bad = random.randint(-10, 1)
    rv, out = getstatusoutput(f"{prg} -s {bad}")
    assert rv != 0
    assert re.search(f'--step "{bad}" must be greater than 0', out)


# --------------------------------------------------
def test_float_num():
    """float value for num"""

    bad = round(random.random() * 10, 2)
    rv, out = getstatusoutput(f"{prg} --num {bad}")
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_float_step():
    """float value for step"""

    bad = round(random.random() * 10, 2)
    rv, out = getstatusoutput(f"{prg} --step {bad}")
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_str_num():
    """str value for num"""

    bad = random_string()
    rv, out = getstatusoutput(f"{prg} -n {bad}")
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)

# --------------------------------------------------
def test_str_step():
    """str value for step"""

    bad = random_string()
    rv, out = getstatusoutput(f"{prg} -s {bad}")
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_one():
    """One bottle of beer"""

    expected = (
        "One bottle of beer on the wall,\n"
        "One bottle of beer,\n"
        "Take one down, pass it around,\n"
        "No more bottles of beer on the wall!"
    )

    rv, out = getstatusoutput(f"{prg} --num 1")
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_two():
    """Two bottles of beer"""

    expected = (
        "Two bottles of beer on the wall,\n"
        "Two bottles of beer,\n"
        "Take one down, pass it around,\n"
        "One bottle of beer on the wall!\n\n"
        "One bottle of beer on the wall,\n"
        "One bottle of beer,\n"
        "Take one down, pass it around,\n"
        "No more bottles of beer on the wall!"
    )

    rv, out = getstatusoutput(f"{prg} -n 2")
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_random():
    """Random number"""

    sums = dict(map(lambda x: x.split("\t"), open("sums.txt").read().splitlines()))

    for n in random.choices(list(sums.keys()), k=10):
        flag = "-n" if random.choice([0, 1]) == 1 else "--num"
        rv, out = getstatusoutput(f"{prg} {flag} {n}")
        out += "\n"  # because the last newline is removed
        assert rv == 0
        assert hashlib.md5(out.encode("utf-8")).hexdigest() == sums[n]


def test_step_2():
    """Test step 2"""

    expected = (
        "Ten bottles of beer on the wall,\n"
        "Ten bottles of beer,\n"
        "Take two down, pass them around,\n"
        "Eight bottles of beer on the wall!\n\n"
        "Eight bottles of beer on the wall,\n"
        "Eight bottles of beer,\n"
        "Take two down, pass them around,\n"
        "Six bottles of beer on the wall!\n\n"
        "Six bottles of beer on the wall,\n"
        "Six bottles of beer,\n"
        "Take two down, pass them around,\n"
        "Four bottles of beer on the wall!\n\n"
        "Four bottles of beer on the wall,\n"
        "Four bottles of beer,\n"
        "Take two down, pass them around,\n"
        "Two bottles of beer on the wall!\n\n"
        "Two bottles of beer on the wall,\n"
        "Two bottles of beer,\n"
        "Take two down, pass them around,\n"
        "No more bottles of beer on the wall!"
    )

    rv, out = getstatusoutput(f"{prg} -s 2")
    assert rv == 0
    assert out == expected


def test_step_5():
    """Test step 5"""

    expected = (
        "Ten bottles of beer on the wall,\n"
        "Ten bottles of beer,\n"
        "Take five down, pass them around,\n"
        "Five bottles of beer on the wall!\n\n"
        "Five bottles of beer on the wall,\n"
        "Five bottles of beer,\n"
        "Take five down, pass them around,\n"
        "No more bottles of beer on the wall!"
    )

    rv, out = getstatusoutput(f"{prg} --step 5")
    assert rv == 0
    assert out == expected


def test_overstep():
    """Test 2 bottles step 5"""

    expected = (
        "Two bottles of beer on the wall,\n"
        "Two bottles of beer,\n"
        "Take two down, pass them around,\n"
        "No more bottles of beer on the wall!"
    )

    rv, out = getstatusoutput(f"{prg} -n 2 --step 5")
    assert rv == 0
    assert out == expected


def test_reverse():
    """Test reverse with one bottles"""

    expected = (
        "No bottles of beer on the wall,\n"
        "No bottles of beer,\n"
        "Reach in the case and put one in place,\n"
        "One bottle of beer on the wall!"
    )

    rv, out = getstatusoutput(f"{prg} -n 1 --reverse")
    assert rv == 0
    assert out == expected


def test_reverse_three():
    """Test reverse with 3 bottles"""

    expected = (
        "No bottles of beer on the wall,\n"
        "No bottles of beer,\n"
        "Reach in the case and put one in place,\n"
        "One bottle of beer on the wall!\n\n"
        "One bottle of beer on the wall,\n"
        "One bottle of beer,\n"
        "Reach in the case and put one in place,\n"
        "Two bottles of beer on the wall!\n\n"
        "Two bottles of beer on the wall,\n"
        "Two bottles of beer,\n"
        "Reach in the case and put one in place,\n"
        "Three bottles of beer on the wall!"
    )

    rv, out = getstatusoutput(f"{prg} -n 3 --r")
    assert rv == 0
    assert out == expected


def test_reverse_overstep():
    """Test reverse with overstep"""

    expected = (
        "No bottles of beer on the wall,\n"
        "No bottles of beer,\n"
        "Reach in the case and put three in place,\n"
        "Three bottles of beer on the wall!"
    )

    rv, out = getstatusoutput(f"{prg} -n 3 -s 5 --reverse")
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))
