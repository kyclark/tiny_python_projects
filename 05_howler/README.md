# Howler

https://www.youtube.com/playlist?list=PLhOuww6rJJNNzo5zqtx0388myQkUKyrQz

Write a program that uppercases the given text:

```
$ ./howler.py 'The quick brown fox jumps over the lazy dog.'
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
```

If the text names a file, uppercase the contents of the file:

```
$ ./howler.py ../inputs/fox.txt
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
```

If given no arguments, print a brief usage:

```
$ ./howler.py
usage: howler.py [-h] [-o str] str
howler.py: error: the following arguments are required: str
```

If the `-o` or `--outfile` option is present, write the output to the given file and print nothing:

```
$ ./howler.py ../inputs/fox.txt -o out.txt
```

There should now be an `out.txt` file with the contents:

```
$ cat out.txt
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
```

Respond to `-h` or `--help` with a longer usage:

```
$ ./howler.py -h
usage: howler.py [-h] [-o str] str

Howler (upper-cases input)

positional arguments:
  str                   Input string or file

optional arguments:
  -h, --help            show this help message and exit
  -o str, --outfile str
                        Output filename (default: )
```

Run the test suite to ensure your program is working correctly:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 5 items

test.py::test_exists PASSED                                              [ 20%]
test.py::test_usage PASSED                                               [ 40%]
test.py::test_text_stdout PASSED                                         [ 60%]
test.py::test_text_outfile PASSED                                        [ 80%]
test.py::test_file PASSED                                                [100%]

============================== 5 passed in 0.40s ===============================
```
