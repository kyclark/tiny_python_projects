#!/usr/bin/env python3
"""Tic-Tac-Toe"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--state',
                        help='Board state',
                        metavar='str',
                        type=str,
                        default='.........')

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        metavar='str',
                        type=str,
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell to apply -p',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.player and not re.match('^[XO]$', args.player):
        parser.error(f'Invalid player "{args.player}", must be X or O')

    if args.cell and not 1 <= args.cell <= 9:
        parser.error(f'Invalid cell "{args.cell}", must be 1-9')

    if any([args.player, args.cell]) and not all([args.player, args.cell]):
        parser.error('Must provide both or neither --player and --cell')

    if not re.search('^[.XO]{9}$', args.state):
        msg = 'Invalid state "{}", must be 9 characters of only ., X, O'
        parser.error(msg.format(args.state))

    if args.player and args.cell and args.state[args.cell - 1] != '.':
        parser.error(f'Cell {args.cell} already taken')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    state = list(args.state)

    if args.player and args.cell:
        state[args.cell - 1] = args.player

    print(make_board(state))
    winner = get_winner(state)
    print(f'{winner} won!' if winner else 'No winner.')


# --------------------------------------------------
def make_board(state):
    """Make a TicTacToe board from the cells"""

    cells = [str(i) if c == '.' else c for i, c in enumerate(state, start=1)]
    sep = '-------------'
    tmpl = '| {} | {} | {} |'
    return '\n'.join([
        sep,
        tmpl.format(*cells[0:3]), sep,
        tmpl.format(*cells[3:6]), sep,
        tmpl.format(*cells[6:9]), sep
    ])


# --------------------------------------------------
def get_winner(state):
    """Return winning player if any"""

    winning = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),
               (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for player in ['X', 'O']:
        for i, j, k in winning:
            if [state[i], state[j], state[k]] == [player, player, player]:
                return player
    return ''


# --------------------------------------------------
if __name__ == '__main__':
    main()
