from gibberish import get_kmers, read_training

# --------------------------------------------------
def test_get_kmers():
    """Test get_kmers"""

    assert get_kmers('abcd') == list('abcd')
    assert get_kmers('abcd', 2) == ['ab', 'bc', 'cd']
    assert get_kmers('abcd', 3) == ['abc', 'bcd']
    assert get_kmers('abcd', 4) == ['abcd']
    assert get_kmers('abcd', 5) == []



# --------------------------------------------------
def test_read_training():
    """Test read_training"""

    text = 'The quick brown fox jumps over the lazy dog.'

    expected3 = {
        'qui': ['c'],
        'uic': ['k'],
        'bro': ['w'],
        'row': ['n'],
        'jum': ['p'],
        'ump': ['s'],
        'ove': ['r'],
        'laz': ['y']
    }
    assert read_training([io.StringIO(text)], k=3) == expected3

    expected4 = {'quic': ['k'], 'brow': ['n'], 'jump': ['s']}
    assert read_training([io.StringIO(text)], k=4) == expected4


