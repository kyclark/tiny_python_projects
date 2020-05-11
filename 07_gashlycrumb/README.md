# Gashlycrumb

https://www.youtube.com/playlist?list=PLhOuww6rJJNMxWy34-9jlD2ulZxaA7mxV

Write a program that prints the line from a file starting with a given letter:

```
$ ./gashlycrumb.py a
A is for Amy who fell down the stairs.
```

By default, the `-f` or `--file` should use the included `gashlycrumb.txt` file, but can be overridden:

```
$ ./gashlycrumb.py a -f alternate.txt
A is for Alfred, poisoned to death.
```

The structure of the file is such:

```
$ head alternate.txt
A is for Alfred, poisoned to death.
B is for Bertrand, consumed by meth.
C is for Cornell, who ate some glass.
D is for Donald, who died from gas.
E is for Edward, hanged by the neck.
F is for Freddy, crushed in a wreck.
G is for Geoffrey, who slit his wrist.
H is for Henry, who's neck got a twist.
I is for Ingrid, who tripped down a stair.
J is for Jered, who fell off a chair.
```

The program should accept one or more letters as positional arguments, printing each line or a message that the given argument is not present in the file:

```
$ ./gashlycrumb.py x 4 z -f alternate.txt
X is for Xavier, stuck through with a prong.
I do not know "4".
Z is for Zora, smothered by a fleece.
```

If given no arguments, it should print a brief usage:

```
$ ./gashlycrumb.py
usage: gashlycrumb.py [-h] [-f FILE] letter [letter ...]
gashlycrumb.py: error: the following arguments are required: letter
```

Or a longer usage for `-h` or `--help`:

```
$ ./gashlycrumb.py -h
usage: gashlycrumb.py [-h] [-f FILE] letter [letter ...]

Gashlycrumb

positional arguments:
  letter                Letter(s)

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input file (default: gashlycrumb.txt)
```

The program should reject a bad `--file` argument:

```
$ ./gashlycrumb.py -f alskdf
usage: gashlycrumb.py [-h] [-f str] str [str ...]
gashlycrumb.py: error: argument -f/--file: can't open 'alskdf': \
[Errno 2] No such file or directory: 'alskdf'
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
test.py::test_bad_file PASSED                                            [ 37%]
test.py::test_a PASSED                                                   [ 50%]
test.py::test_b_c PASSED                                                 [ 62%]
test.py::test_y PASSED                                                   [ 75%]
test.py::test_o_alternate PASSED                                         [ 87%]
test.py::test_bad_letter PASSED                                          [100%]

============================== 8 passed in 0.50s ===============================
```
