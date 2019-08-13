from tictactoe import make_board, get_winner


# --------------------------------------------------
def test_make_board1():
    """Test make_board"""

    expected = """
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
    """.strip()

    assert make_board('.' * 9) == expected


# --------------------------------------------------
def test_make_board2():
    """Test make_board"""

    expected = """
-------------
| 1 | 2 | X |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | X |
-------------
    """.strip()

    assert make_board('..X.....X') == expected


# --------------------------------------------------
def test_make_board3():
    """Test make_board"""

    expected = """
-------------
| X | O | 3 |
-------------
| O | 5 | X |
-------------
| 7 | O | X |
-------------
    """.strip()

    assert make_board('XO.O.X.OX') == expected

# --------------------------------------------------
def test_get_winner():
    """Test get_winner"""

    assert get_winner('XXX......') == 'X'
    assert get_winner('O..O..O..') == 'O'
    assert get_winner('...O..X..') == ''
