# Scrambler

https://www.youtube.com/playlist?list=PLhOuww6rJJNPcLby3JXlKSo6duCIjh93S

Write a program that will randomly scramble the middle parts of words of 3 letters or more in a given text which may come from the command line:

```
$ ./scrambler.py 'The quick brown fox jumps over the lazy dog.'
The qiuck bwron fox jmpus over the lzay dog.
```

Or from an input file:

```
$ ./scrambler.py ../inputs/fox.txt
The qucik borwn fox jpmus over the lazy dog.
```

The program should accept a `-s` or `--seed` value for the random seed to ensure reproducibility:

```
$ ./scrambler.py -s 1 ../inputs/fox.txt
The qicuk bwron fox jupms over the lazy dog.
```

It should print a usage if provided no arguments:

```
$ ./scrambler.py
usage: scrambler.py [-h] [-s int] str
scrambler.py: error: the following arguments are required: str
```

And a longer usage for `-h` or `--help`:

```
$ ./scrambler.py -h
usage: scrambler.py [-h] [-s int] str

Scramble the letters of words

positional arguments:
  str                 Input text or file

optional arguments:
  -h, --help          show this help message and exit
  -s int, --seed int  Random seed (default: None)
```

Run the test suite to ensure your program is working correctly:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 7 items

test.py::test_exists PASSED                                              [ 14%]
test.py::test_usage PASSED                                               [ 28%]
test.py::test_text1 PASSED                                               [ 42%]
test.py::test_text2 PASSED                                               [ 57%]
test.py::test_file_bustle PASSED                                         [ 71%]
test.py::test_file_fox PASSED                                            [ 85%]
test.py::test_file_spiders PASSED                                        [100%]

============================== 7 passed in 0.72s ===============================
```
