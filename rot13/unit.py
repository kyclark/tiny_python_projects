import random
from rot13 import rot, pad_out, nth


# --------------------------------------------------
def test_rot():
    """Test rot"""

    assert rot('a', 'abcd', 1) == 'b'
    assert rot('b', 'abcd', 3) == 'a'
    assert rot('c', 'abcd', 5) == 'd'
    assert rot('x', 'abcd', 1) == 'x'


# --------------------------------------------------
def test_pad_out():
    """Test pad_out"""

    random.seed(1)
    a = 'ABCDEFG'
    assert pad_out(a, 2) == 'AB CD EF GE'
    assert pad_out(a, 3) == 'ABC DEF GSZ'
    assert pad_out(a, 4) == 'ABCD EFGY'
    assert pad_out(a, 5) == 'ABCDE FGCID'
    assert pad_out(a, 6) == 'ABCDEF GPYOPU'
    random.seed(None)


# --------------------------------------------------
def test_nth():
    """Test nth"""

    a = 'abcdefghij'
    assert [a[i] for i in nth(2, a)] == list('bdfhj')
    assert [a[i] for i in nth(3, a)] == list('cfi')
    assert [a[i] for i in nth(4, a)] == list('dh')
    assert [a[i] for i in nth(5, a)] == list('ej')
