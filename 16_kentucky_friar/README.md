# The Kentucky Friar

Write a program that will drop the final "g" of two-syllable words ending in "-ing" and also replace any occurrence of the word "you" (case-insensitive) with the word "y'all" so as to transform text into a dialect common to the US Deep South (from which your author hails).
The given text may come from the command line:

```
$ ./friar.py 'Do you want to do some cooking with me?'
Do y'all want to do some cookin' with me?
```

Or from an input file:

```
$ ./friar.py ../inputs/nobody.txt
I'm Nobody! Who are y'all?
Are y'all -- Nobody -- too?
Then there’s a pair of us!
Don't tell! they'd advertise -- y'all know!

How dreary -- to be -- Somebody!
How public -- like a Frog --
To tell one's name -- the livelong June --
To an admirin' Bog!
```

Note that one-syllable words ending with "-ing" should be unchanged:

```
$ ./friar.py swing
swing
```

If provided no arguments, the program should print a brief usage:

```
$ ./friar.py
usage: friar.py [-h] str
friar.py: error: the following arguments are required: str
```

Or a longer usage for `-h` and `--help`:

```
$ ./friar.py -h
usage: friar.py [-h] str

Southern fry text

positional arguments:
  str         Input text or file

optional arguments:
  -h, --help  show this help message and exit
```

Run the test suite to ensure your program works correctly:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 10 items

test.py::test_exists PASSED                                              [ 10%]
test.py::test_usage PASSED                                               [ 20%]
test.py::test_two_syllable_ing_words PASSED                              [ 30%]
test.py::test_one_syllable_ing_words PASSED                              [ 40%]
test.py::test_you_yall PASSED                                            [ 50%]
test.py::test_blake PASSED                                               [ 60%]
test.py::test_banner PASSED                                              [ 70%]
test.py::test_raven PASSED                                               [ 80%]
test.py::test_dickinson PASSED                                           [ 90%]
test.py::test_shakespeare PASSED                                         [100%]

============================== 10 passed in 0.73s ==============================
```
