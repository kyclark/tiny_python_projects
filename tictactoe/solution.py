#!/usr/bin/env python3
"""Tic-Tac-Toe"""

import argparse
import re
import sys


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

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    state = args.state
    player = args.player
    cell = args.cell

    cells = []
    for i, char in enumerate(state, start=1):
        cells.append(str(i) if char == '.' else char)

    if player and cell:
        if cells[cell - 1] not in 'XO':
            cells[cell - 1] = player
        else:
            print('Cell {} already taken'.format(cell))
            sys.exit(1)

    sep = '-------------'
    tmpl = '| {} | {} | {} |'

    print('\n'.join([
        sep,
        tmpl.format(cells[0], cells[1], cells[2]), sep,
        tmpl.format(cells[3], cells[4], cells[5]), sep,
        tmpl.format(cells[6], cells[7], cells[8]), sep
    ]))

    winner = get_winner(state)
    print(f'{winner} won!' if winner else 'No winner.')


# --------------------------------------------------
def get_winner(state):
    """Return winning player if any"""

    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    # for player in ['X', 'O']:
    #     for combo in winning:
    #         i, j, k = combo
    #         if state[i] == player and state[j] == player and state[k] == player:
    #             winner = player
    #             break

    # for player in ['X', 'O']:
    #     for combo in winning:
    #         chars = []
    #         for i in combo:
    #             chars.append(state[i])

    #         if ''.join(chars) == player * 3:
    #             winner = player
    #             break

    # for player in ['X', 'O']:
    #     for i, j, k in winning:
    #         chars = ''.join([state[i], state[j], state[k]])
    #         if ''.join(chars) == '{}{}{}'.format(player, player, player):
    #             winner = player
    #             break

    for player in ['X', 'O']:
        for i, j, k in winning:
            combo = [state[i], state[j], state[k]]
            if combo == [player, player, player]:
                return (player)

    # for combo in winning:
    #     group = list(map(lambda i: state[i], combo))
    #     for player in ['X', 'O']:
    #         if all(x == player for x in group):
    #             winner = player
    #             break


# --------------------------------------------------
if __name__ == '__main__':
    main()
