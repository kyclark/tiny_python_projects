# 99 Bottles of Beer

https://www.youtube.com/playlist?list=PLhOuww6rJJNNGDXdGGfp3RDXBMhJwj0Ij

Write a song that will generate the verses to the song "99 Bottles of Beer":

```
$ ./bottles.py | tail

2 bottles of beer on the wall,
2 bottles of beer,
Take one down, pass it around,
1 bottle of beer on the wall!

1 bottle of beer on the wall,
1 bottle of beer,
Take one down, pass it around,
No more bottles of beer on the wall!
```

If given a `-n` or `--num` argument, generate the verses from that number down to 0:

```
$ ./bottles.py -n 2
2 bottles of beer on the wall,
2 bottles of beer,
Take one down, pass it around,
1 bottle of beer on the wall!

1 bottle of beer on the wall,
1 bottle of beer,
Take one down, pass it around,
No more bottles of beer on the wall!
```

The program should respond to `-h` and `--help` with a usage:

```
$ ./bottles.py -h
usage: bottles.py [-h] [-n int]

Bottles of beer song

optional arguments:
  -h, --help         show this help message and exit
  -n int, --num int  How many bottles (default: 10)
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
test.py::test_bad_int PASSED                                             [ 37%]
test.py::test_float PASSED                                               [ 50%]
test.py::test_str PASSED                                                 [ 62%]
test.py::test_one PASSED                                                 [ 75%]
test.py::test_two PASSED                                                 [ 87%]
test.py::test_random PASSED                                              [100%]

============================== 8 passed in 0.91s ===============================
```
