# Getting Started

## Python Variables

Like most programming languages, Python has the idea of *one* of something and *many* of somethings, and these go into variables. Many are truly variable in Python, meaning we can neither keep them from changing nor enforce a *type* on them such as the idea that some variable can only ever contain an integer value. Some types are naturally immutable like strings and tuples. You'll learn which is which as we go.

Python variables can have a type like `int` for a integer value or `str` for "strings" which have one or more characters. When you create a variable, how you write the value determines it's type. Values in single or double quotes are strings (`str`):

````
>>> thing = 'chair'
>>> type(thing)
<class 'str'>
````

Bare numbers are either integers (`int`) if they are just numerals:

````
>>> thing = 10
>>> type(thing)
<class 'int'>
````

Or floating-pointing numbers (`float`) if they have fractional components:

````
>>> thing = 3.14
>>> type(thing)
<class 'float'>
>>> thing = 4.32e-10
>>> type(thing)
<class 'float'>
````

Each `type` of variable in Python has many helpful *methods* that can do things to the variable like `upper` (uppercase) a `str` or `append` to a `list`. In the REPL, you can use `help(str)` to see the documention on strings, for instance. Often you can use `help` directly on a variable and Python will show you the docs on the type of the variable.  

## Lists, Strings, and Tuples

A `list` in Python is an ordered sequencing of values. Python does not require them to be homogenous, so you can mix any sort of values you like. You can create a `list` by putting values in square brackets (`[]`):

````
>>> my_things = [3.14, 'banana', 42]
>>> type(my_things)
<class 'list'>
````

Like so many other programming languages, Python starts counting at zero `0`. You use the square brackets and the index to retrieve an element, so the first element of a `list` is found at `[0]`:

````
>>> my_things[0]
3.14
````

You can get multiple elements of a `list`, called a "slice", by using `[start:stop]` where both `start` and `stop` are optional. If you leave out `start`, it will be `0`; if you leave out `stop`, it will go to the end of the list. Note that the `stop` value is not inclusive:

````
>>> my_things[1:2]
['banana']
>>> my_things[1:]
['banana', 42]
>>> my_things[:2]
[3.14, 'banana']
````

Python uses the exact same notation to get elements from strings, which, if you squint a bit, a "string" is really just a `list` of characters:

````
>>> thing = 'orange'
>>> thing[1]
'r'
>>> thing[3:]
'nge'
````

Note that you can alter an element in a `list`:

````
>>> my_things[0] = 'cow'
>>> my_things
['cow', 'banana', 42]
````

But you cannot alter a string in the same way:

````
>>> thing[0] = 's'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
````

You can turn a `str` into a `list` using the `list()` function. This is handier than it might seem:

````
>>> list('apple')
['a', 'p', 'p', 'l', 'e']
````

Tuples are immutable lists and are created using parentheses (`()`) to enclose the items rather than square brackets. They are indexed in the same way as a `list` or `str` value.

````
>>> t = ('toast', 'butter', 'jam')
>>> t[1]
'butter'
````

## Dictionaries

If you need to associate some *thing* (a "key") to another *thing* (a "value"), generally you use a `dict` (dictionary). The key is unique in the `dict` and can be most any value as long as it is "hashable"; practically speaking, you can use a `str`, `int`, `float`, or `tuple` containing those kinds of values. You use curly brackets (`{}`) or the `dict()` function to create a new dictionary:

````
>>> d = {'name': 'Arthur', 'favorite color': 'blue'}
````

But you use square brackets (`[]`) to access members using a key:

````
>>> d['name']
'Arthur'
````

If you ask for a key that doesn't exist, bad things happen:

````
>>> d['quest']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'quest'
````

We'll talk later about types of dictionaries that don't blow up or that give you special powers like how to count all the elements in a `list`:

````
>>> from collections import Counter
>>> Counter('foobar')
Counter({'o': 2, 'f': 1, 'b': 1, 'a': 1, 'r': 1})
````

## Sets

A `set` is in between a `list` and a `dict`. Items in a `set` are unique like the keys of a `dict`, but they are in no particular order unlike a `list`. If you ever want the unique elements of a `list`, create a `set()`:

````
>>> set('foobar')
{'o', 'a', 'b', 'f', 'r'}
````


## Truthiness

While it would seem Python has an actual Boolean (Yes/No, True/False) type, this idea can be seriously abused in many odd and confusing ways. First off, there are actual `True` and `False` values:

````
>>> True == True
True
>>> False == False
True
````

But they are equivalent to integers:

````
>>> True == 1
True
>>> False == 0
True
````

Which means, oddly, that you can add them:

````
>>> True + True
2
>>> True + True + False
2
````

Lots of things are `False`-ey when they are evaluated in a Boolean context. The `int` `0`, the `float` `0.0`, the empty string, an empty list, and the special value `None` are all considered `False`-ey:

````
>>> 'Hooray!' if 0 else 'Shucks!'
'Shucks!'
>>> 'Hooray!' if 0. else 'Shucks!'
'Shucks!'
>>> 'Hooray!' if [] else 'Shucks!'
'Shucks!'
>>> 'Hooray!' if '' else 'Shucks!'
'Shucks!'
>>> 'Hooray!' if None else 'Shucks!'
'Shucks!'
````

But note:

````
>>> 'Hooray!' if 'None' else 'Shucks!'
'Hooray!'
````

There are quotes around `'None'` so it's the literal string "None" and not the special value `None`, and, since this is not an empty string, it evaluates *in a Boolean context* to not-`False` which is basically `True`.

This behavior can introduce extremely subtle logical bugs into your programs that the Python compiler and linters cannot uncover. Consider the `dict.get` method that will safely return the value for a given key in a dictionary, returning `None` if the key does not exist. Given this dictionary:

````
>>> d = {'foo': 0, 'bar': None}
````

If we access a key that doesn't exist, Python generates an exception that, if not caught in our code, would immediately crash the program:

````
>>> d['baz']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'baz'
````

But we can use `d.get()` to do this safely:

````
>>> d.get('baz')
````

Hmm, that seems unhelpful! What did we get back?

````
>>> type(d.get('baz'))
<class 'NoneType'>
````

Ah, we got `None`! 

We could use an `or` to define a default value:

````
>>> d.get('baz') or 'NA'
'NA'
````

It turns out the `get` method accepts a second, optional argument of the default value to return:

````
>>> d.get('baz', 'NA')
'NA'
````

Great! So let's use that on the other values:

````
>>> d.get('foo', 'NA')
0
>>> d.get('bar', 'NA')
````

The call for `bar` returned nothing because we put an actual `None` as the value:

````
>>> type(d.get('bar', 'NA'))
<class 'NoneType'>
````

The key `bar` didn't fail because that key exists in the dictionary. The `dict.get` method only returns the second, default argument *if the key does not exist in the dictionary* which is entirely different from checking the *value* of the key in the dictionary. OK, so we go back to this:

````
>>> d.get('bar') or 'NA'
'NA'
````

Which seems to work, but notice this:

````
>>> d.get('foo') or 'NA'
'NA'
````

The value for `foo` is actually `0` which evaluates to `False` given the Boolean evaluation of the `or`. If this were a measurement of some value like the amount of sodium in water, then the string `NA` would indicate that no value was recorded whereas `0` indicates that sodium was measured and none detected. If some sort of important analysis rested on our interpretation of the strings in a spreadsheet, we might inadvertently introduce missing values because of the way Python coerces various non-Boolean values into Boolean values.

Perhaps a safer way to access these values would be:

````
>>> for key in ['foo', 'bar', 'baz']:
...   val = d[key] if key in d else 'NA'
...   val = 'NA' if val is None else val
...   print(key, val)
...
foo 0
bar NA
baz NA
````

## Loops

In Python, you can use `for` to iterate through all the values in a sequence. You can use `continue` to skip to the next iteration of a loop:

````
>>> for char in 'foobar':
...     if char in 'aeiou':
...         continue
...     print(char.upper())
...
F
B
R
````

A `while` loop will execute as long as some condition is "truthy." 

````
>>> i = 2
>>> while i:
...     print(i)
...     i -= 1
...
2
1
````

You can use `break` to exit a `for` or `while` loop:

````
>>> for i in range(1, 10):
...     print(i)
...     if i % 3 == 0:
...         break
...
1
2
3
````

## Functions

The style I would teach is heavy on functions, even if they are only one line. In my opinion, no function should exceed 50 lines with the exception of the `get_args` to define your programs arguments and possibly the `main`. A function is defined using the `def` keyword:

````
>>> def say_goodnight_gracie():
...     print("Good night, Gracie!")
...
````

And called using the function name plus `()`:

````
>>> say_goodnight_gracie()
Good night, Gracie!
````

Without the parentheses, it's just the *idea* of the function:

````
>>> say_goodnight_gracie
<function say_goodnight_gracie at 0x100d737b8>
````

This will become important as we talk about "higher-order functions" later when we 

The *arguments* to a function are given in the parentheses in the `def`:

````
>>> def greet(name):
...     print('Hello, {}!'.format(name))
...
````

And you pass them inside the parentheses when you call the function:

````
>>> greet('Ilsa')
Hello, Ilsa!
````

## Parsing command-line arguments with argparse

The central tenet of this work is that you will write *command-line* programs. The reason is that we can pass in all the parameters to the program as *arguments* in order to change how the program works. This makes it fairly easy to *test* our programs, which is another fundamental aspect of the text. I strongly encourage you to use the `argparse` module to interpret all the command-line arguments for every program in this book.

### Types of arguments

Command-line arguments come in a variety of flavors:

* Positional: The order and number of the arguments is what determines their meaning. Some programs might expect, for instance, a file name as the first argument and an output directory as the second. 
* Named options: Standard Unix format allows for a "short" name like `-f` (one dash and a single character) or a "long" name like `--file` (two dashes and a string of characters) followed by some value like a file name or a number. This allows for arguments to be provided in any order or not provided in which case the program can use a reasonable default value.
* Flag: A "Boolean" value like "yes"/"no" or `True`/`False` usually indicated by something that looks like a named option but without a value, e.g., `-d` or `--debug` to turn on debugging. Typically the presence of the flag indicates a `True` value for the argument; therefore, it's absence would mean `False`, so `--debug` turns *on* debugging while no `--debug` flag means there should not no debugging.

### Datatypes of values

The `argparse` module can save you enormous amounts of time by forcing the user to provide arguments of a particular type. If you run `new.py`, all of the above types of arguments are present along with suggestions for how to get string or integer values:

````
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-f',
                        '--flag',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()
````

You should change the `description` to a short sentence describing your program. The `formatter_class` argument tells `argparse` to show the default values in the the standard help documentation. 

The `positional` argument's definition indicates we expect exactly one positional argument. The `-a` argument's `type` must be a `str` while the `-i` option must be something that Python can convert to the `int` type (you can also use `float`). Both of these arguments have `default` values which means the user is not required to provide them. You could instead define them with `required=True` to force the user to provide values themselves.

The `-f` flag notes that the `action` is to `store_true` which means the value's default with be `True` if the argument is present and `False` otherwise. 

The `type` of the argument can be something much richer than simple Python types like strings or numbers. You can indicate that an argument must be a existing, readable file. Here is a simple implementation in Python of `cat -n`:

````
#!/usr/bin/env python3
"""Python version of `cat -n`"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Input file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fh = args.file

    print('Reading "{}"'.format(fh.name))
    for i, line in enumerate(fh):
        print(i, line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
````

The `type` of the input `file` argument is an *open file handle* which we can directly read line-by-line with a `for` loop! Because it's a file *handle* and not a file *name*, I chose to call the variable `fh` to help me remember what it is. You can access the file's name via `fh.name`. 

````
$ ./cat_n.py ../../inputs/the-bustle.txt
Reading "../../inputs/the-bustle.txt"
0 The bustle in a house
1 The morning after death
2 Is solemnest of industries
3 Enacted upon earth,--
4
5 The sweeping up the heart,
6 And putting love away
7 We shall not want to use again
8 Until eternity.
````

### Number of arguments

If you want one positional argument, you can define them like so:

````
#!/usr/bin/env python3
"""One positional argument"""

import argparse

parser = argparse.ArgumentParser(
    description='One positional argument',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('first', metavar='str', help='First argument')
args = parser.parse_args()
print('first =', args.first)
````

If the user provides anything other exactly one argument, they get a help message:

````
$ ./one_arg.py
usage: one_arg.py [-h] str
one_arg.py: error: the following arguments are required: str
$ ./one_arg.py foo bar
usage: one_arg.py [-h] str
one_arg.py: error: unrecognized arguments: bar
$ ./one_arg.py foo
first = foo
````

If you want two different positional arguments:

````
#!/usr/bin/env python3
"""Two positional arguments"""

import argparse

parser = argparse.ArgumentParser(
    description='Two positional arguments',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('first', metavar='str', help='First argument')

parser.add_argument('second', metavar='int', help='Second argument')

return parser.parse_args()

print('first =', args.first)
print('second =', args.second)
````

Again, the user must provide exactly this number of positional arguments:

````
$ ./two_args.py
usage: two_args.py [-h] str str
two_args.py: error: the following arguments are required: str, str
$ ./two_args.py foo
usage: two_args.py [-h] str str
two_args.py: error: the following arguments are required: str
$ ./two_args.py foo bar
first = foo
second = bar
````

You can also use the `nargs=N` option to specify some number of arguments. It only makes sense if the arguments are the same thing like two files:

````
#!/usr/bin/env python3
"""nargs=2"""

import argparse

parser = argparse.ArgumentParser(
    description='nargs=2',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('files', metavar='FILE', nargs=2, help='Two files')

args = parser.parse_args()

file1, file2 = args.files
print('file1 =', file1)
print('file2 =', file2)
````

The help indicates we want two files:

````
$ ./nargs2.py foo
usage: nargs2.py [-h] FILE FILE
nargs2.py: error: the following arguments are required: FILE
````

And we can unpack the two file arguments and use them:

````
$ ./nargs2.py foo bar
file1 = foo
file2 = bar
````

If you want one or more of some argument, you can use `nargs='+'`:

````
$ cat nargs+.py
#!/usr/bin/env python3
"""nargs=+"""

import argparse

parser = argparse.ArgumentParser(
    description='nargs=+',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('files', metavar='FILE', nargs='+', help='Some files')

args = parser.parse_args()
files = args.files

print('number = {}'.format(len(files)))
print('files  = {}'.format(', '.join(files)))
````

Note that this will return a `list` -- even a single argument will become a `list` of one value:

````
$ ./nargs+.py
usage: nargs+.py [-h] FILE [FILE ...]
nargs+.py: error: the following arguments are required: FILE
$ ./nargs+.py foo
number = 1
files  = foo
$ ./nargs+.py foo bar
number = 2
files  = foo, bar
````

### Choices

Sometimes you want to limit the values of an argument. You can pass in a `list` of valid values to the `choices` option. 

````
$ cat appendix/argparse/choices.py
#!/usr/bin/env python3
"""Choices"""

import argparse

parser = argparse.ArgumentParser(
    description='Choices',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('color', metavar='str', help='Color', choices=['red', 'yellow', 'blue'])

args = parser.parse_args()

print('color =', args.color)
````

Any value not present in the list will be rejected and the user will be shown the valid choices:

````
$ ./choices.py
usage: choices.py [-h] str
choices.py: error: the following arguments are required: str
$ ./choices.py purple
usage: choices.py [-h] str
choices.py: error: argument str: invalid choice: 'purple' (choose from 'red', 'yellow', 'blue')
````

### Automatic help

The `argparse` module reserves the `-h` and `--help` flags for generating help documentation. You do not need to add these nor are you allowed to use these flags for other purposes. Using the above definition, this is the help that `argparse` will generate:

````
$ ./foo.py
usage: foo.py [-h] [-a str] [-i int] [-f] str
foo.py: error: the following arguments are required: str
[cholla@~/work/python/playful_python/article]$ ./foo.py -h
usage: foo.py [-h] [-a str] [-i int] [-f] str

Argparse Python script

positional arguments:
  str                A positional argument

optional arguments:
  -h, --help         show this help message and exit
  -a str, --arg str  A named string argument (default: )
  -i int, --int int  A named integer argument (default: 0)
  -f, --flag         A boolean flag (default: False)
````

Notice how unhelpful a name like `positional` is? 

### Getting the argument values

The values for the arguments will be accessible through the "long" name you define and will have been coerced to the Python data type you indicated. If I change `main` to this:

````
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    flag_arg = args.flag
    pos_arg = args.positional

    print('str_arg = "{}" ({})'.format(str_arg, type(str_arg)))
    print('int_arg = "{}" ({})'.format(int_arg, type(int_arg)))
    print('flag_arg = "{}" ({})'.format(flag_arg, type(flag_arg)))
    print('positional = "{}" ({})'.format(pos_arg, type(pos_arg)))
````

And then run it:

````
$ ./foo.py -a foo -i 4 -f bar
str_arg = "foo" (<class 'str'>)
int_arg = "4" (<class 'int'>)
flag_arg = "True" (<class 'bool'>)
positional = "bar" (<class 'str'>)
````

Notice how we might think that `-f` takes the argument `bar`, but it is defined as a `flag` and the `argparse` knows that the program take

````
$ ./foo.py foo -a bar -i 4 -f
str_arg = "bar" (<class 'str'>)
int_arg = "4" (<class 'int'>)
flag_arg = "True" (<class 'bool'>)
positional = "foo" (<class 'str'>)
````

## new.py

In my own practice, I almost never start writing a Python program from an empty page.
I have provided some useful programs in the `bin` directory of the GitHub repository including one called `new.py` that I use to stub out new Python programs using the `argparse` module to parse the command line arguments and options for your programs. I recommend you start every new program with this program. For example, in the `article` directory the `README.md` wants you to create a program called `article.py`. You should do this:

````
$ cd article
$ new.py article
````

This will create a new file called `article.py` (that has been made executable with `chmod +x`, if your operating system supports that) that has example code for you to start writing your program. 

## $PATH

Your `$PATH` is a list of directories where your operating system will look for programs. To see what your `$PATH` looks like, do:

````
$ echo $PATH
````

Probably each directory is separated by a colon (`:`). *The order of the directories matters!* For instance, it's common to have more than one version of Python installed. When you type `python` on the command line, the directories in your `$PATH` are searched in order, and the first `python` found is the one that is used (and it's probably Python version 2!)

You could execute `new.py` by giving the full path to the program, e.g., `$HOME/work/playful_python/bin/new.py`, but that's really tedious. It's best to put `new.py` into one of the directories that is already in your `$PATH` like maybe `/usr/local/bin`. The problem is that you probably need administrator privileges to write to most of the directories that are in your `$PATH`. If you are working on your laptop, this is probably not a problem, but if you are on a shared system, you probably won't be able to copy the program into your `$PATH` directories. 

An alternative is to alter your `$PATH` to include the directory where `new.py` is located. E.g., if `new.py` is in `$HOME/work/playful_python/bin/`, then add this directory to your `$PATH` -- probably by editing  `.bashrc` or `.bash_profile` located in your `$HOME` directory (if you use `bash`). See the documentation for your shell of choice to understand how to edit and persist your `$PATH`.

For what it's worth, I always create a `$HOME/.local` directory for local installations of software I need, so I add `$HOME/.local/bin` to my `$PATH`. Then I copy programs like `new.py` there and they are available to me anywhere on the system.

## Testing your programs

Once you have stubbed out your new program, open it in your favorite editor and change the example arguments in `get_args` to suit the needs of your app, then add your code to `main` to accomplish the task described in the README. To run the test suite using `make`, you can type `make test` in the same directory as the `test.py` and `article.py` program. If your system does not have `make` or you just don't want to use it, type `pytest -v test.py`. 

Your goal is to pass all the tests. The tests are written in an order designed to guide you in how break the problem down, e.g., often a test will ask you to alter one bit of text from the command line, and this it will ask you to read and alter the text from a file. I would suggest you solve the tests in order. The `make test` target in every Makefile executes `pytest -xv test.py` where the `-x` flag will have `pytest` halt testing after it finds one that fails. There's no point in running every test when one fails, so I think this is less frustrating that seeing perhaps hundreds of lines of failing tests shoot by.

A fair number of the program rely on a dictionary of English words. To be sure that you can reproduce my results, I include a copy of mine in `inputs/words.zip`.