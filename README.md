# Playful Python

I believe you can learn serious things through silly games. 

I'd like to make this into a book or something, similar to the Python bioinformatics/data science (https://github.com/kyclark/practical_python_for_data_science) repo. I think you will learn best by *doing*, so I think I will write this as a loose collection of exercises that spell out the skills I aim to teach with each exercise. I will create descriptions for each exercise with examples of how the program should work along with a test suite. You will need to write the program that satisfies the test suite.

I think I'm going to present this differently from other material in that I won't necessarily show you beforehand what you need to write a program. I'll describe what the program should do and provide some discussion about how to write it. I'll also create an appendix with short example of how to do things like read/write from/to a file, process all the files in a directory, extract k-mers from a string, etc. I'll provide some building blocks, but I want you to figure out how to put the pieces together!

# new_py

I provide a program in the `bin` directory called `new_py` that will help you stub out new Python programs using the fabulous `argparse` module to parse the command line arguments and options for your programs. I highly recommend you start every new program with this. For example, if the `README.md` says "Write a Python program called `abc.py` that ...", then you should do this:

````
$ new_py abc
````

This will create a new file called `abc.py` (that has been made executable with `chmod +x`, if your operating system supports that) that has example code for you to start writing your program. It's best to put `new_py` into your `$PATH` or alter your `$PATH` to include the directory where it's located. FWIW, I always create a `$HOME/.local/bin` that I add to my `$PATH` for programs like this.

# How to Use

First use the GitHub interface to "fork" this repository into your own account. Then do `git clone` of *your* repository to get a local copy. Inside that checkout, do:

````
git remote add upstream https://github.com/kyclark/playful_python.git 
````

so that you can do `git pull upstream master` to get updates. When you create new files, `git add/commit/push` them to *your* repository. (Please do not create pull requests on *my* repository -- unless, of course, you have suggestions for improving my repo!).

This is a work in progress. If you see a directory contains a `README.md`, `solution.py`, `Makefile`, and `test.py`, then it's likely ready to be solved.

# Structure

Right now, I'm not sure how I'll structure the exercises. I wouldn't mind if you just randomly chose one and see how it goes. They vary quite a bit in difficulty, so maybe I'll just give them 1, 2, or 3 stars to indicate easy to hard. Here I'll give a brief overview of the exercises:

* abuse (\*\*): generate insults
* anagram (\*\*\*): find anagrams of text
* apples_and_bananas (\*): substitute vowels in text
* bacronym (\*\*): back-fit words onto acronyms
* blackjack (\*\*): play Blackjack (card game)
* bottles_of_beer (\*): produce the "Bottle of Beer on the Wall" song
* family_tree (\*\*): use GraphViz to visualize a family tree from text 
* gashlycrumb (\*): create a morbid lookup table from text
* gematria (\*\*): calculate numeric values of words from characters
* guess (\*): write a number-guessing game
* hangman (\*\*\*): write a Hangman (word/letter-guessing game)
* howler (\*): uppercase input text
* jump_the_five (\*): numeric encryption
* kentucky_fryer (\*\*): turn text into Southern American English
* mad_libs: TBD
* markov_words (\*\*): Markov chain to generate words
* markov_chain (\*\*\*): Markov chain to generate text
* morse (\*\*\*): write a Morse encoder/decoder
* movie_reader (\*): print characters of text with movie pauses
* palindromes (\*): find palindromes in text
* picnic (\*): write the picnic game
* piggie (\*\*): encode text in Pig Latin
* ransom_note (\*): transform input text into RaNSom cASe.
* rhymer (\*): produce rhyming "words" from input text
* rock_paper_scissors (\*): write Rock, Paper, Scissors game
* rot13 (\*\*\*): ROT13-encode input text
* soundex-rhymer (\*\*): use Soundex to find rhyming words from a word list
* substring (\*\*): write a game to guess words sharing a common substring
* tictactoe (\*\*): write a Tic-Tac-Toe game
* twelve_days_of_christmas (\*\*): produce the "12 Days of Christmas" song
* war (\*\*): play the War card game

In addition, there are:

* appendix: texts on thing like data structures, regular expressions, etc. that are used in different exercises
* bin: useful programs like `new_py`

# Author

Ken Youens-Clark <kyclark@gmail.com>
