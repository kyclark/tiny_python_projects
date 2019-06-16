# First Bank of Change

Write a Python program that will figure out all the different combinations of pennies, nickels, dimes, and quarters in a given `value` provided as a single positional argument. The value must be greater than 0 and less than or equal to 100.

````
$ ./combos.py
usage: combos.py [-h] int
combos.py: error: the following arguments are required: int
$ ./combos.py -h
usage: combos.py [-h] int

Coin combos for value

positional arguments:
  int         Sum

optional arguments:
  -h, --help  show this help message and exit
$ ./combos.py 1
If you give me 1 cent, I can give you:
  1: 1 penny
$ ./combos.py 4
If you give me 4 cents, I can give you:
  1: 4 pennies
$ ./combos.py 6
If you give me 6 cents, I can give you:
  1: 6 pennies
  2: 1 nickel, 1 penny
$ ./combos.py 13
If you give me 13 cents, I can give you:
  1: 13 pennies
  2: 1 dime, 3 pennies
  3: 1 nickel, 8 pennies
  4: 2 nickels, 3 pennies
$ ./combos.py 27
If you give me 27 cents, I can give you:
  1: 27 pennies
  2: 1 quarter, 2 pennies
  3: 1 dime, 17 pennies
  4: 2 dimes, 7 pennies
  5: 1 nickel, 22 pennies
  6: 1 dime, 1 nickel, 12 pennies
  7: 2 dimes, 1 nickel, 2 pennies
  8: 2 nickels, 17 pennies
  9: 1 dime, 2 nickels, 7 pennies
 10: 3 nickels, 12 pennies
 11: 1 dime, 3 nickels, 2 pennies
 12: 4 nickels, 7 pennies
 13: 5 nickels, 2 pennies
````
