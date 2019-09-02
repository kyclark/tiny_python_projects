from more import encode_word, decode_word

# --------------------------------------------------
def test_encode_word():
    """Test Encoding"""

    assert encode_word('sos', ENCODE_ITU) == '... --- ...'
    assert encode_word('sos', ENCODE_MORSE) == '... .,. ...'


# --------------------------------------------------
def test_decode_word():
    """Test Decoding"""

    assert decode_word('... --- ...', DECODE_ITU) == 'SOS'
    assert decode_word('... .,. ...', DECODE_MORSE) == 'SOS'


# --------------------------------------------------
def test_roundtrip():
    """Test En/decoding"""

    random_str = lambda: ''.join(random.sample(string.ascii_lowercase, k=10))
    for _ in range(10):
        word = random_str()
        for encode_tbl, decode_tbl in [(ENCODE_ITU, DECODE_ITU),
                                       (ENCODE_MORSE, DECODE_MORSE)]:

            assert word.upper() == decode_word(encode_word(word, encode_tbl),
                                               decode_tbl)


