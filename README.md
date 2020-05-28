# Introduction

This is the code repository for the Manning Publications book, _Tiny Python Projects_, by Ken Youens-Clark:

https://www.manning.com/books/tiny-python-projects?a_aid=youens&a_bid=b6485d52

http://tinypythonprojects.com/

There is a directory for each chapter of the book.
Each directory contains a `test.py` program you can use with `pytest` to check that you have written the program correctly.
I have included a short README to describe each exercise.
If you have problems writing code (or if you would like to support this project!), the book contains details about the skills you need.

The testing step is integral to writing and solving these challenges as well as to the methodology of the book.
I advocate a "test-driven development" mentality where we write tests _before_ we write code.
The tests should define what it means for a program to be correct, and then we write programs to satisfy the tests.
In this project, I've written all the tests for you, but I also encourage you to write your own functions and tests.
You should run the test suite after every change to your program to ensure you are making progress!

# Videos

I've been making videos for each chapter on my YouTube channel:

https://www.youtube.com/user/kyclark

Here are the videos I've completed so far:

* [Chapter 1: How to write and test a Python program](https://www.youtube.com/playlist?list=PLhOuww6rJJNP7UvTeF6_tQ1xcubAs9hvO): How to create a Python program, understanding comments and the shebang, how to make a program executable and install into your $PATH, how to write a main() function, add docstrings, format your code, and run tests.

* [Chapter 2: Crow's Nest](https://www.youtube.com/playlist?list=PLhOuww6rJJNPBqIwfD-0RedqsitBliLhT): How to write a Python program that accepts a single, positional argument and creates a newly formatted output string.

* [Chapter 3: Picnic](https://www.youtube.com/playlist?list=PLhOuww6rJJNMuQohHrNxRjhFTR9UlUOIa): Writing a Python program that accepts multiple string arguments and formats the results depending on the number of items.

* [Chapter 4: Jump The Five](https://www.youtube.com/playlist?list=PLhOuww6rJJNNd1Mbu3h6SGfhD-8rRxLTp): Writing a Python program to encode the numerals in a given text using an algorithm called "Jump The Five." Use of a dictionary as a lookup table, characters not in the dictionary remain unchanged. Introduction to encoding/decoding text, basic idea of encryption.

* [Chapter 5: Howler](https://www.youtube.com/playlist?list=PLhOuww6rJJNNzo5zqtx0388myQkUKyrQz): Writing a Python program that can process input text either from the command line or from a file.The output prints either to STDOUT or to a file.  Learning about "os.path.isfile", how to "open" a file handle for reading/writing, how to read/write the contents of a file.

* [Chapter 6: Word Count](https://www.youtube.com/playlist?list=PLhOuww6rJJNOGPw5Mu5FyhnumZjb9F6kk): Writing a Python program to emulate the `wc` (word count) program. Validates and processes multiple file inputs as well as STDIN and creates output of the counts of lines, words, and bytes for each file optionally with a "total" if more than one file is provided.

* [Chapter 7: Gashlycrumb](https://www.youtube.com/playlist?list=PLhOuww6rJJNMxWy34-9jlD2ulZxaA7mxV): Writing a Python program that processes an input file to build a lookup table (dictionary) that is used with multiple positional arguments to translate to the values from the file.

* [Chapter 8: Apples and Bananas](https://www.youtube.com/playlist?list=PLhOuww6rJJNMe_qrKzw6jtxzHkTOszozs): Writing a Python program to find and replace elements in a string. Exploring multiple ways to write the same idea from for loops to list comprehensions to higher-order functions like map().

* [Chapter 9: Abuse](https://www.youtube.com/playlist?list=PLhOuww6rJJNOWShq53st6NjXacHHaJurn): Writing a Python program to generate Shakespearean insults by randomly combining some number of adjectives with a randomly chosen noun. Learning about randomness, seeds, testing, how to use triple-quoted strings.

* [Chapter 10: Telephone](https://www.youtube.com/playlist?list=PLhOuww6rJJNN0T5ZKUFuEDo3ykOs1zxPU): Using probabalistic and deterministc approaches to randomly mutating a string.

* [Chapter 11: Bottles of Beer](https://www.youtube.com/playlist?list=PLhOuww6rJJNNGDXdGGfp3RDXBMhJwj0Ij): Writing a Python program to produce the verse to the "99 Bottles of Beer" song from a given starting point. Learning to count down, format strings, algorithm design. A focus on writing a function and unit test, exploring ways to incorporate our function to generate the verses from for loops to list comprehensions to map().

* [Chapter 12: Ransom](https://www.youtube.com/playlist?list=PLhOuww6rJJNMxWhckg7FO4cEx57WgHbd_): Writing a Python program that will randomly capitalize letters in a given piece of text for the nefarious purpose of creating a ransom note. Exploration of for loops, list comprehensions, and the map() function.

* [Chapter 13: Twelve Days of Christmas](https://www.youtube.com/playlist?list=PLhOuww6rJJNNZEMX12PE1OvSKy02UQoB4): Writing a Python program to create the verses for "The Twelve Days of Christmas" from a given day. Learning how to write a function and the test for it, then using the function in a list comprehension and a map to generate the output.

* [Chapter 14: The Rhymer](https://www.youtube.com/playlist?list=PLhOuww6rJJNPNn2qa5ATHJ0qd-JUgM_s0): Writing a Python program that can split off any initial consonants from a word and append a list of prefixes to create new rhyming "words." Exploration of regular expressions to handle words with no initial consonants, with one or more leading consonants, and nothing but consonants. Writing a `stemmer()` function and the `test_stemmer()` function to understand it. Using list comprehensions with guard statements and how that relates to the `filter()` function.

* [Chapter 15: The Kentucky Friar](https://www.youtube.com/playlist?list=PLhOuww6rJJNMflxi3aRAQTqG7mvOXRObW): In this chapter we delve further into regular expressions, first learning how to split a string using a regex so we can separate things that look like "words" from non-words like punctuation and whitespace. Then we try to identify the word "you" (case-insensitive) to turn into "y'all" and any 2-syllable words ending in "-ing" so we can replace the final "g" with an apostrophe so that "cooking" becomes "cookin'" but "swing" would remain "swing." We then apply this to an entire body of text to Kentucky fry the words with amusing results.

* [Chapter 16: The Scrambler](https://www.youtube.com/playlist?list=PLhOuww6rJJNPcLby3JXlKSo6duCIjh93S): Writing a Python program to find each "word" in a body of text and then scramble the letters such that the first and last letters remain in place, then reconstructing the text for output. Using regular expressions to split text, using `random.shuffle()` and understanding in-place mutation vs returning a new value. Comparing `for` loops to list comprehensions and the "map()" function.

* [Chapter 17: Mad Libs](https://www.youtube.com/playlist?list=PLhOuww6rJJNPnNx_Emds00y2RX1Tbk59r): Writing a Python program to play the classic Mad Libs game. Reading an input file with placeholders for parts of speech like "adjective" or "noun." Getting the inputs to replace those from the user interactively via the "input()" function or taking them from the command-line arguments. Using regular expressions to find and replace the placeholders. Learning about greedy regex and how to make them not greedy. Using the `re.findall()` and `re.sub()` functions. Using `sys.exit()` to prematurely exit a program with an error message/value.

# Forking GitHub repo

First use the GitHub interface to "fork" this repository into your own account. Then do `git clone` of *your* repository to get a local copy. Inside that checkout, do:

````
git remote add upstream https://github.com/kyclark/tiny_python_projects.git 
````

This will allow you to `git pull upstream master` in order to get updates. When you create new files, `git add/commit/push` them to *your* repository. (Please do not create pull requests on *my* repository -- unless, of course, you have suggestions for improving my repo!).

# Copyright

© Ken Youens-Clark 2019-2020
