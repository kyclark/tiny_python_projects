# Telephone

https://www.youtube.com/playlist?list=PLhOuww6rJJNN0T5ZKUFuEDo3ykOs1zxPU

Write a program that randomly mutates some given text which may be given on the command line:

```
$ ./telephone.py 'The quick brown fox jumps over the lazy dog.'
You said: "The quick brown fox jumps over the lazy dog."
I heard : "The qu)ck brown HoN jumps over thf lazy dog."
```

Or from a file:

```
$ ./telephone.py ../inputs/fox.txt
You said: "The quick brown fox jumps over the lazy dog."
I heard : "=he quick brswn fox jumps over the*[azy dog."
```

The program should accept a `-m` or `--mutations` that is a floating point number between 0 and 1 that represents a percentage of mutations to introduce:

```
$ ./telephone.py -m .5 ../inputs/fox.txt
You said: "The quick brown fox jumps over the lazy dog."
I heard : "w\eeqhR$kBbxown|foGLFuvn| ooe: t'. l"zy d&:."
```

It should also accept a `-s` or `--seed` argument for the random seed to ensure reproducible results:

```
$ ./telephone.py -s 2 ../inputs/fox.txt
You said: "The quick brown fox jumps over the lazy dog."
I heard : "TheNqHick Crown fox jum_s over the lazy dog."
```

If provided no arguments, it should print a brief usage:

```
$ ./telephone.py
usage: telephone.py [-h] [-s int] [-m float] str
telephone.py: error: the following arguments are required: str
```

```
$ ./telephone.py -h
usage: telephone.py [-h] [-s int] [-m float] str

Telephone

positional arguments:
  str                   Input text or file

optional arguments:
  -h, --help            show this help message and exit
  -s int, --seed int    Random seed (default: None)
  -m float, --mutations float
                        Percent mutations (default: 0.1)
```

Run the test suite to ensure your program is correct:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 10 items

test.py::test_exists PASSED                                              [ 10%]
test.py::test_usage PASSED                                               [ 20%]
test.py::test_bad_seed_str PASSED                                        [ 30%]
test.py::test_bad_mutation_str PASSED                                    [ 40%]
test.py::test_bad_mutation PASSED                                        [ 50%]
test.py::test_for_echo PASSED                                            [ 60%]
test.py::test_now_cmd_s1 PASSED                                          [ 70%]
test.py::test_now_cmd_s2_m4 PASSED                                       [ 80%]
test.py::test_fox_file_s1 PASSED                                         [ 90%]
test.py::test_fox_file_s2_m6 PASSED                                      [100%]

============================== 10 passed in 0.82s ==============================
```
