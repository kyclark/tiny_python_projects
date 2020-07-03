# WOD (Workout of the Day)

https://www.youtube.com/playlist?list=PLhOuww6rJJNM2jtyu3zw3aIeZ8Ov7hSy-

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

The file structure looks like this:

```
$ cat exercises.csv
exercise,reps
Burpees,20-50
Situps,40-100
Pushups,25-75
Squats,20-50
Pullups,10-30
Hand-stand pushups,5-20
Lunges,20-40
Plank,30-60
Crunches,20-30
```

The program should accept an `-n` or `--num` argument to control the number of exercises which are randomly chosen from the input file.
The "Reps" value will be randomly chosen from the given low/high range in the "reps" column:

```
$ ./wod.py -n 2
Exercise      Reps
----------  ------
Situps          83
Pullups         30
```

The program should accept a `-s` or `--seed` value for the random seed to ensure reproducibility:

```
$ ./wod.py -s 1
Exercise      Reps
----------  ------
Pushups         56
Situps          88
Crunches        27
Burpees         35
```

As well as a `-e` or `--easy` flag to indicate that the reps should be halved:

```
$ ./wod.py -s 1 -e
Exercise      Reps
----------  ------
Pushups         28
Situps          44
Crunches        13
Burpees         17
```

The program should print a usage for the `-h` or `--help` flags:

```
$ ./wod.py -h
usage: wod.py [-h] [-f str] [-s int] [-n int] [-e]

Create Workout Of (the) Day (WOD)

optional arguments:
  -h, --help          show this help message and exit
  -f str, --file str  CSV input file of exercises (default: exercises.csv)
  -s int, --seed int  Random seed (default: None)
  -n int, --num int   Number of exercises (default: 4)
  -e, --easy          Halve the reps (default: False)
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

The test suite only checks your program using well-formed input files.
There are several "bad" input files provided which are not used by the test but are provided for you to try with your program.
These represent several types of real-world problems you might encounter parsing delimited text files.
