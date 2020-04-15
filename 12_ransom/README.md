# Ransom

https://www.youtube.com/playlist?list=PLhOuww6rJJNMxWhckg7FO4cEx57WgHbd_

Write a program that will randomly capitalize the letters in a given piece of text a la a ransom note.
The text may be provided on the command line:

```
$ ./ransom.py 'The quick brown fox jumps over the lazy dog.'
THe qUICk BrOWn fOX jumPS OVEr THE LAzy DOg.
```

Or with a file:

```
$ ./ransom.py ../inputs/fox.txt
THE QUicK BRown fox JuMPS OVER THe laZY dog.
```

Given no arguments, the program should print a brief usage:

```
$ ./ransom.py
usage: ransom.py [-h] [-s int] str
ransom.py: error: the following arguments are required: str
```

The program should accept a `-s` or `--seed` option to use as a random seed to ensure reproducibility:

```
$ ./ransom.py -s 1 ../inputs/fox.txt
thE QUICk BrOWn Fox jumpS OveR tHe LAzY dOg.
```

It should respond to `-h` and `--help` with a longer usage:

```
$ ./ransom.py -h
usage: ransom.py [-h] [-s int] str

Ransom Note

positional arguments:
  str                 Input text or file

optional arguments:
  -h, --help          show this help message and exit
  -s int, --seed int  Random seed (default: None)
```

Run the test suite to ensure your program is correct:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 6 items

test.py::test_exists PASSED                                              [ 16%]
test.py::test_usage PASSED                                               [ 33%]
test.py::test_text1 PASSED                                               [ 50%]
test.py::test_text2 PASSED                                               [ 66%]
test.py::test_file1 PASSED                                               [ 83%]
test.py::test_file2 PASSED                                               [100%]

============================== 6 passed in 0.62s ===============================
```
