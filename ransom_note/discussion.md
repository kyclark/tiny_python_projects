I like this problem because there are so many interesting ways to solve it. I know, I know, Python likes there to be "one obvious way" to solve it, but let's explore, shall we?

It's a common pattern in many of these problems that the input can either be given on the command line or in a file, so I have to defined the `text` argument as having `type=str`. In this version of the program, I decided to check in the `get_args` if the `text` is a file (`os.path.isfile(text)`), and, if so, to override the value of `args.text` with the result of reading the contents of the file. That way when I get to the `args = get_args()` line in my program, I've already gotten the text from the user, whether given on the command line or in a file.

I set the `--seed` optional `default` to Python's special `None` value which means nothing at all. As such, I can pass it directly to `random.seed` because setting the seed to `None` is the same as not setting it. Only if the user indicates a `--seed` value (which must be an `int` and which `argparse` will validate) will this affect the behavior of the program.

Assume that we have the following:

````
>>> text = 'The quick brown fox jumps over the lazy dog.'
````

We want to randomly upper- and lowercase the letters. As suggested in the description of the problem, we can use a `for` loop to iterate over each character. Here's one way to print an uppercase version of the `text`

````
>>> for char in text:
...     print(char.upper(), end='')
...
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
````

Let's use `random.choice` to make a binary selection:

````
>>> import random
>>> random.choice([True, False])
False
>>> random.choice([0, 1])
0
>>> random.choice(['blue', 'green'])
'blue'
````

Now use that to select whether to take the upper- or lowercase character. Note that this version relies on the idea of "truthiness" (cf appendix) where `0` is considered `False` and anything not zero (like `1`) is `True`. So if `random.choice([0, 1])` returns a `1` (or `True`) then we take `char.upper()` otherwise we take `char.lower()`:

````
>>> ransom = []
>>> for char in text:
...     ransom.append(char.upper() if random.choice([0, 1]) else char.lower())
...
>>> ''.join(ransom)
'The quIck brOwn Fox JumpS over ThE lAZY dOG.'
````

We can shorten this to one line of code if we use a list comprehension, essentially putting the `for` loop inside the brackets `[]` that create the `ransom` list:

````
>>> ransom = [c.upper() if random.choice([0, 1]) else c.lower() for c in text]
>>> ''.join(ransom)
'thE quicK bRowN foX JUmPs OVER tHe lAzY dog.'
````

All the code for deciding which case could go into a very small function which you could either write as a `lambda`:

````
>>> choose = lambda c: c.upper() if random.choice([0, 1]) else c.lower()
>>> choose('t')
'T'
````

Or the more standard `def` version:

````
>>> def choose(c):
...     return c.upper() if random.choice([0, 1]) else c.lower()
...
>>> choose('t')
't'
````

And then use that in your list comprehension. This version reads very well as is perhaps my favorite:

````
>>> ransom = [choose(c) for c in text]
>>> ''.join(ransom)
'thE QUicK broWN fOx JUmPS OVeR the lAZy doG.'
````

But I also quite like the `map` function which takes another function as the first argument which is applied to all the elements of second argument which is an iterable:

````
>>> ransom = map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(), text)
>>> ''.join(ransom)
'ThE qUiCk BROwn FoX JUMps oVER THe lAzY dog.'
````

And that cleans up very nicely if instead we used our named function. This version is the shortest and perhaps cleanest but does require the reader to understand `map`:

````
>>> ransom = map(choose, text)
>>> ''.join(ransom)
'thE QUIck BrOwN FOX jumPs oVeR thE lAZY dOg.'
````

It may seem silly to spend so much time working through five ways to solve what is an essientially trivial problem, but one of the goals in this book is to explore the various ideas available in Python. The first method is a very imperative, c-like solution while the list comprehensions are very Pythonic and the `map` versions borrow from the world of purely functional languages like Haskell.
