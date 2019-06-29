# Telephone

Perhaps you remember the game of "Telephone" where a message is secretly passed through a series of intermediaries and then the result at the end of the chain is compared with how it started? This is like that, only we're going to take some`text` (from the command line or a file) and mutate it by some percentage `-m|--mutations` (a number between 0 and 1, default `0.1` or 10%) and then print out the resulting text.

Each mutation to the text should be chosen using the `random` module, so your program will also need to accept a `-s|--seed` option (default `None`) to pass to the `random.seed` function for testing purposes. Print the resulting text after making the appropriate number of mutations.

````
$ ./telephone.py
usage: telephone.py [-h] [-s str] [-m float] str
telephone.py: error: the following arguments are required: str
$ ./telephone.py -h
usage: telephone.py [-h] [-s str] [-m float] str

Telephone

positional arguments:
  str                   Input text or file

optional arguments:
  -h, --help            show this help message and exit
  -s str, --seed str    Random seed (default: None)
  -m float, --mutations float
                        Percent mutations (default: 0.1)
````				

The program should not accept a bad `--mutations` argument:

````
$ ./telephone.py -m 10 foo
usage: telephone.py [-h] [-s str] [-m float] str
telephone.py: error: --mutations "10.0" must be b/w 0 and 1
````		

It can be interesting to watch the accumulation of mutations:

````
$ ./telephone.py -s 1 ../inputs/fox.txt
Tho quick brown foa jumps oWer*the lazy dog.
$ ./telephone.py -s 1 -m .5 ../inputs/fox.txt
Thakqkrck&brow- fo[ jumps#oWe,*L/C lxdy dogos
````

## Mutations in DNA

For what it's worth, this is how DNA changes over time. The machinery to copy DNA makes mistakes, and mutations randomly occur. Many times the change is in a part of the DNA that doesn't affect the organism or is a "synonymous" change that doesn't end up affecting the function of the DNA. Our example will only change characters to other characters, what are called "point mutations" or "single nucleotide variations" (SNV) or "single nucleotide polymorphisms" (SNP) in biology. We could write a version that would also randomly delete or insert new characters which are called them "in-dels" (insertion-deletions) in biology.

Mutations (that don't result in the demise of the organism) occur at a fairly standard rate, so counting the number of mutations between a conserved region of any two organisms can allow an estimate of how long ago they diverged from a common ancestor!

We can revisit the output of this program later by using the Hamming distance to find how many changes we'd need to make to the output to regain the input.

## Hints

To create a combined error/usage statement for the `--mutations` error, look at `parser.error` in `argparse`.

To select a character position to change, I suggest using `random.choice` and a `range` from length of the incoming text. With that, you'll need to alter the character at that position, but you'll find that strings in Python are *immutable*. For instance, if I wanted to change "candle" into "handle":

````
>>> s = 'candle'
>>> s[0] = 'h'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
````

So, I need to create a *new string* that has `h` joined to the rest of the string `s` after the zeroth position. How could you do that?

For the replacement value, you should use `random.choice` from the union of the `string` class's `ascii_letters` and `punctuation`:

````
>>> import string
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
````