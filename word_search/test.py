#!/usr/bin/env python3
"""tests for wod.py"""

import re
import os
import random
from subprocess import getstatusoutput

prg = './search.py'

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
def test_puzzle01():
    """forward horizontal"""

    rv, out = getstatusoutput('{} puzzle01.txt'.format(prg))
    assert rv == 0
    assert out.strip() == '.BC.'

# --------------------------------------------------
def test_puzzle02():
    """backward horizontal"""

    rv, out = getstatusoutput('{} puzzle02.txt'.format(prg))
    assert rv == 0
    assert out.strip() == 'AB.'

# --------------------------------------------------
def test_puzzle03():
    """forward vertical down"""

    rv, out = getstatusoutput('{} puzzle03.txt'.format(prg))
    assert rv == 0
    assert out.strip() == '.B.\n.E.\n.H.'


# --------------------------------------------------
def test_puzzle04():
    """backward vertical down"""

    rv, out = getstatusoutput('{} puzzle04.txt'.format(prg))
    assert rv == 0
    assert out.strip() == '..C\n..F\n..I'

# --------------------------------------------------
def test_puzzle05():
    """forward diagonal down"""

    rv, out = getstatusoutput('{} puzzle05.txt'.format(prg))
    assert rv == 0
    assert out.strip() == 'A..\n.E.\n..I'

# --------------------------------------------------
def test_puzzle06():
    """backward diagonal down"""

    rv, out = getstatusoutput('{} puzzle06.txt'.format(prg))
    assert rv == 0
    assert out.strip() == '...\nD..\n.H.'

# --------------------------------------------------
def test_puzzle07():
    """backward diagonal down"""

    rv, out = getstatusoutput('{} puzzle07.txt'.format(prg))
    assert rv == 0
    assert out.strip() == '.B.\n..F\n...'

# --------------------------------------------------
def test_puzzle08():
    """forward diagonal up"""

    rv, out = getstatusoutput('{} puzzle08.txt'.format(prg))
    assert rv == 0
    assert out.strip() == '..C\n.E.\n...'

# --------------------------------------------------
def test_puzzle09():
    """backward diagonal up"""

    rv, out = getstatusoutput('{} puzzle09.txt'.format(prg))
    assert rv == 0
    assert out.strip() == '...\n..F\n.H.'

# --------------------------------------------------
def test_ice_cream():
    """ice cream"""

    expected = """.....CHOCOLATE
.SKCARTESOOM..
.YVANILLA.N...
M.D.T..A..A..A
.A.N.IN...C..E
..P.AAG...E..T
...LNC.E..P.RN
...AE.N.R..E.E
..B..W.O.TE..E
......A.TSA..R
.......LET.I.G
.EGDUF.SN.O.L.
DAORYKCORU.C..
...TUNOCOCT...
    """.rstrip()
    rv, out = getstatusoutput('{} ice_cream.txt'.format(prg))
    assert rv == 0
    assert out.strip() == expected

# --------------------------------------------------
def test_shapes():
    """shapes"""

    expected = """...C.S.........
..T.UU..S......
..R..BR.P..M...
..I..ME.H.S....
..AENOC.EI.....
..N..HT.R......
..G.TRAPEZOID..
POLYGON.DL....N
PPENTAGON.L..O.
.Y.O..L.IE.IG..
MARGOLELLARAP..
...A...CY.TA.S.
...XM.R.CC..U.E
...E.I..O....Q.
...HC.D.......S
    """.rstrip()
    rv, out = getstatusoutput('{} shapes.txt'.format(prg))
    assert rv == 0
    assert out.strip() == expected
