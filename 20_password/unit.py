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

    state = random.getstate()
    random.seed(1)
    assert (ransom('Money') == 'moNeY')
    assert (ransom('Dollars') == 'DOLlaRs')
    random.setstate(state)


# --------------------------------------------------
def test_l33t():
    """Test l33t"""

    state = random.getstate()
    random.seed(1)
    assert l33t('Money') == 'moNeY{'
    assert l33t('Dollars') == 'D0ll4r5`'
    random.setstate(state)
