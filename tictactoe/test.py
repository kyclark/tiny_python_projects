#!/usr/bin/env python3
"""tests for tictactoe.py"""

import os
import random
import re
from subprocess import getstatusoutput, getoutput

prg = './tictactoe.py'


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
def test_bad_state():
    """dies on bad state"""

    expected = 'Invalid state "{}", must be 9 characters of only ., X, O'
    for bad in ['ABC', '...XXX', 'XXXOOOXX']:
        rv, out = getstatusoutput('{} --state {}'.format(prg, bad))
        assert rv != 0
        assert re.search(expected.format(bad), out)


# --------------------------------------------------
def test_bad_player():
    """dies on bad player"""

    rv, out = getstatusoutput('{} -p A'.format(prg))
    assert rv != 0
    assert re.search('Invalid player "A", must be X or O', out)


# --------------------------------------------------
def test_bad_cell_int():
    """dies on bad cell"""

    bad = random.randint(10, 20)
    rv, out = getstatusoutput('{} --cell {}'.format(prg, bad))
    assert rv != 0
    expected = 'Invalid cell "{}", must be 1-9'
    assert re.search(expected.format(bad), out)


# --------------------------------------------------
def test_bad_cell_str():
    """dies on bad cell string value"""

    rv, out = getstatusoutput('{} --cell foo'.format(prg))
    assert rv > 0
    assert re.match("usage", out, re.IGNORECASE)
    assert re.search("invalid int value", out, re.IGNORECASE)


# --------------------------------------------------
def test_both_player_and_cell():
    """test for both --player and --cell"""

    rv, out = getstatusoutput('{} --player X'.format(prg))
    assert rv > 0
    assert re.search('Must provide both or neither --player and --cell', out)


# --------------------------------------------------
def test_no_input():
    """makes board on no input"""

    board = """
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
No winner.
""".strip()

    out = getoutput(prg)
    assert out.strip() == board


# --------------------------------------------------
def test_good_state1():
    """makes board on good input"""

    board1 = """
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
No winner.
""".strip()

    out1 = getoutput('{} -s .........'.format(prg))
    assert out1.strip() == board1


# --------------------------------------------------
def test_good_state2():
    """makes board on good input"""
    board2 = """
-------------
| 1 | 2 | 3 |
-------------
| O | X | X |
-------------
| 7 | 8 | 9 |
-------------
No winner.
""".strip()

    out2 = getoutput('{} -s ...OXX...'.format(prg))
    assert out2.strip() == board2


# --------------------------------------------------
def test_mutate_state1():
    """mutates board on good input"""

    board1 = """
-------------
| X | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
No winner.
""".strip()

    out1 = getoutput('{} -s ......... --player X -c 1'.format(prg))
    assert out1.strip() == board1


# --------------------------------------------------
def test_mutate_state2():
    """mutates board on good input"""
    board2 = """
-------------
| X | X | O |
-------------
| 4 | O | 6 |
-------------
| O | O | X |
-------------
No winner.
""".strip()

    out2 = getoutput('{} --state XXO...OOX --p O -c 5'.format(prg))
    assert out2.strip() == board2


# --------------------------------------------------
def test_mutate_state_taken():
    """test for a cell already taken"""

    out1 = getoutput('{} -s XXO...OOX --player X --cell 9'.format(prg))
    assert out1.strip() == 'Cell 9 already taken'

    out2 = getoutput('{} --state XXO...OOX --p O -c 1'.format(prg))
    assert out2.strip() == 'Cell 1 already taken'


# --------------------------------------------------
def test_outcome():
    """outcome"""

    wins = [('X', 'XXX......'), ('O', 'OOO......'), ('X', '...XXX...'),
            ('O', '...OOO...'), ('X', '......XXX'), ('O', '......OOO'),
            ('X', 'X..X..X..'), ('O', 'O..O..O..'), ('X', '.X..X..X.'),
            ('O', '.O..O..O.'), ('X', '..X..X..X'), ('O', '..O..O..O'),
            ('X', 'X...X...X'), ('O', 'O...O...O'), ('X', '..X.X.X..'),
            ('O', '..O.O.O..')]

    for player, state in wins:
        l = len(state)
        dots = [i for i in range(l) if state[i] == '.']
        mut = random.sample(dots, k=2)
        other_player = 'O' if player == 'X' else 'X'
        new_state = ''.join(
            [other_player if i in mut else state[i] for i in range(l)])
        out = getoutput('{} -s {}'.format(prg, new_state))
        assert re.search(f'{player} won!', out)

    losing_state = list('XXOO.....')
    for i in range(10):
        random.shuffle(losing_state)
        out = getoutput('{} -s {}'.format(prg, ''.join(losing_state)))
        assert re.search('No winner.', out)
