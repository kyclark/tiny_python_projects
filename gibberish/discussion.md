As recommended in the description, I define my arguments in `get_args` to rely on `argparse` to validate as much as possible, e.g. verify that I get `int` values and readable files as well as provide reasonable defaults for everything but the required `file` argument. I additionally define a `-d|--debug` flag that is only `True` when present so that I can add this bit of code:

````
logging.basicConfig(
    filename='.log',
    filemode='w',
    level=logging.DEBUG if args.debug else logging.CRITICAL)
````

This is a simple and effective way to turn debugging messages on and off. I usually write to a `.log` file, being sure to choose a name that starts with a `.` so that it will normally be hidden when I `ls` the directory. Since the `filemode='w'`, the file will be overwritten on each run. I set the threshold to `logging.DEBUG` if the `debug` flag is `True`; otherwise the `logging` module will only emit those at the `CRITICAL` level. As I don't have any "critical" messages, the `.log` file will be empty unless the `--debug` is present. Then I have `logging.debug()` calls throughout my code which will only log messages when I ask. This is easier than putting `print` statements in your code which you have to remove or comment out when you are done debugging.

## Finding kmers in text

If you followed my advice about breaking down the problem, then you probably created a `kmers` function with the formula for the number of kmers in a given test (`n = l - k + 1`):

````
>>> def get_kmers(text, k=1):
...     return [text[i:i + k] for i in range(len(text) - k + 1)]
...
````

Using the formula given in the intro for the number of kmers in a string, I use the `range` function to get the start position of each of those kmers and then get the slice of the `text` from that position to the position `k` away.

I can verify it works in the REPL:

````
>>> get_kmers('abcd', 2)
['ab', 'bc', 'cd']
>>> get_kmers('abcd', 3)
['abc', 'bcd']
````

But more importantly, I can write a `test_kmers` function that I embed in my code and run with `pytest`!

## Reading the training files

Since I used the `argparse.FileType` to define the `file` with `nargs='+'`, I have a `list` of *open file handles* that can be read. I defined a `read_training` function that iterates over all the words in each file by calling `fh.read().split()`. As this breaks the text on spaces, various bits of punctuation may still be attached:

````
>>> fh = open('../inputs/spiders.txt')
>>> fh.read().split()
['Don’t', 'worry,', 'spiders,', 'I', 'keep', 'house', 'casually.']
````

So I use a regular expression to remove anything that is *not* in the set of letters "a-z" by defining a negated character class `[^a-z]`. I create a one-line function to `lower` the word and `clean` it:

````
>>> import re
>>> clean = lambda word: re.sub('[^a-z]', '', word.lower())
>>> clean('"Hey!"')
'hey'
````

Now I can get cleaned, lowercase text:

````
>>> fh = open('../inputs/spiders.txt')
>>> list(map(clean, fh.read().split()))
['dont', 'worry', 'spiders', 'i', 'keep', 'house', 'casually']
````

I can now get all the kmers for each word by using my `kmers` function. I put all this into a function called `read_training`. It takes a `list` of open file handles (which I get from `argparse`) and a `k` which defaults to `1`:

````
>>> def read_training(fhs, k=1):
...     chains = defaultdict(list)
...     clean = lambda word: re.sub('[^a-z]', '', word.lower())
...     for fh in fhs:
...         for word in map(clean, fh.read().split()):
...             for kmer in get_kmers(word, k + 1):
...                 chains[kmer[:-1]].append(kmer[-1])
...     return chains
...
````

Note the handling of the kmers. I actually request `k+1`-mers and then slice `kmer[:-1]` to get the actual `k`-mer (everything up to the penultimate letter) and then `append` `kmer[-1]` (the last letter) to the `chains` for that `k`-mer.

I can verify it works:

````
>>> from collections import defaultdict
>>> from pprint import pprint as pp
>>> pp(read_training([open('../inputs/spiders.txt')], k=5))
defaultdict(<class 'list'>,
            {'asual': ['l'],
             'casua': ['l'],
             'pider': ['s'],
             'spide': ['r'],
             'suall': ['y']})
````

But, again, *more importantly is that I can write a test that verifies it works*! If you copy in the `test_read_training` function, you have the assurange that you are creating valid chains.

## Making new words

Once I have the chains from all the input files, I need to use a `for` loop for the `range(args.num_words)`. Each time through the loop, I need to choose a starting kmer for a new word and a length

````
>>> k = 3
>>> max_word = 12
>>> chains = read_training([open('../inputs/spiders.txt')], k)
>>> kmers = list(chains.keys())
>>> num_words = 3
>>> for i in range(num_words):
...     word = random.choice(kmers)
...     length = random.choice(range(k + 2, max_word))
...     print('Length "{}" starting with "{}"'.format(length, word))
...
Length "9" starting with "pid"
Length "7" starting with "cas"
Length "8" starting with "orr"
````

OK, that's our starting point. Given a starting kmer like `'pid'`, we need to create a `while` loop that will continue as long as the `len(word)` is less than the `length` we chose for the word. Each time through the loop, I'll set the current `kmer` to the last `k` letters of the `word`. I use `random.choice` to select from `chains[kmer]` to find the next `char` (character) and append that to the `word`:

````
>>> while len(word) < length:
...     kmer = word[-1 * k:]
...     if not chains[kmer]: break
...     char = random.choice(list(chains[kmer]))
...     word += char
...
>>> print(word)
piders
````

It can happen sometimes that there are no options for a given `kmer`. That is, `chains[kmer]` is an empty list, so I in my code I add a check to `break` out of the `while` loop if this evaluates to `False`.

Finally I `print` out the number of the word and the word itself using a format string to align the numbers and text:

````
>>> print('{:3}: {}'.format(i+1, word))
  3: piders
````

## Machine Learning

If you didn't realize it, you just implemented a basic machine learning algorithm. Your program predicts the next letter after a given sequence based on the frequencies of patterns you "learned" from the training files! The kmers you extracted from the text could become vectors for other machine learning techniques. You could, for instance, train on texts that are labeled by language source (e.g., English, German, French) and then, given a new unlabled text, predict the language by the kmer frequencies.

## What next

Now you can talk the "Markov Chain" problem that moves to the level of words and generates novel texts!
