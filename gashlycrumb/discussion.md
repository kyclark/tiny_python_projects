I prefer to have all the logic for parsing and validating the command-line arguments in the `get_args` function. In particular, `argparse` can do a fine job verifying tedious things such as an argument being an existing, readable `--file` which is why I use `type=argparse.FileType('r')` for that argument. If the user doesn't supply a valid argument, then `argparse` will throw an error, printing a helpful message along with the short usage and exiting with an error code. 

By the time I get to the line `args = get_args()`, I know that I have a valid, open file handle in the `args.file` slot. In the REPL, I can manually do what `argparse` has done by using `open` to get a file handle which I like to usually call `fh`:

````
>>> fh = open('gashlycrumb.txt')
````

I can use a `for` loop to read each line of text and get the first letter using `line[0]` and set a `dict` called `lookup` with the value for the `line`:

````
>>> lookup = {}
>>> for line in fh:
...     lookup[line[0]] = line.rstrip()
...
>>> from pprint import pprint as pp
>>> pp(lookup)
{'A': 'A is for Amy who fell down the stairs.',
 'B': 'B is for Basil assaulted by bears.',
 'C': 'C is for Clara who wasted away.',
 'D': 'D is for Desmond thrown out of a sleigh.',
 'E': 'E is for Ernest who choked on a peach.',
 'F': 'F is for Fanny sucked dry by a leech.',
 'G': 'G is for George smothered under a rug.',
 'H': 'H is for Hector done in by a thug.',
 'I': 'I is for Ida who drowned in a lake.',
 'J': 'J is for James who took lye by mistake.',
 'K': 'K is for Kate who was struck with an axe.',
 'L': 'L is for Leo who choked on some tacks.',
 'M': 'M is for Maud who was swept out to sea.',
 'N': 'N is for Neville who died of ennui.',
 'O': 'O is for Olive run through with an awl.',
 'P': 'P is for Prue trampled flat in a brawl.',
 'Q': 'Q is for Quentin who sank on a mire.',
 'R': 'R is for Rhoda consumed by a fire.',
 'S': 'S is for Susan who perished of fits.',
 'T': 'T is for Titus who flew into bits.',
 'U': 'U is for Una who slipped down a drain.',
 'V': 'V is for Victor squashed under a train.',
 'W': 'W is for Winnie embedded in ice.',
 'X': 'X is for Xerxes devoured by mice.',
 'Y': 'Y is for Yorick whose head was bashed in.',
 'Z': 'Z is for Zillah who drank too much gin.'}
````

We've seen list comprehensions by essentially sticking a `for` inside brackets `[]`, and we can use a dictionary comprehension by doing the same with a `for` loop inside curlies `{}`. If you are following along by pasting code into the REPL, note that we have exhausted the file handle `fh` just above by reading it. I need to `open` it again for this next bit:

````
>>> fh = open('gashlycrumb.txt')
>>> lookup = {line[0]: line.rstrip() for line in fh}
````

If you `pprint` it again, you should see the same output as above. It may seem like showing off to write one line of code instead of three, but it really does make a good deal of sense to write compact, idiomatic code. More code always means more chances for bugs, so I usually try to write code that is as simple as possible (but no simpler).

Now that I have a `lookup`, I can ask if some value is `in` the keys. Note that I know the letters are in uppercase and I assume the user could give me lower, so I just use `letter.upper()` to only compare that case:

````
>>> letter = 'a'
>>> letter.upper() in lookup
True
>>> lookup[letter.upper()]
'A is for Amy who fell down the stairs.'
````

If the letter is found, I can print the line of text for that letter; otherwise, I can print the message that I don't know that letter:

````
>>> letter = '4'
>>> if letter.upper() in lookup:
...     print(lookup[letter.upper()])
... else:
...     print('I do not know "{}".'.format(letter))
...
I do not know "4".
````

I don't have to use a `dict`. I could, for example, use a `list` of `tuple` values:

````
>>> fh = open('gashlycrumb.txt')
>>> lookup = [(line[0], line.rstrip()) for line in fh]
>>> pp(lookup[:2])
[('A', 'A is for Amy who fell down the stairs.'),
 ('B', 'B is for Basil assaulted by bears.')]
````

I can get the letters with a list comprehension:

````
>>> [char for char, line in lookup][:3]
['A', 'B', 'C']
````

And then use `in` to see if my `letter` is present:

````
>>> letter = 'a'
>>> letter.upper() in [char for char, line in lookup]
True
````

And get the value like so:

````
>>> [line for char, line in lookup if char == letter.upper()]
['A is for Amy who fell down the stairs.']
````

The problem is that the cost of the search is proportional to the number of values. That is, if we were searching a million keys in a list, then Python starts searching at the beginning of the list and goes until it finds the value. When you store items in a `dict`, the search time for a key can be much shorter, often nearly instantaneous. It's well worth your time to learn dictionaries very well!

## Edward Gorey

If you are not familiar with the work of Edward Gorey, please  go read about him immediately, e.g. https://www.brainpickings.org/2011/01/19/edward-gorey-the-gashlycrumb-tinies/! 

## Alternate text

Write your own version of Gorey's text and pass in your version as the `--file`. I include my own `alternate.txt` which I used the simple and Soundex rhymers to help me find words.

## Interactive version

Write an interactive version that takes input directly from the user.

````
$ ./gashlycrumb_interactive.py
Please provide a letter [! to quit]: t
T is for Titus who flew into bits.
Please provide a letter [! to quit]: 7
I do not know "7".
Please provide a letter [! to quit]: !
Bye
````

Hint: Use `while True` to set up an infinite loop and keep using `input` to get the user's next `letter`.
