By using `argparse`, we can define all the parameters for the program along with reasonable defaults. The two flags for `--dealer_hits` and `--player_hits` will be `False` by default. The defaults for `--stand` and `--seed` will be 18 and `None`, respetively, and any values the user provides must be `int` values. 

## Making a deck

As mentioned in the intro, I chose to model my cards as strings where the suite is the first character and the value is the rest of the string, e.g., `♣10` is the 10 of clubs. I can create a `list` with the four Unicode strings for the suites:

````
>>> suites = list('♥♠♣♦')
>>> suites
['♥', '♠', '♣', '♦']
````

For the number values 2-10, I can use `range(2, 11)` (remembering that the upper limit is not inclusive), but I need to turn all these into `str` values, so I can `map` them into that function:

````
>>> list(map(str, range(2, 11)))
['2', '3', '4', '5', '6', '7', '8', '9', '10']
````

I can use the `+` operator to join that `list` to one with the face cards "A" (Ace), "J" (Jack), "Q" (Queen), and "K" ("King"):


This will produce a `list` of 52 tuples like ()

````
>>> values = list(map(str, range(2, 11))) + list('AJQK')
>>> values
['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']
````

I use `itertools.product` to cross the `suites` and `values` and get a `list` of 52 (4 suites times 13 values) which are tuples containing the suite and value:

````
>>> from itertools import product
>>> cards = list(product(suites, values))
>>> len(cards)
52
>>> cards[0]
('♥', '2')
````

Since I want those to be strings, I can `map` them into the function `''.join` to make them strings:

````
>>> cards = list(map(''.join, product(suites, values)))
>>> cards[0]
'♥2'
````

Finally I can put `sorted` around all this to order them before shuffling. (This is only for the purposes of testing so that our decks will be in the same order so that we will draw the same cards.)

````
>>> cards = list(sorted(map(''.join, product(suites, values))))
>>> cards[0]
'♠10'
````

I chose to call `random.shuffle` in my `make_deck` function. It's important to note the difference between how `sorted` *returns a new list* and `random.shuffle` *mutates the list in-place

````
>>> random.shuffle(cards)
>>> cards[0]
'♥J'
````

As suggested, all this code goes into a function called `make_deck` and I use the `test_make_deck` function in the intro to check it with `pytest`.

## Playing the game

To start the game, I need to deal one card to the player, one to the dealer, one to the player, one to the dealer. Since the `cards` is a `list`, will use `pop` to remove a card from the deck. You cannot use the `random` module's `choice` or `sample` functions because the card would not be removed from the deck and so could be dealt again. 

````
>>> p1, d1, p2, d2 = cards.pop(), cards.pop(), cards.pop(), cards.pop()
````

Note that `list.pop` by default removes elements from the *end* of the list. If you want to remove those at another position, you can provide an index, e.g., `0` to indicate the beginning of the list. It doesn't matter which end of `cards` we draw from, just so long as we both agree to draw from the same side.

I use a `list` to model each players "hand":

````
>>> player = [p1, p2]
>>> dealer = [d1, d2]
>>> player
['♦10', '♣6']
>>> dealer
['♥2', '♠10']
````

If the flags to hit the player or dealer are present, I `append` the results of using `pop` on the deck

````
>>> player_hits = True
>>> dealer_hits = False
>>> if player_hits:
...     player.append(cards.pop())
...
>>> if dealer_hits:
...     dealer.append(cards.pop())
...
>>> player
['♦10', '♣6', '♦7']
>>> dealer
['♥2', '♠10']
````

## Figuring hand value

So, given a list like `['♦10', '♣6', '♦7']` how do we add up the values of the cards? I chose to create a `card_value` function that gives me the value of any one card. I start off using a dictionary comprehension to associtate the string value of the integer cards to their integer values:

````
>>> vals = {str(i): i for i in range(2, 11)}
>>> vals
{'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10}
````

I can then `update` the dictionary with *another dictionary* of the face values, which is pretty cool:

````
>>> vals.update({'A': 1, 'J': 10, 'Q': 10, 'K': 10})
>>> from pprint import pprint as pp
>>> pp(vals)
{'10': 10,
 '2': 2,
 '3': 3,
 '4': 4,
 '5': 5,
 '6': 6,
 '7': 7,
 '8': 8,
 '9': 9,
 'A': 1,
 'J': 10,
 'K': 10,
 'Q': 10}
````

I expect the card has the suite as the first character, so the "value" of the card is anything *after* the first character:

````
>>> card = '♦10'
>>> val = card[1:]
>>> val
'10'
````

I then `assert` that the value is something in my `vals` dict:

````
>>> assert val in vals
````

The `assert` function returns nothing when it works; otherwise it throws an exception that would halt the program completely, which I actually want. If I were to have passed something that's not actually a "card" to the program, something is definitely wrong and needs to be fixed!

````
>>> assert 'X' in vals
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
````

If all goes well, I can `return` the value:

````
>>> def card_value(card):
...     vals = {str(i): i for i in range(2, 11)}
...     vals.update({'A': 1, 'J': 10, 'Q': 10, 'K': 10})
...     val = card[1:]
...     assert val in vals
...     return vals[val]
...
````

I can test it manually and with the `test_card_value` provided in the intro:

````
>>> card_value('♦10')
10
>>> card_value('♦A')
1
````

## Adding the card values

So to return to our question of how to add the values in a hand like `['♦10', '♣6', '♦7']`, we can `map` each card into our `card_value` function and then `sum` them:

````
>>> player
['♦10', '♣6', '♦7']
>>> sum(map(card_value, player))
23
````

## Printing the hands and outcomes

I can print out each of the hands and their values:

````
>>> player_hand = sum(map(card_value, player))
>>> dealer_hand = sum(map(card_value, dealer))
>>> print('Dealer [{:2}]: {}'.format(dealer_hand, ' '.join(dealer)))
Dealer [12]: ♥2 ♠10
>>> print('Player [{:2}]: {}'.format(player_hand, ' '.join(player)))
Player [23]: ♦10 ♣6 ♦7
````

After printing the hands, I go through the checklist in the intro, checking who went "bust," who got 21, who should hit, and so forth.