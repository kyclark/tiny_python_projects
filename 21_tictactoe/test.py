#!/usr/bin/env python3
"""tests for tictactoe.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re
import string

prg = './tictactoe.py'


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

    rv, out = getstatusoutput(prg)
    assert rv == 0
    assert out.strip() == board


# --------------------------------------------------
def test_bad_board():
    """dies on bad board"""

    expected = '--board "{}" must be 9 characters of ., X, O'

    for bad in ['ABC', '...XXX', 'XXXOOOXX']:
        rv, out = getstatusoutput(f'{prg} --board {bad}')
        assert rv != 0
        assert re.search(expected.format(bad), out)


# --------------------------------------------------
def test_bad_player():
    """dies on bad player"""

    bad = random.choice([c for c in string.ascii_uppercase if c not in 'XO'])
    rv, out = getstatusoutput(f'{prg} -p {bad}')
    assert rv != 0
    expected = f"-p/--player: invalid choice: '{bad}'"
    assert re.search(expected, out)


# --------------------------------------------------
def test_bad_cell_int():
    """dies on bad cell"""

    for bad in [0, 10]:
        rv, out = getstatusoutput(f'{prg} --cell {bad}')
        assert rv != 0
        assert re.search(f'-c/--cell: invalid choice: {bad}', out)


# --------------------------------------------------
def test_bad_cell_str():
    """dies on bad cell string value"""

    bad = random.choice(string.ascii_letters)
    rv, out = getstatusoutput(f'{prg} --cell {bad}')
    assert rv != 0
    assert re.search(f"-c/--cell: invalid int value: '{bad}'", out, re.I)


# --------------------------------------------------
def test_both_player_and_cell():
    """test for both --player and --cell"""

    player = random.choice('XO')
    rv, out = getstatusoutput(f'{prg} --player {player}')
    assert rv != 0
    assert re.search('Must provide both --player and --cell', out)


# --------------------------------------------------
def test_good_board_01():
    """makes board on good input"""

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

    rv, out = getstatusoutput(f'{prg} -b .........')
    assert rv == 0
    assert out.strip() == board


# --------------------------------------------------
def test_good_board_02():
    """makes board on good input"""

    board = """
-------------
| 1 | 2 | 3 |
-------------
| O | X | X |
-------------
| 7 | 8 | 9 |
-------------
No winner.
""".strip()

    rv, out = getstatusoutput(f'{prg} --board ...OXX...')
    assert rv == 0
    assert out.strip() == board


# --------------------------------------------------
def test_mutate_board_01():
    """mutates board on good input"""

    board = """
-------------
| X | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
No winner.
""".strip()

    rv, out = getstatusoutput(f'{prg} -b ......... --player X -c 1')
    assert rv == 0
    assert out.strip() == board


# --------------------------------------------------
def test_mutate_board_02():
    """mutates board on good input"""

    board = """
-------------
| X | X | O |
-------------
| 4 | O | 6 |
-------------
| O | O | X |
-------------
O has won!
""".strip()

    rv, out = getstatusoutput(f'{prg} --board XXO...OOX --p O -c 5')
    assert rv == 0
    assert out.strip() == board


# --------------------------------------------------
def test_mutate_cell_taken():
    """test for a cell already taken"""

    rv1, out1 = getstatusoutput(f'{prg} -b XXO...OOX --player X --cell 9')
    assert rv1 != 0
    assert re.search('--cell "9" already taken', out1)

    rv2, out2 = getstatusoutput(f'{prg} --board XXO...OOX --p O -c 1')
    assert rv2 != 0
    assert re.search('--cell "1" already taken', out2)


# --------------------------------------------------
def test_winning():
    """test winning boards"""

    wins = [('PPP......'), ('...PPP...'), ('......PPP'), ('P..P..P..'),
            ('.P..P..P.'), ('..P..P..P'), ('P...P...P'), ('..P.P.P..')]

    for player in 'XO':
        other_player = 'O' if player == 'X' else 'X'

        for board in wins:
            board = board.replace('P', player)
            dots = [i for i in range(len(board)) if board[i] == '.']
            mut = random.sample(dots, k=2)
            test_board = ''.join([
                other_player if i in mut else board[i]
                for i in range(len(board))
            ])
            out = getoutput(f'{prg} -b {test_board}').splitlines()
            assert out[-1].strip() == f'{player} has won!'


# --------------------------------------------------
def test_losing():
    """test losing boards"""

    losing_board = list('XXOO.....')
    for i in range(10):
        random.shuffle(losing_board)
        out = getoutput(f'{prg} -b {"".join(losing_board)}').splitlines()
        assert out[-1].strip() == 'No winner.'
