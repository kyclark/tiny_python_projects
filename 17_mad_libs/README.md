# Mad Libs

https://www.youtube.com/playlist?list=PLhOuww6rJJNPnNx_Emds00y2RX1Tbk59r

Write a "Mad Libs" program that will read a given file and prompt the user for the parts of speech indicated in angle brackets, e.g., `<verb>`, replacing those values and printing the new text a la the beloved "Mad Libs" game.
For example, the input file might look like this:

```
$ cat inputs/fox.txt
The quick <adjective> <noun> jumps <preposition> the lazy <noun>.
```

When run with this input, the program would prompt the user for "adjective," "noun," etc.
When all the answers have been collected, the new text will be printed:

```
$ ./mad.py inputs/fox.txt
Give me an adjective: scary
Give me a noun: chair
Give me a preposition: behind
Give me a noun: sky
The quick scary chair jumps behind the lazy sky.
```

In order to test, the program should also accept all the values as `-i` or `--inputs`:

```
$ ./mad.py inputs/fox.txt -i scary chair behind sky
The quick scary chair jumps behind the lazy sky.
```

If provided no arguments, the program should print a brief usage:

```
$ ./mad.py
usage: mad.py [-h] [-i [str [str ...]]] FILE
mad.py: error: the following arguments are required: FILE
```

Or a longer usage for `-h` or `--help`:

```
$ ./mad.py -h
usage: mad.py [-h] [-i [str [str ...]]] FILE

Mad Libs

positional arguments:
  FILE                  Input file

optional arguments:
  -h, --help            show this help message and exit
  -i [str [str ...]], --inputs [str [str ...]]
                        Inputs (for testing) (default: None)
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
test.py::test_bad_file PASSED                                            [ 42%]
test.py::test_no_blanks PASSED                                           [ 57%]
test.py::test_fox PASSED                                                 [ 71%]
test.py::test_help PASSED                                                [ 85%]
test.py::test_verona PASSED                                              [100%]

============================== 7 passed in 0.65s ===============================
```
