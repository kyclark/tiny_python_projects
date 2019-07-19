# Ready, Set, Go!

We programmed "Blackjack," a card game using a standard deck of 52 playing cards which differed in two attributes: the suites (e.g., "Hearts"), and the card value (e.g., "10" or "Jack"). Now we're going to look at another card game that uses 81 cards which differ in 4 attributes each of which can have 3 values:

1. Number (1, 2, 3)
2. Color (Red, Green, Purple)
3. Shading (Solid, Striped, Putlined)
4. Shape (Oval, Squiggle, Diamond)

Look up the game online to see examples of the cards. Even better, get a deck and play with your friends!

In this exercise, we'll write a Python program called `set.py` that plays the Set card game. The only argument your program needs to take is a `-s|--seed` to pass to `random.seed`. My version additionally takes a `-d|--debug` flag to log messages to `.log` to help you see how it works. When run with the `-h|--help` flag, it should print a usage:

````
$ ./set.py -h
usage: set.py [-h] [-s int] [-d]

Argparse Python script

optional arguments:
  -h, --help          show this help message and exit
  -s int, --seed int  Random seed (default: None)
  -d, --debug         Debug (default: False)
````

Otherwise, your program will need to create a deck of 81 cards by crossing all 4 attributes with each of the 3 values (`3 ** 4 == 81`), draw 12 at random, and find sets which are defined as any three cards where each of the 4 attributes above is the *same* among all 3 cards or *different* in every one. For instance, either there are the same number of shapes on all 3 cards or there is a different number on each. In the following example, the first set has different values for the number, color, and shape but the same value for the shading:

````
$ ./set.py -s 1
Set 1
1 Green Outlined Diamond
2 Red Outlined Oval
3 Purple Outlined Squiggle
Set 2
1 Green Outlined Squiggle
2 Red Outlined Squiggle
3 Purple Outlined Squiggle
````

## Creating and sorting the deck

There are dozens of ways you could chose to solve this, but, in order to pass the test suite, we will have to do a couple of things the same way. For one, we both need to use the same method to sort and shuffle our decks and then select the 12 cards. 

To create the deck, you could manually enter all 81 cards, but that way lies madness. I suggest you use `itertools.product` to cross four lists, one for each of the numbered attributes above and each containing their three values. This returns a `list` of `tuple` values, which seems like a perfect way to model the cards:

````
>>> from itertools import product
>>> list(product('AB', '12'))
[('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]
````

However you chose to represent each card, the `list` of cards should be sorted by number color, shading, and shape. Consider making a function called `make_deck` that will create the deck and return it sorted properly. Then add something like this function to run with `pytest`. That is, I chose to use tuples for each card, so I'm checking that the first and last values in the `deck` are my expected tuples:

````
def test_make_deck():
    """Test make_deck"""

    deck = make_deck()
    assert len(deck) == 81
    assert deck[0] == ('1', 'Green', 'Outlined', 'Diamond')
    assert deck[-1] == ('3', 'Red', 'Striped', 'Squiggle')
````

Once you have a sorted deck, use `random.shuffle` to sort it, then use `random.sample` to select 12 cards. With that, we should both have identical cards for the tests.

## Finding a set

Think about how you might decide if any three of cards forms a set. I would suggest thinking backwards from this test function which I suggest you include in your program:

````
def test_is_set():
    """Test is_set"""

    assert is_set([tuple('ABCD'), tuple('ABCD'), tuple('ABCD')])
    assert is_set([tuple('ABCD'), tuple('EFGH'), tuple('IJKL')])
    assert not is_set([tuple('ABCD'), tuple('ABCD'), tuple('ABCE')])
    assert is_set([
        ('1', 'Green', 'Outlined', 'Diamond', '1'),
        ('Green', 'Outlined', 'Squiggle'),
        ('1', 'Green', 'Outlined', 'Oval')
    ])
    assert is_set([
        ('1', 'Green', 'Outlined', 'Diamond'),
        ('2', 'Red', 'Striped', 'Squiggle'),
        ('3', 'Purple', 'Solid', 'Oval')
    ])
    assert not is_set([
        ('1', 'Green', 'Outlined', 'Diamond'),
        ('2', 'Red', 'Striped', 'Squiggle'),
        ('3', 'Green', 'Solid', 'Oval')
    ])
```` 

If you represent your cards as strings, dictionaries, sets, or some other object, you should modify the test to reflect your design decisisons. Still, the ideas are the same. The first test assumes that I pass in 3 identical structures have the same 4 elements, `A`, `B`, `C`, and `D`. That should be a set. In the second test, all 3 structures are entirely different, so that's a set. In the third, the fourth element of the last structure is composed of the values `D`, `D`, and `E`, so that's not a set. Can you write the function `is_set` that will return a `bool` that indicates whether or not the list is a set?

Once you have that function job, you need to examine all possible combinations of 3 cards. I suggest you use `itertools.combinations` for this. Then you can `filter` the combinations for those where `is_set` is `True`.

Print out each set of cards with "Set N" and then the three cards in the set each on a new line. The test suite doesn't card what order the sets are printed, but the cards need to be `sorted`.
