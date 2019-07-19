There's very little to see in `get_args`, just defining the `-s|--seed` and `-d|--debug` options, the former of which gets passed to `random.seed`. As in many other programs, I set up `logging.basicConfig` to log to a `filename='.log'` (so it will normally be hidden from view) using `filemode='w'` (so it will be overwritten each time it runs), and setting the `level` either to `logging.DEBUG` or `logging.CRITICAL` depending on the presence of the `--debug` flag.

As stated in the introduction, I chose to use the list of tuples returned from `itertools.product`. I also have chosen to include some type annotations by bringing in the `typing` module. This allows me to use the `mypy` tool to check for common errors. It also helps me think about the inputs and return values for my functions. The function `make_deck` has no inputs and returns a list of tuples:

````
>>> from itertools import product
>>> from typing import List, Tuple
>>> def make_deck() -> List[Tuple[str, str, str, str]]:
...     numbers = ('1', '2', '3')
...     colors = ('Red', 'Purple', 'Green')
...     shadings = ('Solid', 'Striped', 'Outlined')
...     shapes = ('Oval', 'Squiggle', 'Diamond')
...     return sorted(product(numbers, colors, shadings, shapes))
...
>>> len(make_deck())
81
````

As expected, I get 81 cards from the function. I can use the `test_make_deck` function to do a little more probing.

The next function I tackled was `is_set` that takes 3 cards and looks at the 4 attributes. The order of the attributes is actually not important for this function. That is, we don't care that "number" is first, we only care that all the first elements are exactly the same or entirely different. The data structure that comes to my mind is, not surprisingly, a `set`. If all the elements of the `set` are the same, then the length of the set will be `1`; if they are entirely different, then the length will be `3`.

I can use the `zip` function to group all the first elements together, then all the second elements, and so forth.

````
>>> cards = [tuple('ABCD'), tuple('ABCD'), tuple('ABCD')]
>>> list(zip(*cards))
[('A', 'A', 'A'), ('B', 'B', 'B'), ('C', 'C', 'C'), ('D', 'D', 'D')]
````

And then I want to apple the `set` function to each element in that `list`, so I can use `map`:

````
>>> sets = list(map(set, zip(*cards)))
>>> sets
[{'A'}, {'B'}, {'C'}, {'D'}]
````

These cards do comprise a "set" if the `len` of `all` of the `sets` are either `1` or `3`:

````
>>> all([len(s) in [1,3] for s in sets])
True
````

We can put this into a function:

````
>>> def is_set(cards: List[tuple]) -> bool:
...     sets = map(set, zip(*cards))
...     return all([len(s) in [1,3] for s in sets])
...
````

And then test it:

````
>>> is_set([tuple('ABCD'), tuple('ABCD'), tuple('ABCD')])
True
>>> is_set([tuple('ABCD'), tuple('ABCD'), tuple('ABCE')])
False
````

With those functions in place, we can make a deck of cards, shuffle them, randomly sample 12 cards, and then select only those where `is_set` is `True`:

````
>>> import random
>>> from itertools import combinations
>>> random.seed(1)
>>> deck = make_deck()
>>> random.shuffle(deck)
>>> hand = random.sample(deck, k=12)
>>> sets = filter(is_set, combinations(hand, 3))
````

If you copy and paste this code, keep in mind that the `filter` function returns a `filter` *object* which is *lazy*, so if you use, for example, `list` to force the REPL to evaluate and print the filtered sets, you will have exhausted the generation of the results. You can assign `sets` to `list(filter(...))` to get something you can `print` and get the `len` and iterate repeatedly. 

Keep in mind that `sets` is a `list` of the 3-tuples of cards that form sets. We still need to iterate over the `sets` and print them out with the cards `sorted`:

````
>>> for i, combo in enumerate(sets, start=1):
...     print(f'Set {i}')
...     print('\n'.join(sorted(map(' '.join, combo))))
...
Set 1
1 Green Outlined Diamond
2 Red Outlined Oval
3 Purple Outlined Squiggle
Set 2
1 Green Outlined Squiggle
2 Red Outlined Squiggle
3 Purple Outlined Squiggle
````

I will confess that my first solution was considerably more complicated involving a custom `class` to represent a `Card` and using one-hot encoding and bit-wise addition to find sets. After writing that version and then sleeping on it, I was moved to create a far simpler solution, in part because of these ideas:

> Sometimes, the elegant implementation is just a function.  Not a method.  Not a class.  Not a framework.  Just a function. -- John Carmack

> Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away. -- Antoine de Saint-Exupery

A big leap was in thinking of sets as `ABCD` rather than `3 Purple Outlined Squiggle` and then realizing that the `list(tuple)` structure returned by `itertools.product` was the simplest data structure that solved 90% of my design. My first implementation was about 1/3 longer than this final version which I think reads considerably better.
