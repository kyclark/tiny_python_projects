# Scrambler

Write a Python program called `scrambler.py` that will take a single position positional argument that is text or a text file and then convert each word into a scrambled version. The scrambling should only work on words greater than 3 characters in length and should only scramble the letters in the middle, leaving the first and last characters unchanged. The program should take a `-s|--seed` argument (default `None`) to pass to `random.seed`.

Cf. Typoglycemia https://www.dictionary.com/e/typoglycemia/

We'll need to use the same algorithm for scrambling the words. I used the `random.shuffle` method to mix up the letters in the middle, being sure that the word that gets created is not the same as the word that you are given. If the word is 3 characters or shorter, just return the word unchanged.

Another very tricky bit is that we want to scramble all the "words" on each line and leave everything that's not a "word" unchanged. We'll use a regular expression that looks for strings composed only of the characters a-z, A-Z, and the single quote so we can find words like `can't` or `Susie's`. Everything else will be consider not a word. Here is the regex you should use:

````
>>> import re
>>> text = 'this is  a\n"sentence?"'
>>> re.split(r'(\W+)', text)
['this', ' ', 'is', '  ', 'a', '\n"', 'sentence', '?"', '']
````

Now scramble all the things that are "words"!

Here is how the program should perform:

````
$ ./scrambler.py
usage: scrambler.py [-h] [-s int] STR
scrambler.py: error: the following arguments are required: STR
$ ./scrambler.py -h
usage: scrambler.py [-h] [-s int] STR

Scramble the letters of words

positional arguments:
  STR                 Input text or file

optional arguments:
  -h, --help          show this help message and exit
  -s int, --seed int  Random seed (default: None)
````  
  
It should handle text on the command line:

````
$ ./scrambler.py -s 1 foobar
faobor
$ ./scrambler.py -s 1 "foobar bazquux"
faobor buuzaqx
````

Or from a file:

````
$ ./scrambler.py -s 1 ../inputs/the-bustle.txt
The blutse in a hsoue
The monrnig atefr dteah
Is snleoemst of iusinedrts
Eatcend uopn etarh,--

The sewnpeig up the hreat,
And ptunitg lvoe aawy
We slahl not wnat to use agian
Utnil ertiteny.
````
