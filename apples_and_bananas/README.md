# Apples and Bananas

Perhaps you remember the children's song "Apples and Bananas"?

    I like to eat, eat, eat apples and bananas
    I like to eat, eat, eat apples and bananas

    I like to ate, ate, ate ay-ples and ba-nay-nays
    I like to ate, ate, ate ay-ples and ba-nay-nays

    I like to eat, eat, eat ee-ples and bee-nee-nees
    I like to eat, eat, eat ee-ples and bee-nee-nees

![Apple and bananas go together like peas and carrots.](images/apples-and-bananas.png)

Write a Python program called `apples.py` that will turn all the vowels in some given text in a single positional argument into just one `-v|--vowel` (default `a`) like this song. 

Replace all vowels with the given vowel, both lower- and uppercase.

If the program is run with no arguments or the `-h|--help` flags, print a usage statement:

````
$ ./apples.py
usage: apples.py [-h] [-v str] str
apples.py: error: the following arguments are required: str
$ ./apples.py -h
usage: apples.py [-h] [-v str] str

Apples and bananas

positional arguments:
  str                  Input text or file

optional arguments:
  -h, --help           show this help message and exit
  -v str, --vowel str  The only vowel allowed (default: a)
````

The program should complain if the `--vowel` argument is not a single, lowercase vowel:

````
$ ./apples.py -v x foo
usage: apples.py [-h] [-v str] str
apples.py: error: argument -v/--vowel: \
invalid choice: 'x' (choose from 'a', 'e', 'i', 'o', 'u')
````

The program should handle text on the command line:

````
$ ./apples.py foo
faa
$ ./apples.py foo -v i
fii
````

If the given text argument is a file, read the text from the file:

````
$ ./apples.py ../inputs/fox.txt
Tha qaack brawn fax jamps avar tha lazy dag.
$ ./apples.py --vowel u ../inputs/fox.txt
Thu quuck bruwn fux jumps uvur thu luzy dug.
````

Hints:

* See `choices` in the `argparse` documentation for how to constrain the `--vowel` options
