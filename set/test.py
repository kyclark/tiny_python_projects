#!/usr/bin/env python3
"""tests for set.py"""

import os
import re
from subprocess import getstatusoutput
from collections import defaultdict
from typing import List

prg = './set.py'


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
def parse_out(out: str) -> List[list]:
    """parse output"""

    sets = defaultdict(list)
    cur = 0
    for line in out.splitlines():
        match = re.match(r'Set (\d+)', line)
        if match:
            cur = int(match.group(1))
        else:
            assert cur > 0, 'Lines in proper order'
            sets[cur].append(line)

    return sets.values()


# --------------------------------------------------
def test_ok1():
    """runs"""

    rv, out = getstatusoutput('{} -s 1'.format(prg))
    assert rv == 0
    sets = parse_out(out)
    assert len(sets) == 2

    expected = [[
        '1 Green Outlined Diamond', '2 Red Outlined Oval',
        '3 Purple Outlined Squiggle'
    ],
                [
                    '1 Green Outlined Squiggle', '2 Red Outlined Squiggle',
                    '3 Purple Outlined Squiggle'
                ]]

    for e in expected:
        assert e in sets


# --------------------------------------------------
def test_ok2():
    """runs"""

    rv, out = getstatusoutput('{} -s 2'.format(prg))
    assert rv == 0
    sets = parse_out(out)
    assert len(sets) == 3

    expected = [[
        '1 Red Outlined Squiggle', '2 Red Solid Diamond', '3 Red Striped Oval'
    ],
                [
                    '1 Purple Outlined Squiggle', '2 Purple Solid Diamond',
                    '3 Purple Striped Oval'
                ],
                [
                    '1 Purple Outlined Squiggle', '2 Purple Outlined Diamond',
                    '3 Purple Outlined Oval'
                ]]

    for e in expected:
        assert e in sets
