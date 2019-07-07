## Handling arguments

As suggested in the introduction, I check that the `--num` argument is a positive integar and that the given acronym is composed entirely of letters and is at least two characters in length. The second is achieved with a regular expression which returns `None` when it fails to match:

````
>>> import re
>>> acronym = 'A'
>>> type(re.search(r'^[A-Z]{2,}$', acronym.upper()))
<class 'NoneType'>
>>> acronym = '4E9'
>>> type(re.search(r'^[A-Z]{2,}$', acronym.upper()))
<class 'NoneType'>
>>> acronym = 'ABC'
>>> type(re.search(r'^[A-Z]{2,}$', acronym.upper()))
<class 're.Match'>
````

If any errors with the arguments are detected, I use `parser.error` to cause `argparse` to do the following:

1. Print the short usage
2. Print an error message
3. Exit the program with a non-zero exit value to indicate a failure

If you inspect the `test.py`, you can see that the tests for these bad inputs verify that the `rv` (return value) for these calls is not `0`. If you write "pipelines" on the command line where the output of one program is the input for the next, it is important to stop the process when a program exits with an error. Non-zero exit values can be used by tools like `make` to halt a larger execution of programs.

I defined my `--exclude` words with `nargs='+'` to indicate one or more string values, so I set the `default='a an the'.split()` which creates a list more easily than typing each individual word in quotes and `[]`:

````
>>> 'a an the'.split()
['a', 'an', 'the']
````

I can take that list and lowercase each word by mapping the values into the `str.lower` function. Note that `map` is a "lazy" function that only produces values when needed, so I have to use `list` in the REPL if I want to see the evaluated `list`:

````
>>> list(map(str.lower, 'A AN THE'.split()))
['a', 'an', 'the']
````

Then I can use `set` to create a unique list of stop words:

````
>>> exclude = 'a an the'.split()
>>> stop = set(map(str.lower, exclude))
>>> stop
{'the', 'an', 'a'}
````

Because I define the `--seed` to be `type=int` with a `default=None`, I can pass `args.seed` directly to `random.seed`. I also define `--wordlist` using `type=argparse.FileType('r')` to ensure that the value is a readable file, and I set the default to my system dictionary.

## Grouping words by first letters

After validating the arguments, the next big conceptual task is reading the `--wordlist` and grouping the words by their first letters. A dictionary is perfect for this sort of task. Many times we associate some single value like a string to some other single value like another string or a number, e.g., a last name to a first name or a name to an age. Here, though, we want to link a letter like `a` to a `list` of words that start with that letter. 

It's tedious to check for the existence of a key and then create a new `list` if that key doesn't exist, so let's use the `defaultdict` for this. The argument to `defaultdict` is the **type** of data we want to use for the **value** of a new entry. That is, if we start with an empty `dict` called `words` and try to access `words['a']`, it will blow up:

````
>>> words = dict()
>>> words['a']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'a'
````

If instead we create `words` as a `defaultdict` that initializes an undefined key with an empty list, we get this instead:

````
>>> from collections import defaultdict
>>> words = defaultdict(list)
>>> words['a']
[]
````

Which means we can call `list` methods on the values of elements in the `dict`, methods like `append`:

````
>>> words['b'].append('banana')
>>> words
defaultdict(<class 'list'>, {'a': [], 'b': ['banana']})
````

Since we defined the `--wordlist` to be a readable file, `argparse` has already delivered to us an open file handle upon which we can call `read`. I also want to lowercase the line and then `split` it into word-like units. I'm going to create an `io.StringIO` object here that I also use in the test to create a string that will behave like an open filehandle:

````
>>> fh = io.StringIO('apple, "BANANA," The Coconut! Berry - APPLE; A cabbage.')
>>> type(fh)
<class '_io.StringIO'>
````

My goal is to turn this into a data structure where the words are grouped by their first, lowercased letter, something like this:

````
'a' = ['apple']
'b' = ['banana']
'c' = ['cabbage', 'coconut']
````

I can chain the methods `read`, `lower`, and `split` to get word-like units. Note that I can only `read` an `io.StringIO` object once. Just like a file handle, once it is exhausted it has to be opened again:

````
>>> words = fh.read().lower().split()
>>> words
['apple,', '"banana,"', 'the', 'coconut!', 'berry', '-', 'apple;', 'a', 'cabbage.']
````

We're getting closer, but we still need to remove anything that's not a letter from each word. We can create a `clean` function to do this. It's really just one line of code, so I can actually make it like so:

````
>>> clean = lambda word: re.sub('[^a-z]', '', word)
````

And I can `map` all the words into that function to get actual "words":

````
>>> words = list(map(clean, fh.read().lower().split()))
>>> words
['apple', 'banana', 'the', 'coconut', 'berry', '', 'apple', 'a', 'cabbage']
````

We only want to take words that are at least 2 characters long, so we can create a regular expression for this:

````
>>> good = re.compile(r'^[a-z]{2,}$')
````

And we can use it like so:

````
>>> type(good.search('banana'))
<class 're.Match'>
>>> type(good.search('i'))
<class 'NoneType'>
````

I'd actually like to use it as a `filter` for the elements coming out of the `map`, but there's a problem in that we can't use it like it is:

````
>>> words = list(filter(good, map(clean, fh.read().lower().split())))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 're.Pattern' object is not callable
````

It's a bit cryptic to figure this out, but the problem is with the fact that `good` is not a function, it's a compiled regular expression:

````
>>> type(good)
<class 're.Pattern'>
````

What we want is something that is something that uses `re.match` with a regex to filter the elements. The `re.match` function takes two arguments, and the `filter` will automatically feed in the words, so what we need is a *partially applied* function where the first argument (the regex pattern) is already bound. We can use `functools.partial` for this:

````
>>> good = partial(re.search, r'^[a-z]{2,}$')
>>> type(good('banana'))
<class 're.Match'>
>>> type(good('x'))
<class 'NoneType'>
````

And it can now be a part of our chain:

````
>>> words = list(filter(good, map(clean, fh.read().lower().split())))
>>> words
['apple', 'banana', 'the', 'coconut', 'berry', 'apple', 'cabbage']
````

So we're just read the input file, split it into words, removed any bad characters, and filtered out unwanted strings in one line of code that is extremely readable! To avoid adding words more than once, I created a `seen` variable from a `set` to check if a word has been seed before. I was also given a list of `stop` words to avoid which is also a `set` (or it could just as easily be a `list`), so I need to check that any given `word` is not in either of these.

````
>>> stop
{'the', 'an', 'a'}
>>> seen = set()
>>> for word in words:
...     if not any([word in stop, word in seen]):
...         print(word)
...         seen.add(word)
...
apple
banana
coconut
berry
cabbage
````

And you can see that "apple" was only printed once. Returning to the end goal of making a list of words by first letter, we return to our `defaultdict(list)` that we started off with:

````
>>> words_by_letter = defaultdict(list)
>>> for word in words:
...     if not any([word in stop, word in seen]):
...         words_by_letter[word[0]].append(word)
...         seen.add(word)
...
>>> from pprint import pprint as pp
>>> pp(words_by_letter)
defaultdict(<class 'list'>,
            {'a': ['apple'],
             'b': ['banana', 'berry'],
             'c': ['coconut', 'cabbage']})
````

Finally we can make all this a function called `group_words`. Note that I'll make the `stop` words an option by adding a default value:

````
>>> def group_words(file, stop_words=set()):
...     """Groups words in file by first letter"""
...     good = partial(re.search, r'^[a-z]{2,}$')
...     seen = set()
...     words_by_letter = defaultdict(list)
...     clean = lambda word: re.sub('[^a-z]', '', word)
...     for word in filter(good, map(clean, file.read().lower().split())):
...         if word not in seen and word not in stop_words:
...             seen.add(word)
...             words_by_letter[word[0]].append(word)
...     return words_by_letter
...
````

I can call it with an open file handle:

````
>>> pp(group_words(open('../inputs/fox.txt')))
defaultdict(<class 'list'>,
            {'b': ['brown'],
             'd': ['dog'],
             'f': ['fox'],
             'j': ['jumps'],
             'l': ['lazy'],
             'o': ['over'],
             'q': ['quick'],
             't': ['the']})
````

Most importantly, I can write a test which I'll call `test_group_words` (included in the introduction) so that `pytest` will execute it. My test sends in a fake (or "mock" in testing parlance) file handle and checks that the expected words are present and absent. It may seem like overkill to put just a few lines of code into a function, but it's very important to write small functions that do essentially one thing and which can be tested!

## Making definitions

Similarly, I made a small function that takes the grouped words, an acronym, and number and returns a list of that number of plausible definitions. I can use a `for` loop with `range(n)` to iterate `n` times through some code. Since I don't need the number for each loop, I can use an underscore (`_`) to throwaway the value:

````
>>> limit = 2
>>> for _ in range(limit):
...     print('hi')
...
hi
hi
````

So, for however many definitions I want, I need to loop through each letter of the acronym and select some word from the grouped words:

````
>>> pp(words_by_letter)
defaultdict(<class 'list'>,
            {'a': ['apple'],
             'b': ['banana', 'berry'],
             'c': ['coconut', 'cabbage']})
>>> import random
>>> definition = []
>>> acronym = 'ABC'
>>> for letter in acronym:
...     opts = words_by_letter.get(letter.lower(), [])
...     definition.append(random.choice(opts).title() if opts else '?')
...
>>>
>>> definition
['Apple', 'Berry', 'Coconut']
````

Depending on the wordlist I read, a given letter may not exist, so I use the `dict.get` method to safely look for a `letter` with the default return value being an empty list `[]`. Then I can use an `if` *expression* to use `random.choice` to select from those options if they exists or use the question mark `?` to indicate no possible value. I can put all this into a function:

````
>>> def make_definitions(acronym, words_by_letter, limit=1):
...     definitions = []
...     for _ in range(limit):
...         definition = []
...         for letter in acronym.lower():
...             opts = words_by_letter.get(letter.lower(), [])
...             definition.append(random.choice(opts).title() if opts else '?')
...         definitions.append(' '.join(definition))
...     return definitions
...
>>> make_definitions('ABC', words_by_letter)
['Apple Berry Coconut']
>>> make_definitions('ABX', words_by_letter)
['Apple Berry ?']
````

The `test_make_definitions` function included in the introduction ensures that this function works properly.

## Putting it together

To recap, so far we've written three central functions to:

1. Parse and validate the user arguments
2. Read the word list file and group the words by their first letters
3. Make definitions from the grouped words for the given acronym

Now we can write very understandable, almost self-documenting code:

````
>>> words_by_letter = group_words(open('/usr/share/dict/words'), stop)
>>> definitions = make_definitions('YYZ', words_by_letter, 2)
>>> definitions
['Yearock Yon Zone', 'Yacca Yengee Zincalo']
````

If we are able to make some `definitions`, we will print them out; otherwise we can apologize:

````
>>> if definitions:
...     print(acronym.upper() + ' =')
...     for definition in definitions:
...         print(' - ' + definition)
... else:
...     print('Sorry I could not find any good definitions')
...
ABC =
 - Yearock Yon Zone
 - Yacca Yengee Zincalo
````

## Testing

In the introduction, I encouraged you to write a couple of functions that included specific tests that live *inside* your program. Such tests help you know that the building blocks of your code work -- what are often called "unit tests." 

Additionally, you have been provided a test suite that checks that the program works from the *outside*. However you implement the logic of the code, these tests check that the whole program works -- what might be called "integration tests."

As you write your own programs, you should think about writing very small functions that do *one thing* and then writing tests to be sure they actually do the thing you think and always continue to do that thing as you change your program. Additionally, you need to write tests to make sure that all the parts work together to accomplish the larger task at hand. While writing and refactoring this program, I repeatedly updated and used my test suite to ensure I wasn't introducing bugs!