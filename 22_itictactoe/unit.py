from itictactoe import format_board, find_winner
import random


# --------------------------------------------------
def test_board_no_state():
    """makes default board"""

    board = """
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
""".strip()

    assert format_board('.' * 9) == board


# --------------------------------------------------
def test_board_with_state():
    """makes board"""

    board = """
-------------
| 1 | 2 | 3 |
-------------
| O | X | X |
-------------
| 7 | 8 | 9 |
-------------
""".strip()

    assert format_board('...OXX...') == board


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
            assert find_winner(test_state) == player


# --------------------------------------------------
def test_losing():
    """test losing states"""

    losing_state = list('XXOO.....')

    for i in range(10):
        random.shuffle(losing_state)
        assert find_winner(''.join(losing_state)) == None
