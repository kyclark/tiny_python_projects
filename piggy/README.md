# Piggy (Pig Latin)

> "Sucks to your assmar" -- William Golding

Write a Python program named `piggy.py` that takes one or more file names as positional arguments and converts all the words in them into "Pig Latin" (see rules below). Write the output to a directory given with the flags `-o|--outdir` (default `out-yay`) using the same basename as the input file, e.g., `input/foo.txt` would be written to `out-yay/foo.txt`. 

If an argument names a non-existent file, print a warning to STDERR and skip that file. If the output directory does not exist, create it.

To create "Pig Latin":

1. If the word begins with consonants, e.g., "k" or "ch", move them to the end of the word and append "ay" so that "mouse" becomes "ouse-may" and "chair" becomes "air-chay."
2. If the word begins with a vowel, simple append "-yay" to the end, so "apple" is "apple-yay."

![He's speaking "pig" Latin. Get it?](images/pig.png)

The program should print a usage if given no arguments or the `-h|--help` flag:

````
$ ./piggy.py
usage: piggy.py [-h] [-o str] FILE [FILE ...]
piggy.py: error: the following arguments are required: FILE
[cholla@~/work/python/playful_python/piggie]$ ./piggy.py -h
usage: piggy.py [-h] [-o str] FILE [FILE ...]

Convert to Pig Latin

positional arguments:
  FILE                  Input file(s)

optional arguments:
  -h, --help            show this help message and exit
  -o str, --outdir str  Output directory (default: out-yay)
````

If given a bad input file, it should complain and indicate an error:

````
$ ./piggy.py lkdflk
usage: piggy.py [-h] [-o str] FILE [FILE ...]
piggy.py: error: argument FILE: can't open 'lkdflk': [Errno 2] \
No such file or directory: 'lkdflk'
````

For each file, write a new output file into the `--outdir`:

````
$ ./piggy.py ../inputs/sonnet-29.txt
  1: sonnet-29.txt
Done, wrote 1 file to "out-yay".
$ head -6 out-yay/sonnet-29.txt
onnet-Say 29
illiam-Way akespeare-Shay

en-Whay, in-yay isgrace-day ith-way ortune-fay and-yay en-may’s-yay eyes-yay,
I-yay all-yay alone-yay eweep-bay my-yay outcast-yay ate-stay,
And-yay ouble-tray eaf-day eaven-hay ith-way my-yay ootless-bay ies-cray,
$ ./piggy.py ../inputs/s*.txt
  1: scarlet.txt
  2: sonnet-29.txt
  3: spiders.txt
Done, wrote 3 files to "out-yay".
````

Hints:

* For the `file` argument, use `type=argparse.FileType('r')`
* First write a function that will create a Pig Latin version of just one word; write tests to verify that it does the right thing with words starting with vowels and with consonants
* Write a loop that prints the names of each input file
* Then write a loop inside that to read and print each line from a file
* Then figure out how to print each word on the line
* Then figure out how to print the Pig Latin version of each word on the line
