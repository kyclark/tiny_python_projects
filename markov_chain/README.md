# Markov Chain

_The Practice of Programming_ by Brian Kernighan and Rob Pike describes the Markov Chain algorithm and how it can be implemented in C, C++, Java, awk, and Perl. You should write a Python program called `markov.py` that takes one or more text files as positional arguments for training

````
$ ./markov.py
usage: markov.py [-h] [-l int] [-n int] [-s int] FILE [FILE ...]
$ ./markov.py -h
usage: markov.py [-h] [-l int] [-n int] [-s int] FILE [FILE ...]

Markov Chain

positional arguments:
  FILE                  Training file(s)

optional arguments:
  -h, --help            show this help message and exit
  -l int, --length int  Output length (characters) (default: 50)
  -n int, --num_words int
                        Number of words (default: 2)
  -s int, --seed int    Random seed (default: None)
$ ./markov.py ../inputs/const.txt
President. But if there should remain two or more States, or any
place subject to the other House, by which it shall have been chosen
before the time fixed for the beginning of his office, the Vice
President, to be prescribed by law. Amendment 8 Excessive bail shall
not prevent any person of life, liberty, or property, without due
process of law; nor deny to any of the States by the United States
shall be necessary to the whole number of male citizens twenty-one
years of a Member or Members from two-thirds of the government of
the States, are reserved to the Constitution of the United States,
shall be drawn from the date of the Adoption of this Constitution,
or, on the Application of the Senate, the executive departments or
of the laws thereof, is denied to any other Place.
````
