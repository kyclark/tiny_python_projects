# Article Selector

Write a Python program called `article.py` that will select `a` or `an` for a given word depending on whether the word starts with a consonant or vowel, respectively.

When run with no arguments or the `-h|--help` flags, it should print a usage statement:

````
$ ./article.py
usage: article.py [-h] str
article.py: error: the following arguments are required: str
$ ./article.py -h
usage: article.py [-h] str

Article selector

positional arguments:
  str         Word

optional arguments:
  -h, --help  show this help message and exit
````

When run with a single positional argument, it should print the correct article and the given argument. 

````
$ ./article.py bear
a bear
$ ./article.py Octopus
an Octopus
````

The tests will only give you words that start with an actual alphabetic character, so you won't have to detect numbers or punctuation or other weird stuff. Still, how might you extend the program to ensure that given argument only starts with one of the 26 characters of the English alphabest?

Hints:

* Start your program with `new.py` and fill in the `get_args` with a single position argument called `word`.
* You can get the first character of the word by indexing it like a list, `word[0]`.
* Unless you want to check both upper- and lowercase letters, you can use either the `str.lower` or `str.upper` method to force the input to one case for checking if the first character is a vowel or consonant.
* There are fewer vowels (five, if you recall), so it's probably easier to check if the first character is one of those.
* You can use the `x in y` syntax to see if the element `x` is `in` the collection `y` where "collection" here is a `list`.
* For the purposes of `x in y`, a string (`str`) is a `list` of characters, so you could ask if a character is in a string.
* Use the `print` function to print out the article joined to the argument. Put a single space in between.
* Run `make test` (or `pytest -xv test.py`) *after every change to your program*to ensure your program compiles and is on the right track. 
