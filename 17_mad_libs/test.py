#!/usr/bin/env python3
"""tests for mad_lib.py"""

import re
import os
import random
import string
from subprocess import getstatusoutput

prg = './mad.py'
no_blanks = 'inputs/no_blanks.txt'
fox = 'inputs/fox.txt'
hlp = 'inputs/help.txt'
verona = 'inputs/romeo_juliet.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_file():
    """Test bad input file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_no_blanks():
    """Test no blanks"""

    rv, out = getstatusoutput(f'{prg} {no_blanks}')
    assert rv != 0
    assert out == f'"{no_blanks}" has no placeholders.'


# --------------------------------------------------
def test_fox():
    """test fox"""

    args = f'{fox} -i surly car under bicycle'
    rv, out = getstatusoutput(f'{prg} {args}')
    assert rv == 0
    assert out.strip() == 'The quick surly car jumps under the lazy bicycle.'


# --------------------------------------------------
def test_help():
    """test help"""

    expected = """
Hey! I need tacos!
Oi! Not just salsa!
Hola! You know I need queso!
Arriba!
    """.strip()

    args = f'{hlp} -i Hey tacos Oi salsa Hola queso Arriba'
    rv, out = getstatusoutput(f'{prg} {args}')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_verona():
    """test verona"""

    expected = """
Two cars, both alike in dignity,
In fair Detroit, where we lay our scene,
From ancient oil break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-cross'd pistons take their life;
Whose misadventur'd piteous overthrows
Doth with their stick shift bury their parents' strife.
The fearful passage of their furious love,
And the continuance of their parents' rage,
Which, but their children's end, nought could accelerate,
Is now the 42 hours' traffic of our stage;
The which if you with patient foot attend,
What here shall hammer, our toil shall strive to mend.
    """.strip()

    args = (f'{verona} --inputs cars Detroit oil pistons '
            '"stick shift" furious accelerate 42 foot hammer')
    rv, out = getstatusoutput(f'{prg} {args}')
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
