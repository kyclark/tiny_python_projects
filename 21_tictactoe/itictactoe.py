#!/usr/bin/env python3
"""Interactive Tic-Tac-Toe"""


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    state = {'board': list('.' * 9), 'player': 'X'}

    while True:
        print(format_board(state))
        state = get_move(state)
        winner = find_winner(state)

        if winner:
            print(format_board(state))
            print(f'{winner} has won!')
            break
        elif '.' not in state['board']:
            print(format_board(state))
            print('No winner.')
            break


# --------------------------------------------------
def get_move(state):
    """Play"""

    player = state['player']
    cell = input(f'Player {player}, what is your move?: ')

    if not (cell.isdigit() and int(cell) in range(1, 10)):
        print(f'Invalid cell "{cell}", please use 1-9')
        return state

    cell = int(cell)
    board = state['board']
    if board[cell - 1] in 'XO':
        print('Cell "{cell}" already taken')
        return state

    board[cell - 1] = player
    return {'board': board, 'player': 'O' if player == 'X' else 'X'}


# --------------------------------------------------
def format_board(state):
    """Format the board"""

    cells = []
    for i, char in enumerate(state['board'], start=1):
        cells.append(str(i) if char == '.' else char)

    bar = '-------------'
    cells_tmpl = '| {} | {} | {} |'
    return '\n'.join([
        bar,
        cells_tmpl.format(cells[0], cells[1], cells[2]), bar,
        cells_tmpl.format(cells[3], cells[4], cells[5]), bar,
        cells_tmpl.format(cells[6], cells[7], cells[8]), bar
    ])


# --------------------------------------------------
def find_winner(state):
    """Return the winner"""

    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    board = state['board']
    for player in ['X', 'O']:
        for i, j, k in winning:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player


# --------------------------------------------------
if __name__ == '__main__':
    main()
