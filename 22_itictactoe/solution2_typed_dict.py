#!/usr/bin/env python3
""" Interactive Tic-Tac-Toe using TypedDict """

from typing import List, Optional, TypedDict


class State(TypedDict):
    board: str
    player: str
    quit: bool
    draw: bool
    error: Optional[str]
    winner: Optional[str]


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    state = State(board='.' * 9,
                  player='X',
                  quit=False,
                  draw=False,
                  error=None,
                  winner=None)

    while True:
        print("\033[H\033[J")
        print(format_board(state['board']))

        if state['error']:
            print(state['error'])
        elif state['winner']:
            print(f"{state['winner']} has won!")
            break

        state = get_move(state)

        if state['quit']:
            print('You lose, loser!')
            break
        elif state['draw']:
            print('No winner.')
            break


# --------------------------------------------------
def get_move(state: State) -> State:
    """Get the player's move"""

    player = state['player']
    cell = input(f'Player {player}, what is your move? [q to quit]: ')

    if cell == 'q':
        state['quit'] = True
        return state

    if not (cell.isdigit() and int(cell) in range(1, 10)):
        state['error'] = f'Invalid cell "{cell}", please use 1-9'
        return state

    cell_num = int(cell)
    if state['board'][cell_num - 1] in 'XO':
        state['error'] = f'Cell "{cell}" already taken'
        return state

    board = list(state['board'])
    board[cell_num - 1] = player

    return State(
        board=''.join(board),
        player='O' if player == 'X' else 'X',
        winner=find_winner(board),
        draw='.' not in board,
        error=None,
        quit=False,
    )


# --------------------------------------------------
def format_board(board: str) -> str:
    """Format the board"""

    cells = [str(i) if c == '.' else c for i, c in enumerate(board, 1)]
    bar = '-------------'
    cells_tmpl = '| {} | {} | {} |'
    return '\n'.join([
        bar,
        cells_tmpl.format(*cells[:3]), bar,
        cells_tmpl.format(*cells[3:6]), bar,
        cells_tmpl.format(*cells[6:]), bar
    ])


# --------------------------------------------------
def find_winner(board: List[str]) -> Optional[str]:
    """Return the winner"""

    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for player in ['X', 'O']:
        for i, j, k in winning:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player

    return None


# --------------------------------------------------
if __name__ == '__main__':
    main()
