As with several other programs, we want to take our `text` either from the command line or from a file. I decided to put this logic into the `get_args` function and detect in there if `args.text` is a file and read it so that by the time I call `get_args` I already have the `text` I need. Since `--seed` has a default of `None`, I can directly pass it to `random.seed`. If the seed is `None`, it's the same as not setting the seed. If the seed is defined (and it must be an `int` because of the constraint in `argparse`), then it sets the seed properly.

Because I want to preserve the shape of the input text, I decided to handle the `text` line-by-line by calling `text.splitlines()`. If we are reading the "spiders" haiku, the first line is:

````
>>> line = 'Don’t worry, spiders,'
````

We need to break the line into "words" which we often do with `str.split`:

````
>>> line.split()
['Don’t', 'worry,', 'spiders,']
````

But that leaves punctation stuck to our words. Instead, we'll `import re` to get the regular expression module and split on word boundaries (`\b`):

````
>>> re.split(r'\b', line)
['', 'Don', '’', 't', ' ', 'worry', ', ', 'spiders', ',']
````

That actually breaks "Don't" into two words, but we'll just not worry about that. So let's think about how we'll scramble our words by starting with just one word.

## Scrambling one word

Given any particular "word" that:

1. looks like a string
2. is longer than 3 characters 

We want to scramble the middle of any string, where the "middle" is everything after the first character up to the second to last character. 

We can use list slices to extract part of a string. Since Python starts numbering at `0`, we use `1` to indicate the second character. The position of any string is `-1`:

````
>>> word = 'spiders'
>>> word[0]
's'
>>> word[-1]
's'
````

If we want a slice, we use the `list[start:stop]` syntax. Since the `stop` position is not included, we can get the `middle` like so:

````
>>> middle = word[1:-1]
>>> middle
'pider'
````

We can `import random` to get access to the `shuffle` method. You have to know that this method mutates the given list **in-place**, and that's going to cause a problem:

````
>>> import random
>>> random.shuffle(middle)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/kyclark/anaconda3/lib/python3.7/random.py", line 278, in shuffle
    x[i], x[j] = x[j], x[i]
TypeError: 'str' object does not support item assignment
````

Hey, wha' happan? This is a bit tricky to understand, but basically when we defined the `middle` variable, we were just *pointing to a part of a string*, and strings are immutable. We'd get same error if we did `random.shuffle('ooba')`. We need `middle` make a new `list` of the characters from `word`:

````
>>> middle = list(word[1:-1])
>>> middle
['p', 'i', 'd', 'e', 'r']
````

And that is something we can `shuffle`:

````
>>> random.shuffle(middle)
>>> middle
['r', 'e', 'p', 'i', 'd']
````

While writing the program, I found that the shuffling didn't always result in a different order, so I added a bit of logic to keep shuffling until I get something new. Another problem I encountered was creating an infinite loop while comparing my shuffled string to the original when the word was "keep" because the middle is "ee" and no matter how many times you shuffle that it will always be "ee", so I added a check that the unique `set` of letters in the middle is greater than 1:

````
>>> orig = list(word[1:-1])
>>> middle = orig.copy()
>>> if len(set(middle)) > 1:
...     while middle == orig:
...         random.shuffle(middle)
...
>>> middle
['p', 'i', 'd', 'r', 'e']
>>> middle
['r', 'e', 'p', 'i', 'd']
````

And now I can put the `word` back together with the original first and last characters:

````
>>> word = word[0] + ''.join(middle) + word[-1]
>>> word
'srepids'
````

## Scrambling all the words

Now I have a function `scramble(word)`:

````
>>> def scramble(word):
...     """For words over 3 characters, shuffle the letters in the middle"""
...     if len(word) > 3 and re.match(r'\w+', word):
...         orig = list(word[1:-1])
...         middle = orig.copy()
...         if len(set(middle)) > 1:
...             while middle == orig:
...                 random.shuffle(middle)
...         word = word[0] + ''.join(middle) + word[-1]
...     return word
...
````

And a way to break up each line into word-like piecies (using `re.split`). 

I need to apply a function to a list, and that is exactly what `map` does. For instance, I could `split` the line into words:

````
>>> line.split()
['Don’t', 'worry,', 'spiders,']
````

And `map` that into the `len` function to find the lengths of each element in the list. In order to evaluate the resulting `map` object, I have to use `list` in the REPL (but not in actual code):

````
>>> list(map(len, line.split()))
[5, 6, 8]
````

Instead, we'll `map` into our `scramble` function and split on word boundaries:

````
>>> list(map(scramble, re.split(r'\b', line)))
['', 'Don', '’', 't', ' ', 'wrory', ', ', 'sdeirps', ',']
````

And then put that `list` back together by joining on the empty string:

````
>>> ''.join(map(scramble, re.split(r'\b', line)))
'Don’t wrroy, sperdis,'
````

I do this for each line of text, printing the scrambled line, and that is the whole program.

If you don't like `map`, you can accomplish the same thing with a list comprehension:

````
>>> ''.join([scramble(w) for w in re.split(r'\b', line)])
'Don’t wrory, sdepris,'
````