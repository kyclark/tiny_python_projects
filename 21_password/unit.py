import random
from password import clean, ransom, l33t


# --------------------------------------------------
def test_clean():
    """Test clean"""

    assert clean('') == ''
    assert clean("states,") == 'states'
    assert clean("Don't") == 'Dont'


# --------------------------------------------------
def test_ransom():
    """Test ransom"""

    random.seed(1)
    assert (ransom('Money') == 'moNeY')
    assert (ransom('Dollars') == 'DOLlaRs')
    random.seed(None)


# --------------------------------------------------
def test_l33t():
    """Test l33t"""

    random.seed(1)
    assert (l33t('Money') == 'm0N3Y{')
    assert (l33t('Dollars') == 'D0ll4r5`')
    random.seed(None)
