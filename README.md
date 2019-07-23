# Introduction

> "Codes are a puzzle. A game, just like any other game." - Alan Turing

> "The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie

I believe you can learn serious things through silly games. I also think you will learn best by *doing*. This is a book of programming exercises. Each chapter includes a description of a program you should write with examples of how the program should work. Most importantly, each program includes tests so that you know if your program is working well enough. 

When you are done with this books you be able to:

* Write command-line Python programs
* Process a variety of command-line arguments, options, and flags
* Write and run tests for your programs and functions
* Manipulate of Python data structures including strings, lists, tuples, sets, dictionaries
* Use higher-order functions like `map` and `filter`
* Write and use regular expressions
* Read, parse, and write various text formats
* Use and control of randomness
* Create and use graphs, kmers, Markov chains, Hamming distance, the Soundex algorithm, and more

The first chapter will briefly introduce some aspects of the Python language, but I will assume some basic profiency with Python or some similar language. If you are coming from any other c-based language (even if it uses braces for blocks), I don't think you'll have any problem picking up Python.

## Forking GitHub repo

First use the GitHub interface to "fork" this repository into your own account. Then do `git clone` of *your* repository to get a local copy. Inside that checkout, do:

````
git remote add upstream https://github.com/kyclark/playful_python.git 
````

This will allow you to `git pull upstream master` in order to get updates. When you create new files, `git add/commit/push` them to *your* repository. (Please do not create pull requests on *my* repository -- unless, of course, you have suggestions for improving my repo!).


## Why Not Notebooks?

Notebooks are great for interactive exploration of data, especially if you want to visualize thing, but the downsides:

* Stored as JSON not line-oriented text, so no good `diff` tools
* Not easily shared
* Too easy to run cells out of order
* Hard to test
* No way to pass in arguments

I believe you can better learn how to create testable, **reproducible** software by writing command-line programs that always run from beginning to end and have a test suite. It's difficult to achieve that with Notebooks, but I do encourage you to explore Notebooks on your own.

## Code examples, the REPL

I always love when a language has a good REPL (read-evaluate-print-loop) tool. Python and Haskell both excel in this respect. For simplicity's sake, I show the standard REPL when you execute `python3` on the command-line, but you won't be able to copy and paste the same code examples there. For your own purposes, I suggest using the iPython REPL (`ipython`) instead.

## Code formatting and linting

Every program included has been automatically formatted with `yapf` (Yet Another Python Formatter), a tool from Google that can be customized with a configuration file. I encourage you to adopt and regularly a formatter (see also `black`) *after every modification to your program*. Sometimes I even set up the formatter to format every time I save my program.

I would also encourage you to look at code "linters" like `pylint` to find potential errors in your code that the Python interpreter itself will not compalain about. The `mypy` program can also be used as we introduce type hints.

## Organization

The exercises are roughly arranged from easier to harder. 

## Author

Ken Youens-Clark is a Sr. Scientific Programmer in the lab of Dr. Bonnie Hurwitz at the University of Arizona. He started college as a music major at the University of North Texas but changed to English lit for his BA in 1995. He started programming at his first job out of college, working through several languages and companies before landing in bioinformatics in 2001. In 2019 he earned his MS in Biosystems Engineering, and enjoys helping people learn programming. When he's not working, he likes playing music, riding bikes, cooking, and being with his wife and children.

## Copyright

© Ken Youens-Clark 2019
