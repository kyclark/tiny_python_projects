# Picnic

https://www.youtube.com/playlist?list=PLhOuww6rJJNMuQohHrNxRjhFTR9UlUOIa

Write a program that will correctly format the items we're taking on our picnic.
For one item, it should print the one item:

```
$ ./picnic.py sandwiches
You are bringing sandwiches.
```

For two items, place "and" in between:

```
$ ./picnic.py sandwiches chips
You are bringing sandwiches and chips.
```

For three or more items, use commas and "and":

```
$ ./picnic.py sandwiches chips cake
You are bringing sandwiches, chips, and cake.
```

If the `--sorted` flag is present, the items should first be sorted:

```
$ ./picnic.py sandwiches chips cake --sorted
You are bringing cake, chips, and sandwiches.
```

If no items are given, print a brief usage:

```
$ ./picnic.py
usage: picnic.py [-h] [-s] str [str ...]
picnic.py: error: the following arguments are required: str
```

Respond to `-h` and `--help` with a longer usage:

```
$ ./picnic.py -h
usage: picnic.py [-h] [-s] str [str ...]

Picnic game

positional arguments:
  str           Item(s) to bring

optional arguments:
  -h, --help    show this help message and exit
  -s, --sorted  Sort the items (default: False)
```

Run the test suite to ensure your program is correct:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 7 items

test.py::test_exists PASSED                                              [ 14%]
test.py::test_usage PASSED                                               [ 28%]
test.py::test_one PASSED                                                 [ 42%]
test.py::test_two PASSED                                                 [ 57%]
test.py::test_more_than_two PASSED                                       [ 71%]
test.py::test_two_sorted PASSED                                          [ 85%]
test.py::test_more_than_two_sorted PASSED                                [100%]

============================== 7 passed in 0.51s ===============================
```
