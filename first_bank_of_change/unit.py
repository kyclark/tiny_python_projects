from fboc import fmt_combo, join, figure


# --------------------------------------------------
def test_fmt_combo():
    """Test fmt_combo"""

    assert fmt_combo((2, 0, 0, 1)) == '2 quarters and 1 penny'
    assert fmt_combo((0, 1, 2, 2)) == '1 dime, 2 nickels, and 2 pennies'


# --------------------------------------------------
def test_join():
    """Test join"""

    assert join([]) == ''
    assert join(list('a')) == 'a'
    assert join(list('ab')) == 'a and b'
    assert join(list('abc')) == 'a, b, and c'
    assert join(list('abcd')) == 'a, b, c, and d'


# --------------------------------------------------
def test_figure():
    """Test figure"""

    assert figure(1, (0, 0, 0)) == (0, 0, 0, 1)
    assert figure(3, (0, 0, 0)) == (0, 0, 0, 3)
    assert figure(5, (0, 0, 0)) == (0, 0, 0, 5)
    assert figure(5, (0, 0, 1)) == (0, 0, 1, 0)
    assert figure(5, (0, 1, 1)) == ()
    assert figure(6, (0, 0, 1)) == (0, 0, 1, 1)
    assert figure(11, (0, 0, 2)) == (0, 0, 2, 1)
    assert figure(11, (0, 1, 2)) == ()
    assert figure(11, (0, 1, 0)) == (0, 1, 0, 1)
    assert figure(51, (2, 0, 0)) == (2, 0, 0, 1)
