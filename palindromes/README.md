# Palindromes

Write a Python program called `palindromic.py` that will find words that are palindromes in positional argument which is either a string or a file name.

````
$ ./palindromic.py
usage: palindromic.py [-h] [-m int] str
palindromic.py: error: the following arguments are required: str
$ ./palindromic.py -h
usage: palindromic.py [-h] [-m int] str

Find palindromes in text

positional arguments:
  str                Input text or file

optional arguments:
  -h, --help         show this help message and exit
  -m int, --min int  Minimum word length (default: 3)
$ ./palindromic.py '"Wow!" said Mom.'
wow
mom
$ ./palindromic.py input.txt
anna
civic
kayak
madam
mom
wow
level
noon
racecar
radar
redder
refer
rotator
rotor
solos
stats
tenet
````
