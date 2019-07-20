# Blackjack 

What's a games book without a card game? Let's write a Python program called `blackjack.py` that plays an abbreviated game of Blackjack. Your program should accept a `-S|--stand` option (default `18`) for the value to "stand" on (not "hit" or take another card). Your program should also accept two flags (Boolean values) for `-p|--player_hits` and `-d|--dealer_hits` which will be explained shortly. You will need to accept a `-s|--seed` (default `None`) to set `random.seed`. As usual, you will also have a `-h|--help` option for usage statement:

````
$ ./blackjack.py -h
usage: blackjack.py [-h] [-d] [-p] [-S int] [-s int]

Blackjack

optional arguments:
  -h, --help           show this help message and exit
  -d, --dealer_hits    Dealer hits (default: False)
  -p, --player_hits    Player hits (default: False)
  -S int, --stand int  Stand on value (default: 18)
  -s int, --seed int   Random seed (default: None)
````

If run with a `--stand` value less than 1, it should create an error:

````
$ ./blackjack.py -S 0
usage: blackjack.py [-h] [-d] [-p] [-S int] [-s int]
blackjack.py: error: --stand "0" must be greater than 0
````

The program will create a deck of cards by combining symbols Unicode symbols ♥ (heart), ♠ (club), ♣ (spade), and ♦ (diamond) with the numbers 2-10 and the letters "A", "J", "Q," and "K". In order to pass the tests, you will need to first sort your deck by suite and value before you use the `random.shuffle` method.

Consider making a function called `make_deck` that does nothing but create the 52 cards. You may chose to model a "card" as a simple string as I did, e.g., `♥4`, or you may prefer to use a `tuple`, e.g., `('♥', '4')`, or even a `dict`, e.g., `{'suite': '♥', 'value': '4'}`. However you define a card, add and modify this function `test_make_deck` to ensure you get back a reasonable deck:

````
def test_make_deck():
    """Test for make_deck"""

    deck = make_deck()
    assert len(deck) == 52

    num_card = re.compile(r'\d+$')
    for suite in '♥♠♣♦':
        cards = list(filter(lambda c: c[0] == suite, deck))
        assert len(cards) == 13
        num_cards = list(filter(num_card.search, cards))
        assert len(num_cards) == 9
````

To deal, keep in mind how cards are actually dealt -- first one card to each of the players, then one to the dealer, then the players, then the dealer, etc. You might be tempted to use `random.choice` or something like that to select your cards, but you need to keep in mind that you are modeling an actual deck and so selected cards should no longer be present in the deck. If the `--player_hits` flag is present, deal an additional card to the player; likewise with the `--dealer_hits` flag.

In Blackjack, number cards are worth their numeric value, face cards are worth 10, and the Ace will be worth 1 for our game (though in the real game it can alternate between 1 and 11). Consider writing a function called `card_value` will return a `int` value of the card's worth. Add this `test_card_value` function:

````
def test_card_value():
    """Test card_value"""

    assert card_value('♥A') == 1

    for face in 'JQK':
        assert card_value('♦' + face) == 10

    for num in range(2, 11):
        assert card_value('♠' + str(num)) == num
````

When the program runs with no arguments, display the dealer and players hand along with a sum of the values of the cards. 

````
$ ./blackjack.py -s 1
Dealer [15]: ♥J ♠5
Player [10]: ♠9 ♦A
Dealer should hit.
Player should hit.
````

Here we see that both the dealer and player fall below the `--stand` value of `18`. Run again and have both players hit:

````
$ ./blackjack.py -s 1 -d -p
Dealer [23]: ♥J ♠5 ♠8
Player [14]: ♠9 ♦A ♣4
Dealer busts.
````

Here the dealer's hand went above 21, so he "busts." The player could stand to hit again, but, of course, need not since the dealer busted.

If we run with a different seed, we see different results:

````
$ ./blackjack.py -s 3
Dealer [19]: ♥K ♠9
Player [12]: ♣3 ♥9
Player should hit.
````

Here the dealer is recommended to stand because they have more than 18. Run with a higher `--stand` to change that:

````
$ ./blackjack.py -s 3 -S 20
Dealer [19]: ♥K ♠9
Player [12]: ♣3 ♥9
Dealer should hit.
Player should hit.
````

Now the dealer is recommended to hit, which seems unwise.

After dealing all the required cards and displaying the hands, the code should do (in order):

1. Check if the player has more than 21; if so, print 'Player busts! You lose, loser!' and `exit(0)`
2. Check if the dealer has more than 21; if so, print 'Dealer busts.' and `exit(0)`
3. Check if the player has exactly 21; if so, print 'Player wins. You probably cheated.' and `exit(0)`
4. Check if the dealer has exactly 21; if so, print 'Dealer wins!' and `exit(0)`
5. If the either the dealer or the player has less than 18, you should indicate "X should hit."

Hints:

* Use `parser.error` in `argparse` to create the error for a bad `--stand` value
* Use `itertools.product` to combine the suites and cards to make your deck.