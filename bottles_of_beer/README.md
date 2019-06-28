# Bottles of Beer Song

Write a Python program called `bottles.py` that takes a single option `-n|--num` which is an positive integer (default `10`) and prints the "<N> bottles of beer on the wall song." The program should also respond to `-h|--help` with a usage statement:

````
$ ./bottles.py -h
usage: bottles.py [-h] [-n INT]

Bottles of beer song

optional arguments:
  -h, --help         show this help message and exit
  -n INT, --num INT  How many bottles (default: 10)
````

If the `--num` argument is not an integer value, print an error message and stop the program:

````
$ ./bottles.py -n foo
usage: bottles.py [-h] [-n INT]
bottles.py: error: argument -n/--num: invalid int value: 'foo'
$ ./bottles.py -n 2.4
usage: bottles.py [-h] [-n INT]
bottles.py: error: argument -n/--num: invalid int value: '2.4'
````

If the `-n` argument is less than 1, die with '--num (<N>) must be > 0'. 

````
$ ./bottles.py -n -1
usage: bottles.py [-h] [-n INT]
bottles.py: error: --num (-1) must > 0
````

If the argument is good, then print the appropriate number of verses:

````					
$ ./bottles.py -n 1
1 bottle of beer on the wall,
1 bottle of beer,
Take one down, pass it around,
0 bottles of beer on the wall!

$ ./bottles.py | head
10 bottles of beer on the wall,
10 bottles of beer,
Take one down, pass it around,
9 bottles of beer on the wall!

9 bottles of beer on the wall,
9 bottles of beer,
Take one down, pass it around,
8 bottles of beer on the wall!
````

Hints:

* Start with `new.py` and add a named *option* with `-n` for the "short" flag and `--num_bottles` for the "long" flag name. Be sure to choose `int` for the `type`. Note that the `metavar` is just for displaying to the user and has no effect on validation the arguments `type`.
* Look into `parser.error` for how to get `argparse` to printing an error message along with the usage and halt the program.
* Be sure to make the "bottle" into the proper singular or plural depending on the number in the phrase, e.g., "1 bottle" or "0 bottles."
* Either run your program or do `make test` after *every single change to your program* to ensure that it compiles and is getting closer to passing the tests. Do not change three things and then run it. Make one change, then run or test it.
* If you use `make test`, it runs `pytest -xv test.py` where the `-x` flag tells `pytest` to stop after the first test failure. The tests are written in a order to help you complete the program. For instance, the first test just ensures that the program exists. The next one that you have some sort of handling of `--help` which would probably indicate that you're using `argparse` and so have defined your arguments. 
* Just try to pass each test in order. Focus on just one thing at a time. Create the program. Add the help. Handle bad arguments. Print just one verse. Print two verses. Etc.
* Read the next section on how to count down.

## Counting down

You are going to need to count down, so you'll need to consider how to do that. You can use `range` to get a list of integers from some a "start" (default `0`, inclusive) to an "stop" (not inclusive). The `range` function is "lazy" in that it won't actually generate the list until you ask for the numbers, so I could create a `range` generator for an absurdly large number like `range(10**1000)` and the REPL returns immediately. Try it! To force *see* the list of numbers, I can coerce it into a `list`:

````
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
````

OK, so maybe you were expecting the numbers 1-10? Welcome to "computer science" where we often starting counting at `0` and are quite often "off-by-one." To count 1 to 10, I have to do this:

````
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
````

Cool, cool, but we actually need to count *down*. You saw that this function works differently depending on whether you give it one argument (`10`) or two (`1, 11`). It also will do something different if you give it a third argument that represents the "step" of the numbers. So, to list every other number:

````
>>> list(range(1, 11, 2))
[1, 3, 5, 7, 9]
````

And to count *down*, reverse the start and stop and use `-1` for the step:

````
>>> list(range(11, 1, -1))
[11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
````

Wait, what? OK, the start number is inclusive and the stop is not. Try again:

````
>>> list(range(10, 0, -1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
````

There's a slightly easier way to get that list by using the `reversed` function:

````
>>> list(reversed(range(1, 11)))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
````


