from hangman import get_words, play


# --------------------------------------------------
def test_get_words():
    """Test get_words"""

    text = 'Apple banana COW da epinephrine'
    assert get_words(io.StringIO(text), 1, 20) == text.lower().split()
    assert get_words(io.StringIO(text), 5, 10) == ['apple', 'banana']
    assert get_words(io.StringIO(text), 3, 10) == ['apple', 'banana', 'cow']


# --------------------------------------------------
def test_play():
    """Test play"""

    assert play({'word': 'banana', 'inputs': list('abn')}) == True
    assert play({'word': 'banana', 'inputs': list('abcdefghijklm')}) == False
    assert play({'word': 'banana', 'inputs': list('???')}) == True
    assert play({'word': 'banana', 'inputs': list('!')}) == False


