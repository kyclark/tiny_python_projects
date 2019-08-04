import io, random
from bacronym import group_words, make_definitions


# --------------------------------------------------
def test_group_words():
    """Test group_words()"""

    text = 'apple, "BANANA," The Coconut! Berry - APPLE; A cabbage.'
    words = io.StringIO(text)
    stop = 'a an the'.split()
    words_by_letter = group_words(words, stop)

    assert words_by_letter['a'] == ['apple']
    assert words_by_letter['b'] == ['banana', 'berry']
    assert words_by_letter['c'] == ['coconut', 'cabbage']
    assert 't' not in words_by_letter


# --------------------------------------------------
def test_make_definitions():
    """Test make_definitions()"""

    words = {
        'a': ['apple'],
        'b': ['banana', 'berry'],
        'c': ['coconut', 'cabbage']
    }

    random.seed(1)
    assert make_definitions('ABC', words) == ['Apple Banana Cabbage']
    random.seed(2)
    assert make_definitions('ABC', words) == ['Apple Banana Coconut']
    random.seed(3)
    assert make_definitions('AAA', words) == ['Apple Apple Apple']
    random.seed(4)
    assert make_definitions('YYZ', words) == ['? ? ?']
    random.seed(None)
