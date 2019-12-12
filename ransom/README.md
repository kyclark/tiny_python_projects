# Ransom

![A ransom note.](images/ransom.png)

Create a Python program called `ransom.py` that will randomly capitalize the letters in a text. The program should take a `-s|--seed` argument for the `random.seed` to control randomness for the test suite. It should print usage when given no arguments or `-h|--help`.

````
$ ./ransom.py
usage: ransom.py [-h] [-s int] str
ransom.py: error: the following arguments are required: str
$ ./ransom.py -h
usage: ransom.py [-h] [-s int] str

Ransom Note

positional arguments:
  str                 Input text or file

optional arguments:
  -h, --help          show this help message and exit
  -s int, --seed int  Random seed (default: None)
````

The text can be given on the command line:

````
$ ./ransom.py -s 2 'The quick brown fox jumps over the lazy dog.'
the qUIck BROWN fOX JUmps ovEr ThE LAZY DOg.
````

Or in a file:

````
$ cat ../inputs/fox.txt
The quick brown fox jumps over the lazy dog.
$ ./ransom.py --seed 2 ../inputs/fox.txt
the qUIck BROWN fOX JUmps ovEr ThE LAZY DOg.
````

Hints:

* You can iterate each character in the input string with a `for` loop
* For each character, can use the `random.choice` function to decide whether to force the character to upper or lower case using methods from the `str` class
