# Anagram

Write a program called `presto.py` that will find anagrams of a given positional argument. The program should take an optional `-w|--wordlist` (default `/usr/share/dict/words`) and produce output that includes combinations of `-n|num_combos` words (default `1`) that are anagrams of the given input.

It should provide a usage with no input or the `-h|--help` flags:

````
$ ./presto.py
usage: presto.py [-h] [-w str] [-n int] [-d] str
presto.py: error: the following arguments are required: str
$ ./presto.py -h
usage: presto.py [-h] [-w str] [-n int] [-d] str

Find anagrams

positional arguments:
  str                   Input text

optional arguments:
  -h, --help            show this help message and exit
  -w str, --wordlist str
                        Wordlist (default: /usr/share/dict/words)
  -n int, --num_combos int
                        Number of words combination to test (default: 1)
  -d, --debug           Debug (default: False)
````

Be default, it should search the `--wordlist` file for other words of the same length as the input that have the same letters in the same frequency:

````
$ ./presto.py presto
presto =
   1. poster
   2. repost
   3. respot
   4. stoper
$ ./presto.py listen
listen =
   1. enlist
   2. silent
   3. tinsel
````   
   
If `-n` is greater than 1 (the default), then the program should additionally find all combinations of two words that together create the original word. 
   
````   
$ ./presto.py listen -n 2 | tail
  82. sten li
  83. te nils
  84. ten lis
  85. ten sil
  86. ti lens
  87. til ens
  88. til sen
  89. tin els
  90. tin les
  91. tinsel
````

Hints:

* How will you determine that two strings are anagrams? That is, what is the code you will use to compare two strings and return `True` or `False` that they are anagrams? Start there.
* You can assume a strict dictionary-type input file like the default, but you might also consider mining some other text as the source for anagrams, one that might have punctuation and mixed-case letters.
* When you move to `-n > 1`, you may find you quickly have an overwhelming number of combinations to consider. My `/usr/share/dict/words` has 235886 words. At `n=2`, that could produce over 55 *billion* combinations of words. Obviously I don't need to consider the entire Cartesian product of the list, only those whose lengths sum to equal the length of the input word. How can you find all the combinations of numbers that sum to that length? E.g, for 5, you can add 0 + 5, 1 + 4, and 2 + 3. How can you segregate all the input words by their lengths?