# Ready, Set, Go!

We programmed "Blackjack," a card game using a standard deck of 52 playing cards which differed in two attributes: the suites (e.g., "Hearts"), and the card value (e.g., "10" or "Jack"). Now we're going to look at another card game that uses 81 cards which differ in 4 attributes each of which can have 3 values:

1. Color (red, green, purple)
2. Shape (oval, squiggle, diamond)
3. Number (1, 2, 3)
4. Shading (solid, striped, outlined)

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
  2: 1 Green Outlined Diamond
  6: 3 Purple Outlined Squiggle
  8: 2 Red Outlined Oval
Set 2
  4: 2 Red Outlined Squiggle
  6: 3 Purple Outlined Squiggle
  9: 1 Green Outlined Squiggle
````

## Creating and sorting the deck

There are dozens of ways you could chose to solve this, and it's unlikely you would stumble upon my particular solution. In order to pass the test suite, we will have to do a couple of things the same way. For one this, we both need to use the same method to sort and shuffle our decks and then select the 12 cards. 

To create the deck, you could manually enter all 81 cards, but that way lies madness. I suggest you use `itertools.product` to cross four lists, one for each of the numbered attributes above and each containing their the three values. The problem comes in sorting the deck, and so let's just agree to sort the cards by the string representation which, as shown above, will be `number color shading shape`, e.g., "3 Purple Outlined Squiggle." 

There are many ways you could represent the idea of a "card" in your program. You could use a `tuple` of four strings which would sort properly and allow you to access each individual field for purposes of comparing cards. You'll have to remember the location of each field which is not too onerous, but still you might rather choose to use a `dict` with named fields and a full string of the values for sorting. I happened to choose a `class` with the `@dataclass` decorator that has a special `__str__` method to stringify the `Card` class. 

Consider making a function called `make_deck` that will create the deck (however you represent it) and return it sorted properly. Then add this function to run with `pytest`:

````
def test_make_deck():
    """Test make_deck"""

    deck = make_deck()
    assert len(deck) == 81
    assert str(deck[0]) == '1 Green Outlined Diamond'
    assert str(deck[-1]) == '3 Red Striped Squiggle'
````

Once you have a sorted deck, use `random.shuffle` to sort it, then use `random.sample` to select 12 cards. With that, we should both have identical cards for the tests.

## Finding a set

If you run `solution.py -d`, you can see a sample hand of 12 cards:

````
DEBUG:root:hand =
1 Red Outlined Oval
1 Red Outlined Squiggle
1 Green Outlined Diamond
3 Red Striped Diamond
2 Red Outlined Squiggle
3 Green Outlined Oval
3 Purple Outlined Squiggle
1 Purple Solid Oval
2 Red Outlined Oval
1 Green Outlined Squiggle
1 Purple Solid Squiggle
2 Green Solid Diamond
````

Your job is to look at all possible combinations of 3 cards, and I suggest you use `itertools.combinations` for this. Any 3 cards form a set if each attribute is exactly the same or entirely different. This particular has 2 sets. Can you find them manually? How will you write code to determine if cards are a set? How will you represent each attribute?