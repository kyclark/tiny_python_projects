#!/usr/bin/env python3
"""tests for pareto.py"""

import os
import re
import random
import hashlib
from subprocess import getstatusoutput

prg = './pareto.py'


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
def test_runs1():
    """Runs"""

    expected = """
  1: 2115 iterations
  2: 2058 iterations
  3: 1330 iterations
  4: 2139 iterations
  5: 2294 iterations
  6: 1226 iterations
  7: 1663 iterations
  8: 1603 iterations
  9: 1088 iterations
 10: 2008 iterations
Average = 1,752 iterations
    """.strip()

    rv, out = getstatusoutput('{} -s 1'.format(prg))
    assert rv == 0
    assert out.strip() == expected
