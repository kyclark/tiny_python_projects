#!/usr/bin/env python3
"""tests for outcome.py"""

from subprocess import getstatusoutput, getoutput
from random import shuffle, sample
import os.path
import re

outcome = './outcome.py'


def usage(prg):
    """usage"""

    (retval, out) = getstatusoutput(prg)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)


def test_outcome_usage():
    """outcome usage"""

    usage(outcome)


def bad_input(prg):
    """fails on bad input"""

    tmpl = 'State "{}" must be 9 characters of only ., X, O'
    """bad input"""
    state1 = '.'
    out1 = getoutput('{} {}'.format(prg, state1))
    assert out1.rstrip() == tmpl.format(state1)

    state2 = '..X.OA..X'
    out2 = getoutput('{} {}'.format(prg, state2))
    assert out2.rstrip() == tmpl.format(state2)


def test_outcome_bad_input():
    """outcome bad input"""

    bad_input(outcome)


def test_outcome():
    wins = [('X', 'XXX......'), ('O', 'OOO......'), ('X', '...XXX...'),
            ('O', '...OOO...'), ('X', '......XXX'), ('O', '......OOO'),
            ('X', 'X..X..X..'), ('O', 'O..O..O..'), ('X', '.X..X..X.'),
            ('O', '.O..O..O.'), ('X', '..X..X..X'), ('O', '..O..O..O'),
            ('X', 'X...X...X'), ('O',
                                 'O...O...O'), ('X',
                                                '..X.X.X..'), ('O',
                                                               '..O.O.O..')]

    for player, state in wins:
        l = len(state)
        dots = [i for i in range(l) if state[i] == '.']
        mut = sample(dots, k=2)
        other_player = 'O' if player == 'X' else 'X'
        new_state = ''.join(
            [other_player if i in mut else state[i] for i in range(l)])
        out = getoutput('{} {}'.format(outcome, new_state))
        assert out.strip() == '{} has won'.format(player)

    losing_state = list('XXOO.....')
    for i in range(10):
        shuffle(losing_state)
        out = getoutput('{} {}'.format(outcome, ''.join(losing_state)))
        assert out.strip() == 'No winner'
