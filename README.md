# Introduction

This is the code repository for the Manning Publications book, _Tiny Python Projects_, by Ken Youens-Clark:

https://www.manning.com/books/tiny-python-projects?a_aid=youens&a_bid=b6485d52

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

# Forking GitHub repo

First use the GitHub interface to "fork" this repository into your own account. Then do `git clone` of *your* repository to get a local copy. Inside that checkout, do:

````
git remote add upstream https://github.com/kyclark/tiny_python_projects.git 
````

This will allow you to `git pull upstream master` in order to get updates. When you create new files, `git add/commit/push` them to *your* repository. (Please do not create pull requests on *my* repository -- unless, of course, you have suggestions for improving my repo!).

# Copyright

© Ken Youens-Clark 2019-2020
