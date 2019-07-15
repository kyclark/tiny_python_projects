As suggested, I wrote my `get_args` to handle all the user input validation. It's easy enough to check, for instance, if the `text` argument is actually a file and `open`/`read` it so as to return exactly what the rest of the program requires. I can also see if the `--symbol` is not exactly one character and use `parser.error` to print an error with the usage and then exit with a non-zero status.

Inside my `main`, I pass most of the arguments to the `count` function I described in the intro which is where most of the logic of the program is contained. If you wrote several functions to do each part or if you simply put all the logic in the `main`, that's fine (as long as you are passing the test suite). The advantage to me is that I can write a `test_count` function where I pass in some known text and ensure that I'm getting back the filtered, sorted results I expect. 

The first thing to notice about the `test_count` function is the text that it passes in:

````
>>> text = '"ab,Bc CC: dd_d-d"'
````

I only want to count the alphabetic characters, so how can I remove all the other stuff? I love to use regular expressions for this. I create a character class with `r'[a-zA-Z]'` (where `r''` creates a "raw" string), the brackets `[]` enclose the class, and `a-z` is the range of letters from lowercase `a` to lowercase `z` and then `A-Z` is the uppercase letters. The `re.findall` method will return a `list` of matching characters:

````
>>> import re
>>> re.findall(r'[a-zA-Z]', text)
['a', 'b', 'B', 'c', 'C', 'C', 'd', 'd', 'd', 'd']
````

Which is exactly what we need for `collections.Counter`:

````
>>> freqs = Counter(re.findall(r'[a-zA-Z]', text))
>>> freqs
Counter({'d': 4, 'C': 2, 'a': 1, 'b': 1, 'B': 1, 'c': 1})
````

So, in one line of code we filtered and counted the input text. Next, we can remove letters that are found too infrequently. A dictionary comprehension works well if we use `freq.items()` to get a list of tuples and only take those above the minimum:

````
>>> minimum = 2
>>> freqs = {k:v for k,v in freqs.items() if v >= minimum}
>>> freqs
{'C': 2, 'd': 4}
````

We need to find the highest value which is what the `max` function will do. Note that you should not call your variable `max` as it will then *overwrite the actual function* called `max`!

````
>>> high = max(freqs.values())
>>> highest
4
````

If the `highest` value is greater than the `width` argument, we should scale the values down. Again a dictionary comprehension works well:

````
>>> freqs = {k:int(v * scale) for k,v in freqs.items()}
>>> freqs
{'C': 1, 'd': 3}
````

Finally we need to sort the values either by the characters (which are the `keys`) or their frequencies (which are the `values`). We can use the `sorted` function on the `freqs.items()` to sort by key and value, but that would be case-senstive. To sort without regard to case, we need to convert the keys to upper- or lowercase first, but we still want to display the proper case. Note that `dict.items` returns a list of tuples:

````
>>> freqs.items()
dict_items([('C', 1), ('d', 3)])
````

We could add another field to the tuple that is the first value in lowercase:

````
>>> s = list(map(lambda t: (t[0].lower(), t[0], t[1]), freqs.items()))
>>> s
[('c', 'C', 1), ('d', 'd', 3)]
````

Then call `sorted` on that. We can then remove the first field from each tuple:

````
>>> list(map(lambda t: (t[1], t[2]), s))
[('C', 1), ('d', 3)]
````

The other sort is by values, so we can use a dictionary comprehension to reverse the keys and values before calling `sorted`:

````
>>> s = sorted([(v, k) for k, v in freqs.items()], reverse=True)
>>> s
[(3, 'd'), (1, 'C')]
````

And then reverse the tuples to put them back with `(character, count)`:

````
>>> list(map(lambda t: (t[1], t[0]), s))
[('d', 3), ('C', 1)]
````

Now it's a matter to `print` each item. I can use the `*` operator to repeat the `symbol` argument by the scaled count:

````
>>> symbol = '|'
>>> for c, num in freqs:
...     print('{} {:6} {}'.format(c, num, symbol * num))
...
d      3 |||
C      1 |
````

## Further

* Turn the histogram 90 degrees so that the characters are listed on the bottom and the bars go up
* You will use this code in the Pareto exercise to plot the distribution of resources over a given set of actors.
