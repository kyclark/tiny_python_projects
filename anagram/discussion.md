I rely on `type=argparse.FileType('r')` for any "file" argument, so my `get_args` once again uses that to define the input `--wordlist`. Likewise, I defined `--num_combos` as an `int` and let `argparse` handle argument validation for me. 

## Logging

My solution also incorporates the `logging` I used while solving this problem for myself. I tend copy and paste this block all the time:

````
logging.basicConfig(
    filename='.log',
    filemode='w',
    level=logging.DEBUG if args.debug else logging.CRITICAL)
````

If I define `args.debug` as a Boolean, then I can effectively turn `logging` on and off because I tend not to write `CRITICAL` messages. Since I use `filemode='w'` to overwrite the `.log` file, then that file will be empty after every run that `--debug` isn't on (and the default is that it is not). Also, I like to use a filename starting with a `.` (e.g., `.log`) as it will be hidden in most Unix-style `ls` commands. This makes logging as transparent and easy as I can think.

## Reading wordlist

First I handle getting a wordlist. I wrote a rather verbose way to process what could be a large input file. Rather than called `args.wordlist.read().split()` which reads the *entire file into memory*, I chose to read each line one-by-one into memory and call `line.split()` on that. If you have to deal with large input file (e.g., I regularly deal with files in the gigabytes in biology!), it's best to read line-by-line. 

I iterate `for` each `word` in the line and clean it up with a regular expression that defines a character class of all the characters `a-z` and `0-9` with `[a-z0-9]` and then uses a caret **inside** the character class to negate it. Then I use the `sub` (substitute) function to replace characters that match with the empty string:

````
>>> import re
>>> regex = re.compile('[^a-z0-9]')
>>> regex.sub('', '"hey!"')
'hey'
````

If the remaining word is only 1 character long, I only accept it if it is "a" or "i".

To store the words, I decided to use a dictionary where the key is the length of a given word and the value is a `set` of the words of that length. I chose a `set` in case I was reading a file other than a standard dictionary-type file where words might be repeated. I use the length of the each word as the key so that I can select the combinations of words whose lengths sum to the desired lenghts. That is, if my input word is 5 characters long, there is no reason to look at words longer than 5 characters.

## defaultdict

To define this data structure, I used `words = defaultdict(set)` where `defaultdict` takes a datatype like `str` or `list` as the default *value* to initiate when a given key does not exist. For instance, using `int` will create a new entry in the dictionary with a value of `0`:

````
>>> from collections import defaultdict
>>> d = defaultdict(int)
>>> d
defaultdict(<class 'int'>, {})
>>> d['foo'] += 1
>>> d
defaultdict(<class 'int'>, {'foo': 1}) 
````

If you use `str`, the empty string will be used:

````
>>> d = defaultdict(str)
>>> d
defaultdict(<class 'str'>, {})
>>> d['foo'] += 'a'
>>> d
defaultdict(<class 'str'>, {'foo': 'a'})
>>> d['foo'] += 'b'
>>> d
defaultdict(<class 'str'>, {'foo': 'ab'})
````

Likewise with a `list`, you get an empty list:

````
>>> d = defaultdict(list)
>>> d
defaultdict(<class 'list'>, {})
>>> d['foo'] += 'a'
>>> d['foo'] += 'b'
>>> d
defaultdict(<class 'list'>, {'foo': ['a', 'b']})
````

And so, with `set` you get an empty set to which you can `add`:

````
>>> d = defaultdict(set)
>>> d
defaultdict(<class 'set'>, {})
>>> d['foo'].add('a')
>>> d['foo'].add('b')
````

Note that the argument to `defaultdict` is *not* in quotes. You are passing the class `set` not the string `'set'`!

So, with all that, I end up adding words like so:

````
>>> words = defaultdict(set)
>>> word = 'apple'
>>> words[len(word)].add(word)
>>> word = 'bear'
>>> words[len(word)].add(word)
>>> words
defaultdict(<class 'set'>, {5: {'apple'}, 4: {'bear'}})
````

## Identifying anagrams

In the intro to the problem, I mentioned my algorithm for finding an anagram:

1. Same length as the given word
2. Same frequency of characters as the given word

The first one is easy enough to find using `len`. If our given word is "listen," then we only need to look at words of length 6 or less:

````
>>> given = 'listen'
>>> len(given)
6
````

How about the character frequency? There are many ways to find this, but I know of no easier method than to use the `Counter` from the `collections` module:

````
>>> from collections import Counter
>>> Counter('listen')
Counter({'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1})
````

If we are looking at the word "tinsel," we see that we have found an anagram:

````
>>> word = 'tinsel'
>>> len(given) == len(word)
True
>>> Counter(given) == Counter(word)
True
````

## Selecting words to compare

My first implementation of this program was quite naive and yet worked fine for find all other single words that were anagrams. Everything came crashing down when I attempted to find combinations. I suddenly realized the number of 2-word combinations I needed to check (that 55 *billion* I mentioned before). As it happened, I then rewatched "The Imitation Game" about Alan Turing and the creation of his machine ("Christopher") to crack the Enigma code which has a possible 150 million million possible states. He was unable to build a machine that could churn through that many possibilities in the 18 hours or so per day they had to find the right combination, so they had to find a way to cut down the number of combinations they attempted. Similarly, I realized I only needed to look at combinations of words whose lengths sum to the length of the given word; hency my decision to store `words` using the word length as the key and then as a `set` of words that length. 

Next I needed to find all combinations of numbers that add up to that number. Let's consider we are using "listen" as the `text`:

````
>>> text = 'listen'
>>> text_len = len(text)
>>> text_len
6
````

I need to do quite a few complex operations for which the `itertools` module provides very handy functions:

````
>>> from itertools import combinations, permutations, product, chain
````

First assume that we had words ranging from 1 to 10 characters in our word list file:

````
>>> lengths = list(range(1, 11))
>>> lengths
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
````

Now find all `combinations` of all the different lengths, I first need to `chain` the `lengths` to add it to itself:

````
>>> list(chain(lengths, lengths))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
````

And then find the combinations of which there are many:

````
>>> len(list(combinations(chain(lengths, lengths), 2)))
190
>>> list(combinations(chain(lengths, lengths), 2))[:5]
[(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)]
````

It turns out the list is longer than necessary because the tuples are unique, so we can fix that with a `set`:

````
>>> combos = combinations(chain(lengths, lengths), 2)
>>> uniq_combos = set(map(lambda t: tuple(sorted(t)), combos))
>>> len(uniq_combos)
55
>>> list(uniq_combos)[:3]
[(5, 9), (4, 7), (1, 3)]
````

And then find those where the sum is `6`:

````
>>> list(filter(lambda t: sum(t) == 6, uniq_combos))
[(3, 3), (1, 5), (2, 4)]
````

If we put it all together and look for combinations of 3 numbers that sum to 6:

````
>>> n = 3
>>> text_len = 6
>>> key_combos = list(
...     filter(
...         lambda t: sum(t) == text_len,
...         set(
...             map(lambda t: tuple(sorted(t)),
...                 combinations(chain(lengths, lengths), n)))))
>>>
>>> key_combos
[(1, 1, 4), (1, 2, 3)]
````

Now I have the *keys* for the `words` to look to check for word combinations! 

````
>>> key_combos
[(3, 3), (1, 5), (2, 4)]
````

Let's take the first combo:

````
>>> keys = key_combos[0]
>>> keys
(1, 3)
````

And pretend we have a very small `words` list:

````
>>> words = defaultdict(set)
>>> words[3].add('les')
>>> words[3].add('tin')
>>> words[4].add('lest')
>>> words[4].add('list')
>>> words[3].add('len')
>>> words[3].add('its')
>>> words
defaultdict(<class 'set'>, {3: {'len', 'its', 'tin', 'les'}, 4: {'list', 'lest'}})
````

I can `map` to find to find all the words for those lengths.

````
>>> list(map(lambda k: words[k], keys))
[{'len', 'its', 'tin', 'les'}, {'len', 'its', 'tin', 'les'}]
````

And then use `product` to get the Cartesian combination:

````
>>> word_combos = list(product(*list(map(lambda k: words[k], keys))))
>>> word_combos[:3]
[('len', 'len'), ('len', 'its'), ('len', 'tin')]
````

Which I can then iterate and apply my algorithm described above to decide if there are any anagrams:

````
>>> counts = Counter('listen')
>>> for t in word_combos:
...     if Counter(''.join(t)) == counts:
...         for s in [' '.join(l) for l in permutations(t)]:
...             if s != text:
...                 print(s)
...
len its
its len
its len
len its
tin les
les tin
les tin
tin les
````

Some are repeated which is why I chose to create my `anagrams` holder as a `set` to make them unique.

In the end, I look to see how many `anagrams` I found using `len(anagrams)`. If there are some, I report how many and what they are in `sorted` order; otherwise I let the user know that none were found.