from rummikub import make_tiles, diffs, is_set


# --------------------------------------------------
def test_make_tiles():
    """Test make_tiles"""

    tiles = make_tiles()
    assert len(tiles) == 104
    assert len(list(filter(lambda tile: tile[0] == 'R', tiles))) == 26
    assert len(list(filter(lambda tile: tile[1] == 1, tiles))) == 8
    assert len(
        list(filter(lambda tile: tile[0] == 'K' and tile[1] == 10,
                    tiles))) == 2


# --------------------------------------------------
def test_diffs():
    """Test diffs"""

    assert diffs([1, 2, 3]) == [1, 1]
    assert diffs([4, 1, 6]) == [3, 2]
    assert diffs([1, 1, 1]) == [0, 0]


# --------------------------------------------------
def test_is_set():
    """Test is_set"""

    assert is_set([('R', 1), ('Y', 1), ('K', 1)])
    assert is_set([('B', 7), ('Y', 7), ('K', 7), ('R', 7)])
    assert not is_set([('Y', 1), ('K', 1)])
    assert not is_set([('B', 8), ('Y', 7), ('K', 7), ('R', 7)])

    assert is_set([('R', 1), ('R', 2), ('R', 3)])
    assert is_set([('K', 3), ('K', 4), ('K', 5), ('K', 7), ('K', 6)])
    assert not is_set([('K', 2), ('K', 4), ('K', 5), ('K', 7), ('K', 6)])
