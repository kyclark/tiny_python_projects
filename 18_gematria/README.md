# Gematria

https://www.youtube.com/playlist?list=PLhOuww6rJJNMI45XbeSAiLdivKhzygwgr

Write a program that will encode each word of a given text by summing the ASCII values of the characters.
The text may come from the command line:

```
$ ./gematria.py 'The quick brown fox jumps over the lazy dog.'
289 541 552 333 559 444 321 448 314
```

Or from an input file:

```
$ ./gematria.py ../inputs/fox.txt
289 541 552 333 559 444 321 448 314
```

When run with no arguments, the program should print a brief usage:

```
$ ./gematria.py
usage: gematria.py [-h] str
gematria.py: error: the following arguments are required: str
```

Or a longer usage for `-h` and `--help`:

```
$ ./gematria.py -h
usage: gematria.py [-h] str

Gematria

positional arguments:
  str         Input text or file

optional arguments:
  -h, --help  show this help message and exit
```

Run the test suite to ensure that your program is working correctly:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 6 items

test.py::test_exists PASSED                                              [ 16%]
test.py::test_usage PASSED                                               [ 33%]
test.py::test_text PASSED                                                [ 50%]
test.py::test_fox PASSED                                                 [ 66%]
test.py::test_spiders PASSED                                             [ 83%]
test.py::test_sonnet PASSED                                              [100%]

============================== 6 passed in 0.60s ===============================
```
