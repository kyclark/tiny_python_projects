# Ransom

Create a Python program called `ransom.py` that will randomly capitalize the letters in a given word or phrase. The input text may also name a file in which case the text should come from the file. The program should take a `-s|--seed` argument for the `random.seed` to control randomness for the test suite. It should also respond to `-h|--help` for usage.

# Expected Behavior

````
$ ./ransom.py
usage: ransom.py [-h] [-s int] str
ransom.py: error: the following arguments are required: str
$ ./ransom.py -h
usage: ransom.py [-h] [-s int] str

Ransom Note

positional arguments:
  str                 Input text or file

optional arguments:
  -h, --help          show this help message and exit
  -s int, --seed int  Random seed (default: None)
$ cat fox.txt
The quick brown fox jumps over the lazy dog.
$ ./ransom.py fox.txt
the quiCK bROWn fOx JUMps OveR tHe LAzy Dog.
$ ./ransom.py -s 2 'The quick brown fox jumps over the lazy dog.'
the qUIck BROWN fOX JUmps ovEr ThE LAZY DOg.
````

# Test Suite

A passing test suite looks like the following:

````
$ make test
pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-4.2.0, py-1.7.0, pluggy-0.8.1 -- /anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/python/practical_python_for_data_science/ch09-python-games/exercises/ransom_a, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.2.0, arraydiff-0.3
collected 5 items

test.py::test_usage PASSED                                               [ 20%]
test.py::test_text1 PASSED                                               [ 40%]
test.py::test_text2 PASSED                                               [ 60%]
test.py::test_file1 PASSED                                               [ 80%]
test.py::test_file2 PASSED                                               [100%]

=========================== 5 passed in 0.61 seconds ===========================
````
