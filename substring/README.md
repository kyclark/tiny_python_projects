# Substring Guessing Game

Write a Python program called `sub.py` that plays a guessing game where you read a `-f|--file` input (default `/usr/share/dict/words`) and use a given `-k|--ksize` to find all the words grouped by their shared kmers. Remove any kmers where the number of words is fewer than `-m|--min_words`. Also accept a `-s|--seed` for `random.seed` for testing purposes. Prompt the user to guess a word for a randomly chosen kmer. If their guess is not present in the shared list, taunt them mercilessly. If their guess is present, affirm their worth and prompt to guess again. Allow them to use `!` to quit and `?` to be provided a hint (a word from the list). For both successful guesses and hints, remove the word from the shared list. When they have quit or exhausted the list, quit play. At the end of the game, report the number of found words.

````
$ ./sub.py -h
usage: sub.py [-h] [-f str] [-s int] [-m int] [-k int]

Find words sharing a substring

optional arguments:
  -h, --help            show this help message and exit
  -f str, --file str    Input file (default: /usr/share/dict/words)
  -s int, --seed int    Random seed (default: None)
  -m int, --min_words int
                        Minimum number of words for a given kmer (default: 3)
  -k int, --ksize int   Size of k (default: 4)
$ ./sub.py
Name a word that contains "slak" [!=quit, ?=hint] (10 left) slake
Totes! "slake" is found!
Name a word that contains "slak" [!=quit, ?=hint] (9 left) ?
For instance, "breislakite"...
Name a word that contains "slak" [!=quit, ?=hint] (8 left) unslakable
Totes! "unslakable" is found!
Name a word that contains "slak" [!=quit, ?=hint] (7 left) q
What is wrong with you?
Name a word that contains "slak" [!=quit, ?=hint] (7 left) !
Quitter!
Hey, you found 2 words! Not bad.
````
