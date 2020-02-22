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
def test_bad_state():
    """dies on bad state"""

    expected = '--state "{}" must be 9 characters of ., X, O'

    for bad in ['ABC', '...XXX', 'XXXOOOXX']:
        rv, out = getstatusoutput(f'{prg} --state {bad}')
        print(out)
        assert rv != 0
        assert re.search(expected.format(bad), out)


# --------------------------------------------------
def test_bad_player():
    """dies on bad player"""

    bad = random.choice([c for c in string.ascii_uppercase if c not in 'XO'])
    print(f'{prg} -p {bad}')
    rv, out = getstatusoutput(f'{prg} -p {bad}')
    print(out)
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
def test_good_state():
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

    rv1, out1 = getstatusoutput(f'{prg} -s .........')
    assert rv1 == 0
    assert out1.strip() == board1

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

    rv2, out2 = getstatusoutput(f'{prg} -s ...OXX...')
    assert out2.strip() == board2


# --------------------------------------------------
def test_mutate_state():
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

    rv1, out1 = getstatusoutput(f'{prg} -s ......... --player X -c 1')
    assert rv1 == 0
    assert out1.strip() == board1

    board2 = """
-------------
| X | X | O |
-------------
| 4 | O | 6 |
-------------
| O | O | X |
-------------
O has won!
""".strip()

    rv2, out2 = getstatusoutput(f'{prg} --state XXO...OOX --p O -c 5')
    assert rv2 == 0
    assert out2.strip() == board2


# --------------------------------------------------
def test_mutate_state_taken():
    """test for a cell already taken"""

    rv1, out1 = getstatusoutput(f'{prg} -s XXO...OOX --player X --cell 9')
    assert rv1 != 0
    assert re.search('--cell "9" already taken', out1)

    rv2, out2 = getstatusoutput(f'{prg} --state XXO...OOX --p O -c 1')
    assert rv2 != 0
    assert re.search('--cell "1" already taken', out2)


# --------------------------------------------------
def test_winning():
    """test winning states"""

    wins = [('PPP......'), ('...PPP...'), ('......PPP'), ('P..P..P..'),
            ('.P..P..P.'), ('..P..P..P'), ('P...P...P'), ('..P.P.P..')]

    for player in 'XO':
        other_player = 'O' if player == 'X' else 'X'

        for state in wins:
            state = state.replace('P', player)
            dots = [i for i in range(len(state)) if state[i] == '.']
            mut = random.sample(dots, k=2)
            test_state = ''.join([
                other_player if i in mut else state[i]
                for i in range(len(state))
            ])
            out = getoutput(f'{prg} -s {test_state}').splitlines()
            assert out[-1].strip() == f'{player} has won!'


# --------------------------------------------------
def test_losing():
    """test losing states"""

    losing_state = list('XXOO.....')
    for i in range(10):
        random.shuffle(losing_state)
        print(f'{prg} {" ".join(losing_state)}')
        out = getoutput(f'{prg} -s {"".join(losing_state)}').splitlines()
        assert out[-1].strip() == 'No winner.'
