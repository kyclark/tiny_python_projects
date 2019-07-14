# I Get Histy

Write a Python program called `histy.py` that takes a single positional argument that may be plain text or the name of a file to read for the text. Count the frequency of each character (not spaces) and print a histogram of the data. By default, you should order the histogram by the characters but include `-f|--frequency_sort` option to sort by the frequency (in descending order). Also include a `-s|--symbol` option (default `|`) to represent a mark in the histogram, a `-m|--minimum` option (default `1`) to include a character in the output, a `-w|--width` option (default `70`) to limit the size of the histogram, and a `-i|--case_insensitive` flag to force all input to uppercase.

When run with no arguments or the `-h|--help` flag, print a usage:

````
$ ./histy.py
usage: histy.py [-h] [-s str] [-m int] [-w int] [-i] [-f] str
histy.py: error: the following arguments are required: str
$ ./histy.py -h
usage: histy.py [-h] [-s str] [-m int] [-w int] [-i] [-f] str

Histogrammer

positional arguments:
  str                   Input text or file

optional arguments:
  -h, --help            show this help message and exit
  -s str, --symbol str  Symbol for marks (default: |)
  -m int, --minimum int
                        Minimum frequency to print (default: 1)
  -w int, --width int   Maximum width of output (default: 70)
  -i, --case_insensitive
                        Case insensitive search (default: False)
  -f, --frequency_sort  Sort by frequency (default: False)
````

Error out if the `--symbol` is not a single character:

````
$ ./histy.py -s XX foobar
usage: histy.py [-h] [-s str] [-m int] [-w int] [-i] [-f] str
histy.py: error: --symbol "XX" must be one character
````

Accept text on the command line. Note that the default sorting should be *case-insensitive* so that `I` follows immediately here after `h`:

````
$ ./histy.py "I don't want the world, I just want your half."
a      3 |||
d      2 ||
e      1 |
f      1 |
h      2 ||
I      2 ||
j      1 |
l      2 ||
n      3 |||
o      3 |||
r      2 ||
s      1 |
t      5 |||||
u      2 ||
w      3 |||
y      1 |
````

Or an input file:

````
$ ./histy.py -i ../inputs/fox.txt -m 2
E      3 |||
H      2 ||
O      4 ||||
R      2 ||
T      2 ||
U      2 ||
````

Note that short flags can be combined:

````
$ ./histy.py ../inputs/const.txt -fim 100 -w 50 -s '#'
E     50 ##################################################
T     36 ####################################
S     26 ##########################
O     26 ##########################
A     26 ##########################
N     25 #########################
I     23 #######################
R     21 #####################
H     19 ###################
L     14 ##############
D     12 ############
C     11 ###########
F      9 #########
U      8 ########
P      7 #######
M      7 #######
B      5 #####
Y      4 ####
V      4 ####
G      4 ####
W      3 ###
````

## Counting, filtering, scaling and sorting text

I chose to create a single function called `count(text, minimum=0, width=0, frequency_sort=False)` that filters the input text to only characters, counts the letter frequencies, filters by a minimum count, scales the numbers down by a maximum width, and sorts the values by the character or by the frequency. I put the following function inside my `histy.py` program that verifies that I get expected results. I encourage you to do the same and then run `pytest -v histy.py` on your program to check your function:

````
def test_count():
    """Test count"""

    text = '"ab,Bc CC: dd_d-d"'
    assert count(text) == [('a', 1), ('B', 1), ('b', 1), ('C', 2), ('c', 1),
                           ('d', 4)]

    assert count(text, minimum=2) == [('C', 2), ('d', 4)]

    assert count(text, frequency_sort=True) == [('d', 4), ('C', 2), ('c', 1),
                                                ('b', 1), ('a', 1), ('B', 1)]

    assert count(text, frequency_sort=True, minimum=2) == [('d', 4), ('C', 2)]

    assert count(text, width=3) == [('a', 0), ('B', 0), ('b', 0), ('C', 1),
                                    ('c', 0), ('d', 3)]
````

Once you have the results of this, you need to create the histogram by printing the `--symbol` the number of times shown for each character.

## Hints

* Put all your input validation into `get_args` and use `parser.error` to error out
* A regular expression plus the `filter` function can help you remove any characters from the input text that are not in the set of ASCII characters "a-zA-Z"
* Look at `collections.Counter` for counting the characters