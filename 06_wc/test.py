#!/usr/bin/env python3
"""tests for wc.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './wc.py'
empty = './inputs/empty.txt'
one_line = './inputs/one.txt'
two_lines = './inputs/two.txt'
fox = '../inputs/fox.txt'
sonnet = '../inputs/sonnet-29.txt'

# --------------------------------------------------
def character_flag():
    """Either -c or --character"""

    return "-c" if random.randint(0, 1) else "--character"


# --------------------------------------------------
def line_flag():
    """Either -l or --line"""

    return "-l" if random.randint(0, 1) else "--line"


# --------------------------------------------------
def word_flag():
    """Either -w or --word"""

    return "-w" if random.randint(0, 1) else "--word"


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
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def test_bad_file():
    """bad_file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_empty():
    """Test on empty"""

    rv, out = getstatusoutput(f'{prg} {empty}')
    assert rv == 0
    assert out.rstrip() == '       0       0       0 ./inputs/empty.txt'


# --------------------------------------------------
def test_one():
    """Test on one"""

    rv, out = getstatusoutput(f'{prg} {one_line}')
    assert rv == 0
    assert out.rstrip() == '       1       1       2 ./inputs/one.txt'


# --------------------------------------------------
def test_two():
    """Test on two"""

    rv, out = getstatusoutput(f'{prg} {two_lines}')
    assert rv == 0
    assert out.rstrip() == '       2       2       4 ./inputs/two.txt'


# --------------------------------------------------
def test_fox():
    """Test on fox"""

    rv, out = getstatusoutput(f'{prg} {fox}')
    assert rv == 0
    assert out.rstrip() == '       1       9      45 ../inputs/fox.txt'


# --------------------------------------------------
def test_more():
    """Test on more than one file"""

    rv, out = getstatusoutput(f'{prg} {fox} {sonnet}')
    expected = ('       1       9      45 ../inputs/fox.txt\n'
                '      17     118     661 ../inputs/sonnet-29.txt\n'
                '      18     127     706 total')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_stdin():
    """Test on stdin"""

    rv, out = getstatusoutput(f'{prg} < {fox}')
    assert rv == 0
    assert out.rstrip() == '       1       9      45 <stdin>'


# --------------------------------------------------
def test_fox_c():
    """Test on fox character column"""

    rv, out = getstatusoutput(f'{prg} {character_flag()} {fox}')
    assert rv == 0
    assert out.rstrip() == '      45 ../inputs/fox.txt'


# --------------------------------------------------
def test_fox_l():
    """Test on fox line column"""

    rv, out = getstatusoutput(f'{prg} {line_flag()} {fox}')
    assert rv == 0
    assert out.rstrip() == '       1 ../inputs/fox.txt'


# --------------------------------------------------
def test_fox_w():
    """Test on fox word column"""

    rv, out = getstatusoutput(f'{prg} {word_flag()} {fox}')
    assert rv == 0
    assert out.rstrip() == '       9 ../inputs/fox.txt'


# --------------------------------------------------
def test_two_lw():
    """Test on two line and word columns"""

    rv, out = getstatusoutput(f'{prg} {line_flag()} {word_flag()} {two_lines}')
    assert rv == 0
    assert out.rstrip() == '       2       2 ./inputs/two.txt'


# --------------------------------------------------
def test_two_lc():
    """Test on two line and character columns"""

    rv, out = getstatusoutput(f'{prg} {two_lines} {line_flag()} {character_flag()}')
    assert rv == 0
    assert out.rstrip() == '       2       4 ./inputs/two.txt'


# --------------------------------------------------
def test_two_wc():
    """Test on two word and character columns"""

    rv, out = getstatusoutput(f'{prg} {two_lines} {word_flag()} {character_flag()}')
    assert rv == 0
    assert out.rstrip() == '       2       4 ./inputs/two.txt'


# --------------------------------------------------
def test_two_lw_paired():
    """Test on two line and word columns paired"""

    rv, out = getstatusoutput(f'{prg} -lw {two_lines}')
    assert rv == 0
    assert out.rstrip() == '       2       2 ./inputs/two.txt'


# --------------------------------------------------
def test_two_lc_paired():
    """Test on two line and character columns paired"""

    rv, out = getstatusoutput(f'{prg} {two_lines} -lc')
    assert rv == 0
    assert out.rstrip() == '       2       4 ./inputs/two.txt'


# --------------------------------------------------
def test_two_wc_paired():
    """Test on two word and character columns paired"""

    rv, out = getstatusoutput(f'{prg} {two_lines} -wc')
    assert rv == 0
    assert out.rstrip() == '       2       4 ./inputs/two.txt'


# --------------------------------------------------
def test_more_all3():
    """Test on more than one file with all three columns"""

    rv, out = getstatusoutput(f'{prg} {fox} {sonnet} -lwc')
    expected = ('       1       9      45 ../inputs/fox.txt\n'
                '      17     118     661 ../inputs/sonnet-29.txt\n'
                '      18     127     706 total')
    assert rv == 0
    assert out.rstrip() == expected


