# Runny Babbit

Are you familiar with Spoonerisms where the initial consonant sounds of two words are switched? According to Wikipedia, they get their name from William Archibald Spooner who did this often. The author Shel Silverstein wrote a wonderful book called _Runny Babbit_ ("bunny rabbit") based on this. So, let's write a Python program called `runny_babbit.py` that will read some text or an input file given as a single positional argument and finds neighboring words with initial consonant sounds to swap. As we'll need to look at pairs of words and in such as way that it will make it difficult to remember the original formatting of the text, let's also take a `-w|--width` (default `70`) to format the output text to a maximum width.

As usual, the program should show usage with no arguments or for `-h|--help`:

````
$ ./runny_babbit.py
usage: runny_babbit.py [-h] [-w int] str
runny_babbit.py: error: the following arguments are required: str
$ ./runny_babbit.py -h
usage: runny_babbit.py [-h] [-w int] str

Introduce Spoonerisms

positional arguments:
  str                  Input text or file

optional arguments:
  -h, --help           show this help message and exit
  -w int, --width int  Output text width (default: 70)
````

It should handle text from the command line:

````
$ ./runny_babbit.py 'the bunny rabbit'
the runny babbit
````

Or a named file:

````
$ cat input1.txt
The bunny rabbit is cute.
$ ./runny_babbit.py input1.txt
The runny babbit is cute.
````

We'll use a set of "stop" words to prevent the switching of sounds when one of the words is in the following list:

before behind between beyond but by concerning despite down
during following for from into like near plus since that the
through throughout to towards which with within without

Hints: 

* You'll need to consider all the words in the input as pairs, like `[(0, 1), (1, 2)]` up to `n` (number of words) etc. How can you create such a list where instead of `0` and `1` you have the actual words, e.g., `[('The', 'bunny'), ('bunny', 'rabbit')]`?
* There are several exercises where we try to break words into initial consonant sounds and whatever else that follows. Can you reuse code from elsewhere? I'd recommend using regular expressions!
* Be sure you don't use a word more than once in a swap. E.g., in the phrase "the brown, wooden box", we'd skip "the" and consider the other two pairs of words `('brown', 'wooden')` and `('wooden', 'box')`. If we swap the first pair to make `('wown', 'brooden')`, we would not want to consider the next pair because 'wooden' has already been used. 
* Use the `textwrap` module to handle the formatting of the ouput text to a maximum `--width`