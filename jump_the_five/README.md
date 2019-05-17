# Jump the Five

Write a program called `jump.py` that will encode any number using "jump-the-five" algorithm that selects as a replacement for a given number the number that is opposite the number on a US telephone pad if you jump over the 5. The numbers 5and 9 will exchange with each other. So, "1" jumps the 5 to become "9," "6" jumps the 5 to become "4," "5" becomes "0," etc.

````
   1  2  3
   4  5  6
   7  8  9
   #  0  *
````

If given no arguments, print a usage statement.

# Expected Behavior

````
$ ./jump.py
Usage: jump.py NUMBER
$ ./jump.py 555-1212
000-9898
$ ./jump.py 'Call 1-800-329-8044 today!'
Call 9-255-781-2566 today!
````

# Test Suite

A passing test looks like this:

````
$ make test
pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-4.2.0, py-1.7.0, pluggy-0.8.1 -- /anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/python/practical_python_for_data_science/ch06-python-dictionaries/exercises/jump_the_five_a, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.2.0, arraydiff-0.3
collected 3 items

test.py::test_usage PASSED                                               [ 33%]
test.py::test_01 PASSED                                                  [ 66%]
test.py::test_02 PASSED                                                  [100%]

=========================== 3 passed in 0.15 seconds ===========================
````
