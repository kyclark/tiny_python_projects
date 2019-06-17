Let's start with a short look at `get_args` where I've decided to move the validation of the single `value` argument into this function rather than getting the arguments in `main` and checking there. We can use `argparse` to ensure the user provides an `int` value, but there's no `type` to say that it must be in our desired range; however, I can use the `parser.error` function on line 22 to trigger the normal fail-with-usage behaviour we normally get from `argparse`. From the standpoint of the calling code on line 32, all the work to coerce and validate the user happens in `get_args`. If we make it past line 32, then all must have been good and we can just focus on the task at hand.

I'd like to mention that I worked for a couple of days on this solution. I tried many different approaches before settling on the way I solved this problem, so what I do next may not be at all how you solved the problem. My idea was to find how many possible nickels, dimes, and quarters are in the given `value` and then find every combination of those values to see which ones sum to the `value` or less. To do this, I can use the `//` operator to find the integer division of the `value` by each of 5, 10, and 25 for nickels, dimes, and quarters, e.g.:

````
>>> value = 13
>>> value // 5
2
````

Finds there are two nickels in 13 cents. I construct a range that includes 0, 1, and 2 like so:

````
>>> nickels = range((value // 5) + 1)
>>> nickels
range(0, 3)
>>> list(nickels)
[0, 1, 2]
````

I used the `itertools.product` function and three ranges for nickels, dimes, and quarters to find every possible combination of every number of coins

````
>>> dimes = range((value // 10) + 1)
>>> quarters = range((value // 25) + 1)
>>> from itertools import product
>>> list(product(nickels, dimes, quarters))
[(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0), (2, 0, 0), (2, 1, 0)]
````

I want to include 0 of every coin so that I can make up the remainder in pennies. Let's jump ahead to the `figure` function to see how I wanted to use these values. Because `product` gives me a list of 3-tuples, I decided to pass `figure` the `value` and then a `coins` tuple that I unpack on line 66. I `sum` the values of the `nickels`, `dimes`, and `quarters` on line 67 and see if that is less than or equal to the `value`. If so, I get the number of pennies by subtracting the sum of the larger coins and return a 4-tuple with the number of each coin. If the previous sum was larger than the `value`, we don't bother defining the `return` of the function and so `None` is used.

Going back to line 37 where I want to call `figure` for each of the combinations returned by `product`, I use a list comprehension combined with a `map` which may seem rather dense but works quite well.  The `map` wants a function and a list of items to apply the function. There's a slight problem in that the `figure` function wants 2 arguments -- the `value` and the 3-tuple. I could have written the `map` using a `lambda`:

````
>>> def figure(value, coins):
...     nickels, dimes, quarters = coins
...     big_coins = sum([5 * nickels, 10 * dimes, 25 * quarters])
...     if big_coins <= value:
...         return (quarters, dimes, nickels, value - big_coins)
...
>>> list(map(lambda c: figure(value, c), product(nickels, dimes, quarters)))
[(0, 0, 0, 13), (0, 1, 0, 3), (0, 0, 1, 8), None, (0, 0, 2, 3), None]
````

But I thought it would be cleaner to create a partial application of the `figure` function with the `value` already bound. The `functools.partial` is exactly the tool we need and then we only need to pass in the 3-tuple of the coins:

````
>>> from functools import partial
>>> fig = partial(figure, value)
>>> fig((1,0,0))
(0, 0, 1, 8)
````

And so now I can use this `partial` function in my `map`:

````
>>> list(map(fig, product(nickels, dimes, quarters)))
[(0, 0, 0, 13), (0, 1, 0, 3), (0, 0, 1, 8), None, (0, 0, 2, 3), None]
````

Notice how we get some `None` values returned. Remember, this is because some of the combinations we are trying are too large, e.g., the maximum number of all the coins will be too large. So, to filter out those value, I can use a list comprehension with a guard at the end:

````
>>> combos = [c for c in map(fig, product(nickels, dimes, quarters)) if c]
>>> combos
[(0, 0, 0, 13), (0, 1, 0, 3), (0, 0, 1, 8), (0, 0, 2, 3)]
````

I could have used a `filter` for this, but it just doesn't seem to read as well:

````
>>> list(filter(lambda c: c, map(fig, product(nickels, dimes, quarters))))
[(0, 0, 0, 13), (0, 1, 0, 3), (0, 0, 1, 8), (0, 0, 2, 3)]
````

This is a list of 4-tuples representing the number of quarters, dimes, nickels, and pennies that will sum to `13`. We still need to report back to the user, so that is the purpose of the `fmt_combo` function. Given that 4-tuple, I want to report, e.g., "1 quarter" or "3 dimes", so I need to know the value of the denomination and the singular/plural versions of name of the denomination. I use the `zip` function to pair the coin denominations with their values:

````
>>> combo = (0, 0, 0, 13)
>>> list(zip(('quarter', 'dime', 'nickel', 'penny'), combo))
[('quarter', 0), ('dime', 0), ('nickel', 0), ('penny', 13)]
````

The `plural` version of each name is made by adding `s` except for `penny`, so line 53 handles that. If the denomination is not in the `combo` (e.g., here we have only pennies), then we skip those by using `if val` where `val` will be the number of coins. The integer value `0` will evaluate to `False` in a Boolean context, so only those with a non-zero value will be included. I decided to create a `list` of the strings for each denomination, so I `append` to that list the `val` plus the correct singular or plural version of the name, finally returning that list joined on comma-space (`', '`). 

Finally lines 39-43 are left to formatting the report to the user, being sure to provide feedback that includes the original `value` ("If you give me ...") and an enumerated list of all the possible ways we could make change. The test suite does not bother to check the order in which you return the combinations, only that the correct number are present and they are in the correct format.