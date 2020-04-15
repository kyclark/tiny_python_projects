# Jump the Five

https://www.youtube.com/playlist?list=PLhOuww6rJJNNd1Mbu3h6SGfhD-8rRxLTp

Write a program that will encode any number in a given string using an algorightm to "jump the five" on a standard US telephone keypad such that "1" becomes "9," "4" becomes "6," etc. 
The "5" and the "0" will swap with each other.
Here is the entire substitution table:

```
1 => 9
2 => 8
3 => 7
4 => 6
5 => 0
6 => 4
7 => 3
8 => 2
9 => 1
0 => 5
```

Encode only the numbers and leave all other text alone:

```
$ ./jump.py 867-5309
243-0751
```

If given no arguments, present a brief usage:

```
$ ./jump.py
usage: jump.py [-h] str
jump.py: error: the following arguments are required: str
```

Respond to `-h` or `--help` with a longer usage:

```
$ ./jump.py -h
usage: jump.py [-h] str

Jump the Five

positional arguments:
  str         Input text

optional arguments:
  -h, --help  show this help message and exit
```

Run the test suite to ensure your program is working correctly:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 4 items

test.py::test_exists PASSED                                              [ 25%]
test.py::test_usage PASSED                                               [ 50%]
test.py::test_01 PASSED                                                  [ 75%]
test.py::test_02 PASSED                                                  [100%]

============================== 4 passed in 0.53s ===============================
```
