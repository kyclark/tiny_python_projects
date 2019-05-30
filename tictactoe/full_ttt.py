#!/usr/bin/env python3

import argparse
import copy
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Two-player Tic-Tac-Toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    return parser.parse_args()


# --------------------------------------------------
def print_board(state):
    """Given a state of cells print the board"""

    bar = '-------------'
    cells_tmpl = '| {} | {} | {} |'

    cells = []
    for i in range(0, 9):
        cells.append(i + 1 if state[i] == '-' else state[i])

    print('\n'.join([
        bar,
        cells_tmpl.format(cells[0], cells[1], cells[2]), bar,
        cells_tmpl.format(cells[3], cells[4], cells[5]), bar,
        cells_tmpl.format(cells[6], cells[7], cells[8]), bar
    ]))


# --------------------------------------------------
def has_won(cells):
    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for combo in winning:
        group = list(map(lambda i: cells[i], combo))
        for player in ['X', 'O']:
            if all(x == player for x in group):
                return player

    return None


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    players = ['X', 'O']
    initial_state = {'cells': list('-' * 9), 'player': players[0]}
    wins = {'X': 0, 'O': 0, 'Draw': 0}
    state = copy.deepcopy(initial_state)
    print_board(state['cells'])

    while (True):
        move = input('Player {}: What is your move (q to quit)? '.format(
            state['player'])).rstrip()

        if move == 'q':
            break

        if not move.isdigit():
            print('Move ({}) is not a digit'.format(move))
            continue

        move = int(move)

        if move < 1 or move > 9:
            print('Move ({}) must be between 1 and 9'.format(move))
            continue

        if state['cells'][move - 1] != '-':
            print('Cell "{}" has already been chosen'.format(move))
            continue

        state['cells'][move - 1] = state['player']
        print_board(state['cells'])

        # Conditions for stopping play
        winning_player = has_won(state['cells'])
        board_is_full = '-' not in state['cells']

        if winning_player or board_is_full:
            if winning_player:
                wins[winning_player] += 1
                print('Player {} has won!'.format(state['player']))
            elif board_is_full:
                wins['Draw'] += 1
                print('No more valid moves')

            play_again = input('Play again? [yN] ')
            if play_again.lower() == 'y':
                state = copy.deepcopy(initial_state)
                print_board(state['cells'])
                continue
            else:
                break

        state['player'] = 'O' if state['player'] == 'X' else 'X'

    for player in players:
        num = wins[player]
        print('Player {} won {} time{}. {}'.format(
            player,
            num,
            '' if num == 1 else 's',
            '(Loser!)' if num == 0 else '',
        ))

    print('There {} {} draw{}.'.format(wins['Draw'],
                                       'was' if wins['Draw'] == 1 else 'were',
                                       '' if wins['Draw'] == 1 else 's'))

    print('Done.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
