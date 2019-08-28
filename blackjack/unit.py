from blackjack import card_value, make_deck


# --------------------------------------------------
def test_card_value():
    """Test card_value"""

    assert card_value('♥A') == 1

    for face in 'JQK':
        assert card_value('♦' + face) == 10

    for num in range(2, 11):
        assert card_value('♠' + str(num)) == num


# --------------------------------------------------
def test_make_deck():
    """Test for make_deck"""

    deck = make_deck()
    assert len(deck) == 52

    num_card = re.compile(r'\d+$')
    for suite in list('♥♠♣♦'):
        cards = list(filter(lambda c: c[0] == suite, deck))
        assert len(cards) == 13
        num_cards = list(filter(num_card.search, cards))
        assert len(num_cards) == 9



