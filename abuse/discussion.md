![Erak! The captain is a corrupt, irksome fiend!](images/parrot.png)

## get_args

More than half of my solution is just in defining the program's arguments to `argparse`. The effort is well worth the result, because `argparse` will ensure that each argument is a valid integer value because I set `type=int`. Notice there are no quotes around the `int` -- it's not the string `'int'` but a reference to the class in Python. You can use the `type` function in Python to find out how Python represents a value:

````
>>> type(int)
<class 'type'>
>>> type('int')
<class 'str'>
````

For `--adjectives` and `--number`, I can set reasonable defaults so that no input is *required* from the user but the values are easily overridden. This makes your program dynamic, interesting, and testable. How do you know if your values are being used correctly unless you change them and test that the proper change was made in your program. Maybe you started off hardcoding the number of insults and forgot to change the `range` to use a variable. Without changing the input value and testing that the number of insults changed accordingly, it might be a user who discovers your bug, and that's somewhat embarrassing.

Another reason I quite like `argparse` is that, if I find there is a problem with an argument, I can use `parser.error` to do four things:

1. Print the short usage of the program to the user
2. Print a specific message about the problem
3. Halt execution of the program
4. Return an error code to the operating system

For instance, I can't very easily tell `argparse` that the `--number` should be a positive integer, only that it must be of type `int`. I can, however, inspect the value myself and call `parser.error('message')` if there is a problem. I do all this inside `get_args` so that, by the time I call `args = get_args()` in my `main` function, I know that all the arguments have been validated. I could have also added a similar check for `--adjectives`, but the main point was to highlight that such a thing is possible. As you write your own programs, you'll have to decide how much validation of user input you feel is necessary.

## main

Once I'm in `main` and have my arguments, I can control the randomness of the program by calling `random.seed(args.seed)` because:

1. The default value of the `seed` is `None`, and setting `random.seed` to `None` is the same as not setting it at all.
2. The `type` of `args.seed` is `int` which is the proper type for `random.seed`. I do not have to validate the argument further. Negative integers are valid values.

To generate some `--number` of insults, I use the `range` function. Because I don't need the number of the insult, I can use the underscore (`_`) as a throwaway value:

````
>>> num_insults = 2
>>> for _ in range(num_insults):
...     print('An insult!')
...
An insult!
An insult!
````

The underscore is a way to unpack a value and indicate that you do not intend to use it. That is, it's not possible to write this:

````
>>> for in range(num_insults):
  File "<stdin>", line 1
    for in range(num_insults):
````

You have to put *something* after the `for` that looks like a variable. If you put a named variable like `n` and then don't use it in the loop, some tools like `pylint` will detect this as a possible error (and well it could be). The `_` shows that you won't use it, which is good information for your future self, some other user, or external tools to know.

You can use multiple `_`, e.g., here I can unpack a 3-tuple so as to get the middle value:

````
>>> x = 'Jesus', 'Mary', 'Joseph'
>>> _, name, _ = x
>>> name
'Mary'
````

To create my list of adjectives, I used the `str.split` method on a long, multi-line string I created using three quotes:

````
>>> adjectives = """
... bankrupt base caterwauling corrupt cullionly detestable dishonest
... false filthsome filthy foolish foul gross heedless indistinguishable
... infected insatiate irksome lascivious lecherous loathsome lubbery old
... peevish rascaly rotten ruinous scurilous scurvy slanderous
... sodden-witted thin-faced toad-spotted unmannered vile wall-eyed
... """.strip().split()
>>> nouns = """
... Judas Satan ape ass barbermonger beggar block boy braggart butt
... carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
... gull harpy jack jolthead knave liar lunatic maw milksop minion
... ratcatcher recreant rogue scold slave swine traitor varlet villain worm
... """.strip().split()
>>> len(adjectives)
36
>>> len(nouns)
39
````

To select some number of adjectives, I chose to use `random.sample` function since I needed more than one:

````
>>> import random
>>> random.sample(adjectives, k=3)
['filthsome', 'cullionly', 'insatiate']
````

For just one randomly selected value, I use `random.choice`:

````
>>> random.choice(nouns)
'boy'
````

To concatenante them together, I need to put `', '` (a comma and a space) between each of the adjectives, and I can use `str.join` for that:

````
>>> adjs = random.sample(adjectives, k=3)
>>> adjs
['thin-faced', 'scurvy', 'sodden-witted']
>>> ', '.join(adjs)
'thin-faced, scurvy, sodden-witted'
````

And feed all this to a format string:

````
>>> noun = random.choice(nouns)
>>> print('You {} {}!'.format(', '.join(adjs), noun))
You thin-faced, scurvy, sodden-witted liar!
````

And now you have a handy way to make enemies and influence people.
