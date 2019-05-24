#!/usr/bin/env python3
"""tests for guess.py"""

from subprocess import getoutput, getstatusoutput

prg = './guess.py'


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_low():
    """low"""

    for flag, val in [('-m', '0'), ('--min', '-1')]:
        rv, out = getstatusoutput('{} {} {}'.format(prg, flag, val))
        assert rv != 0
        assert out.strip() == '--min "{}" cannot be lower than 1'.format(val)


# --------------------------------------------------
def test_bad_guesses():
    """guessess"""

    for flag, val in [('-g', '0'), ('--guesses', '-1')]:
        rv, out = getstatusoutput('{} {} {}'.format(prg, flag, val))
        assert rv != 0
        assert out.strip() == '--guesses "{}" cannot be lower than 1'.format(
            val)


# --------------------------------------------------
def test_low_high():
    """low/high"""

    low = 50
    high = 20
    rv, out = getstatusoutput('{} --min {} --max {}'.format(prg, low, high))
    assert rv != 0
    expected = '--min "{}" is higher than --max "{}"'.format(low, high)
    assert out.strip() == expected


# --------------------------------------------------
def test_01():
    """test the first"""

    out = getoutput('{} -s 1 -i 25 12 6 9'.format(prg))
    expected = """
"25" is too high.
"12" is too high.
"6" is too low.
"9" is correct. You win!
    """.strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_02():
    """test the second"""

    out = getoutput('{} -s 1 -i 25 12 foo 6 q'.format(prg))
    expected = """
"25" is too high.
"12" is too high.
"foo" is not a number.
"6" is too low.
Now you will never know the answer.
    """.strip()
    assert out.strip() == expected


# --------------------------------------------------
def test_03():
    """test the third"""

    out = getoutput('{} -s 2 -g 3 -i 1 2 3'.format(prg))
    expected = """
"1" is too low.
"2" is too low.
"3" is too low.
Too many guesses, loser! The number was "4."
    """.strip()
    print(out)
    assert out.strip() == expected
