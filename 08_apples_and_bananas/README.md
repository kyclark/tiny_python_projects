# Apples and Bananas

https://www.youtube.com/playlist?list=PLhOuww6rJJNMe_qrKzw6jtxzHkTOszozs

Write a program that will substitute all the vowels in a given text with a single vowel (default "a"):

```
$ ./apples.py 'The quick brown fox jumps over the lazy dog.'
Tha qaack brawn fax jamps avar tha lazy dag.
```

The `-v` or `--vowel` can be use to specify another vowel:

```
$ ./apples.py 'The quick brown fox jumps over the lazy dog.' -v i
Thi qiick briwn fix jimps ivir thi lizy dig.
```

The program should reject a `--vowel` that is not a vowel (a, e, i, o, u):

```
$ ./apples.py 'The quick brown fox jumps over the lazy dog.' -v x
usage: apples.py [-h] [-v str] str
apples.py: error: argument -v/--vowel: \
invalid choice: 'x' (choose from 'a', 'e', 'i', 'o', 'u')
```

The argument may name a file in which case you should read the contents of that file:

```
$ ./apples.py ../inputs/fox.txt --vowel u
Thu quuck bruwn fux jumps uvur thu luzy dug.
```

Given no arguments, the program should print a brief usage:

```
$ ./apples.py
usage: apples.py [-h] [-v str] str
apples.py: error: the following arguments are required: str
```

Or a longer usage for `-h` or `--help`:

```
$ ./apples.py -h
usage: apples.py [-h] [-v str] str

Apples and bananas

positional arguments:
  str                  Input text or file

optional arguments:
  -h, --help           show this help message and exit
  -v str, --vowel str  The vowel to substitute (default: a)
```

Run the test suite to ensure your program is correct:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 8 items

test.py::test_exists PASSED                                              [ 12%]
test.py::test_usage PASSED                                               [ 25%]
test.py::test_bad_vowel PASSED                                           [ 37%]
test.py::test_command_line PASSED                                        [ 50%]
test.py::test_command_line_with_vowel PASSED                             [ 62%]
test.py::test_command_line_with_vowel_preserve_case PASSED               [ 75%]
test.py::test_file PASSED                                                [ 87%]
test.py::test_file_with_vowel PASSED                                     [100%]

============================== 8 passed in 0.75s ===============================
```
