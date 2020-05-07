# Rhymer

https://www.youtube.com/playlist?list=PLhOuww6rJJNPNn2qa5ATHJ0qd-JUgM_s0

Write a program that will create rhyming words for a given word by removing the initial consonant sounds and substituting other sounds.
Note that the given word should not appear in the output, so "cake" will be omitted from this run:

```
$ ./rhymer.py cake | head
bake
blake
brake
chake
clake
crake
dake
drake
fake
flake
```

The rhyming words will be created by adding all the consonants plus the following consonant clusters:

```
bl br ch cl cr dr fl fr gl gr pl pr sc 
sh sk sl sm sn sp st sw th tr tw thw wh wr 
sch scr shr sph spl spr squ str thr
```

The output should be sorted alphabetically.
If there is no initial consonant sound, then apply all the consonant sounds to the given word:

```
$ ./rhymer.py apple | tail
thwapple
trapple
twapple
vapple
wapple
whapple
wrapple
xapple
yapple
zapple
```

If provided no arguments, the program should print a short usage:

```
$ ./rhymer.py
usage: rhymer.py [-h] str
rhymer.py: error: the following arguments are required: str
```

And a longer usage for `-h` or `--help`:

```
$ ./rhymer.py -h
usage: rhymer.py [-h] str

Make rhyming "words"

positional arguments:
  str         A word to rhyme

optional arguments:
  -h, --help  show this help message and exit
```

Run the test suite to ensure your program is correct:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 7 items

test.py::test_exists PASSED                                              [ 14%]
test.py::test_usage PASSED                                               [ 28%]
test.py::test_take PASSED                                                [ 42%]
test.py::test_chair PASSED                                               [ 57%]
test.py::test_chair_uppercase PASSED                                     [ 71%]
test.py::test_apple PASSED                                               [ 85%]
test.py::test_no_vowels PASSED                                           [100%]

============================== 7 passed in 0.47s ===============================
```
