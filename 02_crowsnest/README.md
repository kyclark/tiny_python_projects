# Crow's Nest

https://www.youtube.com/playlist?list=PLhOuww6rJJNPBqIwfD-0RedqsitBliLhT

Write a program that will announce the appearance of something "off the larboard bow" to the captain of the ship.
Note that you need to "a" before a word starting with a consonant:

```
$ ./crowsnest.py narwhal
Ahoy, Captain, a narwhal off the larboard bow!
```

Or "an" before a word starting with a vowel:

```
$ ./crowsnest.py octopus
Ahoy, Captain, an octopus off the larboard bow!
```

Given no arguments, the program should print a brief usage:

```
$ ./crowsnest.py
usage: crowsnest.py [-h] str
crowsnest.py: error: the following arguments are required: str
```

It should print a longer usage for `-h` and `--help`:

```
$ ./crowsnest.py -h
usage: crowsnest.py [-h] str

Crow's Nest -- choose the correct article

positional arguments:
  str         A word

optional arguments:
  -h, --help  show this help message and exit
```

A passing test suite looks like this:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 6 items

test.py::test_exists PASSED                                              [ 16%]
test.py::test_usage PASSED                                               [ 33%]
test.py::test_consonant PASSED                                           [ 50%]
test.py::test_consonant_upper PASSED                                     [ 66%]
test.py::test_vowel PASSED                                               [ 83%]
test.py::test_vowel_upper PASSED                                         [100%]

============================== 6 passed in 2.89s ===============================
```
