# Word Search

Write a Python program called `word_search.py` that takes a file name as the single positional argument and finds the words hidden in the puzzle grid. 

````
$ ./word_search.py
usage: word_search.py [-h] FILE
word_search.py: error: the following arguments are required: FILE
$ ./word_search.py -h
usage: word_search.py [-h] FILE

Argparse Python script

positional arguments:
  FILE        The puzzle

optional arguments:
  -h, --help  show this help message and exit
````

The format of the puzzle file will be a grid of letters followed by an empty line followed by a list of words to find delimited by newlines, e.g.:

````
$ cat puzzle1.txt
RAPPLE
AOAMAE
EEARAB
TOLLAB

APPLE
TEAR
BALLOT
EAR
EBB
````

The program should search for each word and note if they are found. At the end, either report `Found all!` if all words were found or `Failed to find N: ` followed by a comma-separated list of words not found.

````
$ ./word_search.py puzzle1.txt
Found "APPLE"
Found "TEAR"
Found "BALLOT"
Found "EAR"
Found "EBB"
Found all!
$ ./word_search.py puzzle2.txt
Found "APPLE"
Found "TEAR"
Found "BALLOT"
Found "EAR"
Found "EBB"
Failed to find 2: ROLL, LEAP
````
