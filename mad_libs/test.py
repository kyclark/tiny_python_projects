#!/usr/bin/env python3
"""tests for mad_lib.py"""

import re
import os
import random
from subprocess import getstatusoutput

prg = './mad_lib.py'


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
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    expected = """
Hey! I need tacos!
Oi! Not just salsa!
Hola! You know I need queso!
Arriba!
    """.strip()

    args = 'help.txt -i Hey tacos Oi salsa Hola queso Arriba'
    rv, out = getstatusoutput('{} {}'.format(prg, args))
    assert rv == 0
    assert out.strip() == expected.strip()


# --------------------------------------------------
def test_02():
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

    args = ('romeo_juliet.txt --inputs cars Detroit oil pistons '
            '"stick shift" furious accelerate 42 foot hammer')
    rv, out = getstatusoutput('{} {}'.format(prg, args))
    assert rv == 0
    assert out.strip() == expected.strip()
