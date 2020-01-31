# WOD (Workout of the Day)

Create a program that will read a CSV `-f` or `--file` of exercises (default `exercises.csv`) and create a Workout of the Day:

```
$ ./wod.py
Exercise              Reps
------------------  ------
Pushups                 74
Hand-stand pushups      10
Squats                  29
Burpees                 33
```

The program should accept an alternate `--file`:

```
$ ./wod.py -f silly-exercises.csv
Exercise                Reps
--------------------  ------
Erstwhile Lunges          18
Hanging Chads             90
Red Barchettas            36
Masochistic Eardowns      29
```

And should reject non-existent file arguments:

```
$ ./wod.py -f lkjdflkj
usage: wod.py [-h] [-f str] [-s int] [-n int] [-e]
wod.py: error: argument -f/--file: can't open 'lkjdflkj': \
[Errno 2] No such file or directory: 'lkjdflkj'
```

Run the test suite to ensure your program is working correctly:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 8 items

test.py::test_exists PASSED                                              [ 12%]
test.py::test_usage PASSED                                               [ 25%]
test.py::test_bad_num PASSED                                             [ 37%]
test.py::test_bad_file PASSED                                            [ 50%]
test.py::test_seed1 PASSED                                               [ 62%]
test.py::test_seed1_easy PASSED                                          [ 75%]
test.py::test_seed2_num8 PASSED                                          [ 87%]
test.py::test_seed4_num3_input2 PASSED                                   [100%]

============================== 8 passed in 0.64s ===============================
```
