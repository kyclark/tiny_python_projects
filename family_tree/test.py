#!/usr/bin/env python3
"""tests for tree.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './tree.py'
joanie = './joanie.txt'


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
def test_bad_input():
    """Bad input"""

    bad = 'bad.txt'
    rv, out = getstatusoutput('{} {}'.format(prg, bad))
    assert rv != 0
    assert out.rstrip() == 'No nodes or edges in "{}".'.format(bad)


# --------------------------------------------------
def test_joanie():
    """Joanie Loves Chachi"""

    out_file = 'joanie.txt.gv'
    out_pdf = out_file + '.pdf'

    try:
        for file in [out_file, out_pdf]:
            if os.path.isfile(file):
                os.remove(file)

        for file in [out_file, out_pdf]:
            assert not os.path.isfile(file)

        rv, out = getstatusoutput('{} {}'.format(prg, joanie))
        assert rv == 0
        assert out.rstrip() == 'Done, see output in "joanie.txt.gv".'

        for file in [out_file, out_pdf]:
            assert os.path.isfile(file)

        gv = open(out_file).read().rstrip()
        assert gv == '// Tree\ndigraph {\n\tJoanie -> Chachi\n}'

    finally:
        for file in [out_file, out_pdf]:
            if os.path.isfile(file):
                os.remove(file)


# --------------------------------------------------
def test_joanie_outfile():
    """Joanie Loves Chachi"""

    out_file = random_string() + '.gv'
    out_pdf = out_file + '.pdf'

    try:
        for file in [out_file, out_pdf]:
            if os.path.isfile(file):
                os.remove(file)

        for file in [out_file, out_pdf]:
            assert not os.path.isfile(file)

        rv, out = getstatusoutput('{} -o {} {}'.format(prg, out_file, joanie))
        assert rv == 0
        assert out.rstrip() == 'Done, see output in "{}".'.format(out_file)

        for file in [out_file, out_pdf]:
            assert os.path.isfile(file)

        gv = open(out_file).read().rstrip()
        assert gv == '// Tree\ndigraph {\n\tJoanie -> Chachi\n}'

    finally:
        for file in [out_file, out_pdf]:
            if os.path.isfile(file):
                os.remove(file)


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
