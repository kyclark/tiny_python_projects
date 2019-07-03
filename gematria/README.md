# Gematria: Numeric encoding of text

Write a Python program called `gematria.py` that will numerically encode each word in a given text. The name of this program comes from gematria, a system for assigning a number to a word by summing the numeric values of each of the letters as defined by the Mispar godol (https://en.wikipedia.org/wiki/Gematria). For English characters, we can use the ASCII table (https://en.wikipedia.org/wiki/ASCII). Python provides these value throug the `ord` function to convert a character to its "ordinal" (order in the ASCII table) value as well as the `chr` function to convert a number to its "character."

````
>>> ord('A')
65
>>> ord('a')
97
>>> chr(88)
'X'
>>> chr(112)
'p'
````

To implement an ASCII version of gematria in Python, for each word in a text we need to turn each letter into a number and add them all together.  So, to start, note that Python can use a `for` loop to cycle through all the characters in a string:

````
>>> for char in 'python':
...     print(ord(char))
...
112
121
116
104
111
110
````

We've seen before how you can put a `for` loop inside brackets `[]` for a list comprehension. Do that and then `sum` the list.

The program should print a usage if given no arguments or the `-h|--help` flag:

````
$ ./gematria.py
usage: gematria.py [-h] str
gematria.py: error: the following arguments are required: str
$ ./gematria.py -h
usage: gematria.py [-h] str

Gematria

positional arguments:
  str         Input text or file

optional arguments:
  -h, --help  show this help message and exit
````

The text may be given on the command line:

````
$ ./gematria.py 'foo bar baz'
324 309 317
````

Or in a file:

````
$ ./gematria.py ../inputs/fox.txt
289 541 552 333 559 444 321 448 314
````

Hints:

* You'll want to read the input line-by-line because the tests are expecting lines of output where each word has been encoded.
* Can you write a function that can encode just one word? E.g, "gematria" = 842.
* Be sure you only encode the words themselves and not any punctuation that might be next to a word. E.g., if you use `str.split` to break text on whitespaces, quotes/commas/periods and such will still be attached to the words. Additionally, you should remove any internal punctuation like apostrophes. Maybe look into the `re` module to use regular expressions.
* Now can you apply that function to each word in a line of text?