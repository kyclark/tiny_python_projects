# Pig Latin

Write a Python program named `piggie.py` that takes one or more file names as positional arguments and converts all the words in them into "Pig Latin" (see rules below). Write the output to a directory given with the flags `-o|--outdir` (default `out-yay`) using the same basename as the input file, e.g., `input/foo.txt` would be written to `out-yay/foo.txt`. 

if a file argument names a non-existent file, print a warning to STDERR and skip that file. If the output directory does not exist, create it.

# Pig Latin Rules

1. If the word begins with consonants, e.g., "k" or "ch", move them to the end of the word and append "ay" so that "mouse" becomes "ouse-may" and "chair" becomes "air-chay."
2. If the word begins with a vowel, simple append "-yay" to the end, so "apple" is "apple-yay."

# Expected Output

````
$ ./piggie.py
usage: piggie.py [-h] [-o str] FILE [FILE ...]
piggie.py: error: the following arguments are required: FILE
$ ./piggie.py -h
usage: piggie.py [-h] [-o str] FILE [FILE ...]

Convert to Pig Latin

positional arguments:
  FILE                  Input file(s)

optional arguments:
  -h, --help            show this help message and exit
  -o str, --outdir str  Output directory (default: out-yay)
$ ./piggie.py inputs/nobody.txt -o out
  1: nobody.txt
Done, wrote 1 file to "out".
$ cat out/nobody.txt
I'm-yay obody-Nay o-Whay are-yay ou-yay
Are-yay ou-yay -yay obody-Nay -yay oo-tay
en-Thay eres-thay a-yay air-pay of-yay us-yay
ont-Day ell-tay eyd-thay advertise-yay -yay ou-yay ow-knay

ow-Hay eary-dray -yay o-tay e-bay -yay omebody-Say
ow-Hay ublic-pay -yay ike-lay a-yay og-Fray -yay
o-Tay ell-tay one's-yay ame-nay -yay e-thay ivelong-lay une-Jay -yay
o-Tay an-yay admiring-yay og-Bay
$ ./piggie.py inputs/*.txt
  1: gettysburg.txt
  2: nobody.txt
  3: usdeclar.txt
Done, wrote 3 files to "out-yay".
````

# Test Suite

A passing test suite look like this:

````
$ make test
pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-4.2.0, py-1.7.0, pluggy-0.8.1 -- /anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/worked_examples/2019_spring_finals/grad/piggie, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.2.0, arraydiff-0.3
collected 6 items

test.py::test_usage PASSED                                               [ 16%]
test.py::test_bad_input PASSED                                           [ 33%]
test.py::test_nobody PASSED                                              [ 50%]
test.py::test_gettysbury PASSED                                          [ 66%]
test.py::test_decl PASSED                                                [ 83%]
test.py::test_all PASSED                                                 [100%]

=========================== 6 passed in 0.48 seconds ===========================
````


