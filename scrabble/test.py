#!/usr/bin/env python3
"""tests for scrabble.py"""

import os
import re
import random
import string
from subprocess import getstatusoutput

prg = './scrabble.py'


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
def test_bad_tiles():
    """bad_tiles"""

    tiles = ''.join(
        random.sample(string.ascii_uppercase, k=random.choice(range(8, 12))))
    rv, out = getstatusoutput('{} -t "{}"'.format(prg, tiles))
    assert rv != 0
    assert re.search('--tiles "{}" can only be 7 characters'.format(tiles),
                     out)
