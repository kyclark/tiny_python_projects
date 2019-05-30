# Gematria

Write a Python program called `gematria.py` 

Gematria is a system for assigning a number to a word by summing the numeric values of each of the letters as defined by the Mispar godol (https://en.wikipedia.org/wiki/Gematria). For English characters, we can use the ASCII table (https://en.wikipedia.org/wiki/ASCII). It is not necessary, however, to encode this table in our program as Python provides the `ord` function to convert a character to its "ordinal" (order in the ASCII table) value as well as the `chr` function to convert a number to its "character."


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

To implement an ASCII version of gematria in Python, we need to turn each letter into a number and add them all together.  So, to start, note that Python can use a `for` loop to cycle through all the members of a list (in order):


````
>>> for char in ['p', 'y', 't', 'h', 'o', 'n']:
...     print(ord(char))
...
112
121
116
104
111
110
````

Now you just need to `sum` those up for each word!

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
$ ./gematria.py 'foo bar baz'
324 309 317
$ ./gematria.py ../inputs/fox.txt
289 541 552 333 559 444 321 448 314
````
