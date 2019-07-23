#!/usr/bin/env python3
"""tests for scrabble.py"""

import os
import re
import random
import hashlib
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
