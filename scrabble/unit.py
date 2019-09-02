from scrabble import make_tiles, get_words


# --------------------------------------------------
def test_make_tiles():
    """Test make_tiles"""

    tiles = make_tiles()
    assert len(tiles) == 100
    assert len(list(filter(lambda c: c == 'A', tiles))) == 9


# --------------------------------------------------
def test_get_words():
    """Test get_words"""

    words = get_words(io.StringIO('apple banana cherry fig'))
    assert len(words[3]) == 1
    assert words[3][0] == ('fig', Counter('fig'))
    assert len(words[5]) == 1
    assert len(words[6]) == 2
