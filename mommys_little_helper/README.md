# Mommy's Little (Crossword) Helper

Write a Python program called `helper.py` that finds all words matching a given `-p|--pattern` such as one might use to complete a crossword puzzle to find words matching from a given `-w|--wordlist` (default `/usr/share/dict/words`). E.g., all 5-letter words with a "t" as the second character and ending in "ed". I could do this on the command line like so:

````
$ grep '^.t' /usr/share/dict/words | grep 'ed$' | awk 'length($0) == 5'
steed
````

Here is how a program could look:

````
$ ./helper.py
usage: helper.py [-h] [-w str] str
helper.py: error: the following arguments are required: str
$ ./helper.py -h
usage: helper.py [-h] [-w str] str

Crossword helper

positional arguments:
  str                   The pattern to search

optional arguments:
  -h, --help            show this help message and exit
  -w str, --wordlist str
                        Wordlist to search (default: /usr/share/dict/words)
````

We'll use an underscore (`_`) to indicate a blank and supply any known letters, e.g., the example above would be `_t_ed`:

````
$ ./helper.py _t_ed
  1: steed
````

Or 6-letter words beginning with "ex" and ending in "s":

````
$ ./helper.py ex___s
  1: excess
  2: excuss
  3: exitus
  4: exodos
  5: exodus
  6: exomis
````
