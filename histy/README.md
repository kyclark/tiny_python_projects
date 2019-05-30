# Histogram

Write a Python program called `histy.py` that takes one or more integer values as positional argumements and creates a histogram of the values in their sorted order using the `-c|--character` (default "|") repeated by the number. Also accept a `-m|--minimum` option that is the minimum value to print a number as well as a `-s|--scale` option that will be used to scale the number of characters printed so that large numbers won't line wrap in your terminal.

````
$ ./histy.py
usage: histy.py [-h] [-c str] [-m int] [-s int] int [int ...]
histy.py: error: the following arguments are required: int
$ ./histy.py -h
usage: histy.py [-h] [-c str] [-m int] [-s int] int [int ...]

Histogrammer

positional arguments:
  int                   Inputs

optional arguments:
  -h, --help            show this help message and exit
  -c str, --character str
                        Character to represent (default: |)
  -m int, --minimum int
                        Minimum value to print (default: 1)
  -s int, --scale int   Scale inputs (default: 1)
$ ./histy.py 3 1 2
  1 |
  2 ||
  3 |||
$ ./histy.py 300 100 200 -s 100
100 |
200 ||
300 |||
$ ./histy.py 300 100 200 -s 100 -c '#'
100 #
200 ##
300 ###
$ ./histy.py 300 100 200 -s 100 -c '#' -m 150
200 ##
300 ###
````

# Test Suite

A passing test suite looks like this:

````
$ make test
pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-4.2.0, py-1.7.0, pluggy-0.8.1 -- /anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/worked_examples/2019_spring_finals/histogram_a, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.2.0, arraydiff-0.3
collected 6 items

test.py::test_usage PASSED                                               [ 16%]
test.py::test_01 PASSED                                                  [ 33%]
test.py::test_02 PASSED                                                  [ 50%]
test.py::test_03 PASSED                                                  [ 66%]
test.py::test_04 PASSED                                                  [ 83%]
test.py::test_05 PASSED                                                  [100%]

=========================== 6 passed in 0.43 seconds ===========================
````
