# Chapter 1

# Howler

Write a Python program `howler.py` that will uppercase all the text from the command line or from a file.

````
$ ./howler.py
usage: howler.py [-h] [-o str] STR
howler.py: error: the following arguments are required: STR
$ ./howler.py -h
usage: howler.py [-h] [-o str] STR

Howler (upper-case input)

positional arguments:
  STR                   Input string or file

optional arguments:
  -h, --help            show this help message and exit
  -o str, --outfile str
                        Output filename (default: )
$ ./howler.py 'One word: Plastics!'
ONE WORD: PLASTICS!
$ ./howler.py ../inputs/fox.txt
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
````

\pagebreak

# howler Solution

````
     1	#!/usr/bin/env python3
     2	"""Howler"""
     3	
     4	import argparse
     5	import os
     6	import sys
     7	
     8	
     9	# --------------------------------------------------
    10	def get_args():
    11	    """get command-line arguments"""
    12	    parser = argparse.ArgumentParser(
    13	        description='Howler (upper-case input)',
    14	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    15	
    16	    parser.add_argument('text', metavar='STR', help='Input string or file')
    17	
    18	    parser.add_argument('-o',
    19	                        '--outfile',
    20	                        help='Output filename',
    21	                        metavar='str',
    22	                        type=str,
    23	                        default='')
    24	
    25	    return parser.parse_args()
    26	
    27	
    28	# --------------------------------------------------
    29	def main():
    30	    """Make a jazz noise here"""
    31	    args = get_args()
    32	    text = args.text
    33	    out_file = args.outfile
    34	
    35	    if os.path.isfile(text):
    36	        text = open(text).read().strip()
    37	
    38	    out_fh = open(out_file, 'wt') if out_file else sys.stdout
    39	    out_fh.write(text.upper() + '\n')
    40	
    41	
    42	# --------------------------------------------------
    43	if __name__ == '__main__':
    44	    main()
````

\pagebreak

# Chapter 2

# Jump the Five

Write a program called `jump.py` that will encode any number using "jump-the-five" algorithm that selects as a replacement for a given number the number that is opposite the number on a US telephone pad if you jump over the 5. The numbers 5and 9 will exchange with each other. So, "1" jumps the 5 to become "9," "6" jumps the 5 to become "4," "5" becomes "0," etc.

````
   1  2  3
   4  5  6
   7  8  9
   #  0  *
````

If given no arguments, print a usage statement.

````
$ ./jump.py
Usage: jump.py NUMBER
$ ./jump.py 555-1212
000-9898
$ ./jump.py 'Call 1-800-329-8044 today!'
Call 9-255-781-2566 today!
````

\pagebreak

# jump_the_five Solution

````
     1	#!/usr/bin/env python3
     2	"""Jump the Five"""
     3	
     4	import os
     5	import sys
     6	
     7	
     8	# --------------------------------------------------
     9	def main():
    10	    """Make a jazz noise here"""
    11	
    12	    args = sys.argv[1:]
    13	
    14	    if len(args) != 1:
    15	        print('Usage: {} NUMBER'.format(os.path.basename(sys.argv[0])))
    16	        sys.exit(1)
    17	
    18	    num = args[0]
    19	    jumper = {
    20	        '1': '9',
    21	        '2': '8',
    22	        '3': '7',
    23	        '4': '6',
    24	        '5': '0',
    25	        '6': '4',
    26	        '7': '3',
    27	        '8': '2',
    28	        '9': '1',
    29	        '0': '5'
    30	    }
    31	
    32	    for char in num:
    33	        print(jumper[char] if char in jumper else char, end='')
    34	    print()
    35	
    36	
    37	# --------------------------------------------------
    38	if __name__ == '__main__':
    39	    main()
````

\pagebreak

# Chapter 3

# Bottles of Beer Song

Write a Python program called `bottles.py` that takes a single option `-n|--num_bottles` which is an positive integer (default 10) and prints the "<N> bottles of beer on the wall song." If the `-n` argument is less than 1, die with "N (<N>) must be a positive integer". The program should also respond to `-h|--help` with a usage statement.

I'd encourage you to think about the program as a formal algorithm. Read the introduction to Jeff Erickson's book _Algorithms_ available here:

* http://jeffe.cs.illinois.edu/teaching/algorithms/#book
* http://jeffe.cs.illinois.edu/teaching/algorithms/book/00-intro.pdf


You are going to need to count down, so you'll need to consider how to do that. First, let's examine a list and see how it can be sorted and reversed. We've already used the `sorted` *function*, but we haven't really talked about the `list` class's `sort` *method*. Note that the former does not mutate the list itself:

````
>>> a = ['foo', 'bar', 'baz']
>>> sorted(a)
['bar', 'baz', 'foo']
>>> a
['foo', 'bar', 'baz']
````

But the `sort` method does:

````
>>> a.sort()
>>> a
['bar', 'baz', 'foo']
````

Also, note what is returned by `sort`:

````
>>> type(a.sort())
<type 'NoneType'>
````

So if you did this, you'd destroy your data:

````
>>> a = a.sort()
>>> a
````

As with `sort`/`sorted`, so it goes with `reverse`/`reversed`. The past participle version *returns a new copy of the data without affecting the original* and is therefore the safest bet to use:

````
>>> a = ['foo', 'bar', 'baz']
>>> a
['foo', 'bar', 'baz']
>>> reversed(a)
<listreverseiterator object at 0x10f0d61d0>
>>> list(reversed(a))
['baz', 'bar', 'foo']
>>> a
['foo', 'bar', 'baz']
````

Compare with:

````
>>> a.reverse()
>>> a
['baz', 'bar', 'foo']
````

Given that and your knowledge of how `range` works, can you figure out how to count down, say, from 10 to 1?

````
$ ./bottles.py -h
usage: bottles.py [-h] [-n INT]

Bottles of beer song

optional arguments:
  -h, --help            show this help message and exit
  -n INT, --num_bottles INT
$ ./bottles.py --help
usage: bottles.py [-h] [-n INT]

Bottles of beer song

optional arguments:
  -h, --help            show this help message and exit
  -n INT, --num_bottles INT
                        How many bottles (default: 10)
$ ./bottles.py -n 1
1 bottle of beer on the wall,
1 bottle of beer,
Take one down, pass it around,
0 bottles of beer on the wall!

$ ./bottles.py | head
10 bottles of beer on the wall,
10 bottles of beer,
Take one down, pass it around,
9 bottles of beer on the wall!

9 bottles of beer on the wall,
9 bottles of beer,
Take one down, pass it around,
8 bottles of beer on the wall!
````

\pagebreak

# bottles_of_beer Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import sys
     5	from dire import die
     6	
     7	
     8	# --------------------------------------------------
     9	def get_args():
    10	    """get command-line arguments"""
    11	    parser = argparse.ArgumentParser(
    12	        description='Bottles of beer song',
    13	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    14	
    15	    parser.add_argument('-n',
    16	                        '--num_bottles',
    17	                        metavar='INT',
    18	                        type=int,
    19	                        default=10,
    20	                        help='How many bottles')
    21	
    22	    return parser.parse_args()
    23	
    24	
    25	# --------------------------------------------------
    26	def main():
    27	    """Make a jazz noise here"""
    28	    args = get_args()
    29	    num_bottles = args.num_bottles
    30	
    31	    if num_bottles < 1:
    32	        die('N ({}) must be a positive integer'.format(num_bottles))
    33	
    34	    line1 = '{} bottle{} of beer on the wall'
    35	    line2 = '{} bottle{} of beer'
    36	    line3 = 'Take one down, pass it around'
    37	    tmpl = ',\n'.join([line1, line2, line3, line1 + '!'])
    38	
    39	    for n in reversed(range(1, num_bottles + 1)):
    40	        s1 = '' if n == 1 else 's'
    41	        s2 = '' if n - 1 == 1 else 's'
    42	        print(tmpl.format(n, s1, n, s1, n - 1, s2))
    43	        if n > 1: print()
    44	
    45	
    46	# --------------------------------------------------
    47	if __name__ == '__main__':
    48	    main()
````

\pagebreak

# Chapter 4

# Picnic

Write a Python program called `picnic.py` that accepts one or more positional arguments as the items to bring on a picnic. In response, print "You are bringing ..." where "..." should be replaced according to the number of items where:

1. If one item, just state, e.g., if "chips" then "You are bringing chips."
2. If two items, put "and" in between, e.g., if "chips soda" then "You are bringing chips and soda."
3. If three or more items, place commas between all the items INCLUDING BEFORE THE FINAL "and" BECAUSE WE USE THE OXFORD COMMA, e.g., if "chips soda cupcakes" then "You are bringing chips, soda, and cupcakes."

````
$ ./picnic.py
usage: picnic.py [-h] str [str ...]
picnic.py: error: the following arguments are required: str
$ ./picnic.py -h
usage: picnic.py [-h] str [str ...]

Picnic game

positional arguments:
  str         Item(s) to bring

optional arguments:
  -h, --help  show this help message and exit
$ ./picnic.py chips
You are bringing chips.
$ ./picnic.py "potato chips" salad
You are bringing potato chips and salad.
$ ./picnic.py "potato chips" salad soda cupcakes
You are bringing potato chips, salad, soda, and cupcakes.
````

\pagebreak

# picnic Solution

````
     1	#!/usr/bin/env python3
     2	"""Picnic game"""
     3	
     4	import argparse
     5	
     6	
     7	# --------------------------------------------------
     8	def get_args():
     9	    """Get command-line arguments"""
    10	
    11	    parser = argparse.ArgumentParser(
    12	        description='Picnic game',
    13	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    14	
    15	    parser.add_argument('item',
    16	                        metavar='str',
    17	                        nargs='+',
    18	                        help='Item(s) to bring')
    19	
    20	    return parser.parse_args()
    21	
    22	
    23	# --------------------------------------------------
    24	def main():
    25	    """Make a jazz noise here"""
    26	
    27	    args = get_args()
    28	    items = args.item
    29	    num = len(items)
    30	
    31	    bringing = items[0] if num == 1 else ' and '.join(
    32	        items) if num == 2 else ', '.join(items[:-1] + ['and ' + items[-1]])
    33	
    34	    print('You are bringing {}.'.format(bringing))
    35	
    36	
    37	# --------------------------------------------------
    38	if __name__ == '__main__':
    39	    main()
````

\pagebreak

# Chapter 5

# Apples and Bananas

Perhaps you remember the children's song "Apples and Bananas"?

    I like to eat, eat, eat apples and bananas
    I like to eat, eat, eat apples and bananas

    I like to ate, ate, ate ay-ples and ba-nay-nays
    I like to ate, ate, ate ay-ples and ba-nay-nays

    I like to eat, eat, eat ee-ples and bee-nee-nees
    I like to eat, eat, eat ee-ples and bee-nee-nees

Write a Python program called `apples.py` that will turn all the vowels in some given text in a single positional argument into just one `-v|--vowel` (default "a") like this song. It should complain if the `--vowel` argument isn't a single, lowercase vowel (hint, see `choices` in the `argparse` documentation). If the given text argument is a file, read the text from the file. Replace all vowels with the given vowel, both lower- and uppercase.

````
$ ./apples.py
usage: apples.py [-h] [-v str] str
apples.py: error: the following arguments are required: str
$ ./apples.py -h
usage: apples.py [-h] [-v str] str

Apples and bananas

positional arguments:
  str                  Input text or file

optional arguments:
  -h, --help           show this help message and exit
  -v str, --vowel str  The only vowel allowed (default: a)
$ ./apples.py -v x foo
usage: apples.py [-h] [-v str] str
apples.py: error: argument -v/--vowel: invalid choice: 'x' (choose from 'a', 'e', 'i', 'o', 'u')
$ ./apples.py foo
faa
$ ./apples.py ../inputs/fox.txt
Tha qaack brawn fax jamps avar tha lazy dag.
````

\pagebreak

# apples_and_bananas Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import os
     5	import re
     6	import sys
     7	
     8	
     9	# --------------------------------------------------
    10	def get_args():
    11	    """get command-line arguments"""
    12	    parser = argparse.ArgumentParser(
    13	        description='Apples and bananas',
    14	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    15	
    16	    parser.add_argument('text', metavar='str', help='Input text or file')
    17	
    18	    parser.add_argument('-v',
    19	                        '--vowel',
    20	                        help='The vowel(s) allowed',
    21	                        metavar='str',
    22	                        type=str,
    23	                        default='a',
    24	                        choices=list('aeiou'))
    25	
    26	    return parser.parse_args()
    27	
    28	
    29	# --------------------------------------------------
    30	def main():
    31	    """Make a jazz noise here"""
    32	    args = get_args()
    33	    text = args.text
    34	    vowel = args.vowel
    35	
    36	    if os.path.isfile(text):
    37	        text = open(text).read()
    38	
    39	    # Method 1: Iterate every character
    40	    # new_text = []
    41	    # for char in text:
    42	    #     if char in 'aeiou':
    43	    #         new_text.append(vowel)
    44	    #     elif char in 'AEIOU':
    45	    #         new_text.append(vowel.upper())
    46	    #     else:
    47	    #         new_text.append(char)
    48	    # text = ''.join(new_text)
    49	
    50	    # Method 2: str.replace
    51	    # for v in 'aeiou':
    52	    #     text = text.replace(v, vowel).replace(v.upper(), vowel.upper())
    53	
    54	    # Method 3: Use a list comprehension
    55	    # new_text = [
    56	    #     vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
    57	    #     for c in text
    58	    # ]
    59	    # text = ''.join(new_text)
    60	
    61	    # Method 4: Define a function, use list comprehension
    62	    def new_char(c):
    63	        return vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c
    64	
    65	    # text = ''.join([new_char(c) for c in text])
    66	
    67	    # Method 5: Use a `map` to iterate with a `lambda`
    68	    # text = ''.join(
    69	    #     map(
    70	    #         lambda c: vowel if c in 'aeiou' else vowel.upper()
    71	    #         if c in 'AEIOU' else c, text))
    72	
    73	    # Method 6: `map` with the function
    74	    text = ''.join(map(new_char, text))
    75	
    76	    # Method 7: Regular expressions
    77	    # text = re.sub('[aeiou]', vowel, text)
    78	    # text = re.sub('[AEIOU]', vowel.upper(), text)
    79	
    80	    print(text.rstrip())
    81	
    82	
    83	# --------------------------------------------------
    84	if __name__ == '__main__':
    85	    main()
````

\pagebreak

# Chapter 6

# Gashlycrumb

Write a Python program called `gashlycrumb.py` that takes a letter of the alphabet as an argument and looks up the line in a `-f|--file` argument (default `gashlycrumb.txt`) and prints the line starting with that letter.

````
$ ./gashlycrumb.py
usage: gashlycrumb.py [-h] [-f str] str
gashlycrumb.py: error: the following arguments are required: str
$ ./gashlycrumb.py -h
usage: gashlycrumb.py [-h] [-f str] str

Gashlycrumb

positional arguments:
  str                 Letter

optional arguments:
  -h, --help          show this help message and exit
  -f str, --file str  Input file (default: gashlycrumb.txt)
$ ./gashlycrumb.py 3
I do not know "3".
$ ./gashlycrumb.py CH
"CH" is not 1 character.
$ ./gashlycrumb.py a
A is for Amy who fell down the stairs.
$ ./gashlycrumb.py z
Z is for Zillah who drank too much gin.
````

If you are not familiar with the work of Edward Gorey, please stop and go read about him immediately, e.g. https://www.brainpickings.org/2011/01/19/edward-gorey-the-gashlycrumb-tinies/! 

Write your own version of Gorey's text and pass in your version as the `--file`.

Write an interactive version that takes input directly from the user:

````
$ ./gashlycrumb_i.py
Please provide a letter [! to quit]: a
A is for Amy who fell down the stairs.
Please provide a letter [! to quit]: b
B is for Basil assaulted by bears.
Please provide a letter [! to quit]: !
Bye
````

\pagebreak

# gashlycrumb Solution

````
     1	#!/usr/bin/env python3
     2	"""Lookup tables"""
     3	
     4	import argparse
     5	import os
     6	from dire import die
     7	
     8	
     9	# --------------------------------------------------
    10	def get_args():
    11	    """get command-line arguments"""
    12	    parser = argparse.ArgumentParser(
    13	        description='Gashlycrumb',
    14	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    15	
    16	    parser.add_argument('letter', help='Letter', metavar='str', type=str)
    17	
    18	    parser.add_argument('-f',
    19	                        '--file',
    20	                        help='Input file',
    21	                        metavar='str',
    22	                        type=str,
    23	                        default='gashlycrumb.txt')
    24	
    25	    return parser.parse_args()
    26	
    27	
    28	# --------------------------------------------------
    29	def main():
    30	    """Make a jazz noise here"""
    31	    args = get_args()
    32	    letter = args.letter.upper()
    33	    file = args.file
    34	
    35	    if not os.path.isfile(file):
    36	        die('--file "{}" is not a file.'.format(file))
    37	
    38	    if len(letter) != 1:
    39	        die('"{}" is not 1 character.'.format(letter))
    40	
    41	    lookup = {}
    42	    for line in open(file):
    43	        lookup[line[0]] = line.rstrip()
    44	
    45	    if letter in lookup:
    46	        print(lookup[letter])
    47	    else:
    48	        print('I do not know "{}".'.format(letter))
    49	
    50	
    51	# --------------------------------------------------
    52	if __name__ == '__main__':
    53	    main()
````

\pagebreak

# Chapter 7

# Movie Reader

Write a Python program called `movie_reader.py` that takes a single positional argument that is a bit of text or the name of an input file. The output will be dynamic, so I cannot write a test for how the program should behave, nor can I include a bit of text that shows you how it should work. Your program should print the input text character-by-character and then pause .5 seconds for ending punctuation like `.`, `!` or `?`, .2 seconds for a pause like `,` `:`, or `;`, and .05 seconds for anything else.

````
$ ./movie_reader.py
usage: movie_reader.py [-h] str
movie_reader.py: error: the following arguments are required: str
$ ./movie_reader.py -h
usage: movie_reader.py [-h] str

Movie Reader

positional arguments:
  str         Input text or file

optional arguments:
  -h, --help  show this help message and exit
$ ./movie_reader.py 'Foo, bar!'
Foo, bar!
$ ./movie_reader.py ../inputs/fox.txt
The quick brown fox jumps over the lazy dog.
````

\pagebreak

# movie_reader Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import os
     5	import sys
     6	import time
     7	
     8	
     9	# --------------------------------------------------
    10	def get_args():
    11	    """Get command-line arguments"""
    12	
    13	    parser = argparse.ArgumentParser(
    14	        description='Movie Reader',
    15	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    16	
    17	    parser.add_argument('text', metavar='str', help='Input text or file')
    18	
    19	    return parser.parse_args()
    20	
    21	
    22	# --------------------------------------------------
    23	def main():
    24	    """Make a jazz noise here"""
    25	
    26	    args = get_args()
    27	    text = args.text
    28	
    29	    if os.path.isfile(text):
    30	        text = open(text).read()
    31	
    32	    for line in text.splitlines():
    33	        for char in line:
    34	            print(char, end='')
    35	            time.sleep(.5 if char in '.!?\n' else .2 if char in ',:;' else .05)
    36	            sys.stdout.flush()
    37	
    38	        print()
    39	
    40	
    41	# --------------------------------------------------
    42	if __name__ == '__main__':
    43	    main()
````

\pagebreak

# Chapter 8

# Palindromes

Write a Python program called `palindromic.py` that will find words that are palindromes in positional argument which is either a string or a file name.

````
$ ./palindromic.py
usage: palindromic.py [-h] [-m int] str
palindromic.py: error: the following arguments are required: str
$ ./palindromic.py -h
usage: palindromic.py [-h] [-m int] str

Find palindromes in text

positional arguments:
  str                Input text or file

optional arguments:
  -h, --help         show this help message and exit
  -m int, --min int  Minimum word length (default: 3)
$ ./palindromic.py '"Wow!" said Mom.'
wow
mom
$ ./palindromic.py input.txt
anna
civic
kayak
madam
mom
wow
level
noon
racecar
radar
redder
refer
rotator
rotor
solos
stats
tenet
````

\pagebreak

# palindromes Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import os
     5	import re
     6	
     7	
     8	# --------------------------------------------------
     9	def get_args():
    10	    """Get command-line arguments"""
    11	
    12	    parser = argparse.ArgumentParser(
    13	        description='Find palindromes in text',
    14	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    15	
    16	    parser.add_argument('text', metavar='str', help='Input text or file')
    17	
    18	    parser.add_argument('-m',
    19	                        '--min',
    20	                        metavar='int',
    21	                        type=int,
    22	                        help='Minimum word length',
    23	                        default=3)
    24	
    25	    return parser.parse_args()
    26	
    27	
    28	# --------------------------------------------------
    29	def main():
    30	    """Make a jazz noise here"""
    31	
    32	    args = get_args()
    33	    text = args.text
    34	    min_length = args.min
    35	
    36	    if os.path.isfile(text):
    37	        text = open(text).read()
    38	
    39	    for line in text.splitlines():
    40	        for word in re.split(r'(\W+)', line.lower()):
    41	            if len(word) >= min_length:
    42	                rev = ''.join(reversed(word))
    43	                if rev == word:
    44	                    print(word)
    45	
    46	
    47	# --------------------------------------------------
    48	if __name__ == '__main__':
    49	    main()
````

\pagebreak

# Chapter 9

# Ransom

Create a Python program called `ransom.py` that will randomly capitalize the letters in a given word or phrase. The input text may also name a file in which case the text should come from the file. The program should take a `-s|--seed` argument for the `random.seed` to control randomness for the test suite. It should also respond to `-h|--help` for usage.

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

\pagebreak

# ransom_note Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import os
     5	import random
     6	import sys
     7	
     8	
     9	# --------------------------------------------------
    10	def get_args():
    11	    """get command-line arguments"""
    12	    parser = argparse.ArgumentParser(
    13	        description='Ransom Note',
    14	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    15	
    16	    parser.add_argument('text', metavar='str', help='Input text or file')
    17	
    18	    parser.add_argument('-s',
    19	                        '--seed',
    20	                        help='Random seed',
    21	                        metavar='int',
    22	                        type=int,
    23	                        default=None)
    24	
    25	    return parser.parse_args()
    26	
    27	
    28	# --------------------------------------------------
    29	def main():
    30	    """Make a jazz noise here"""
    31	    args = get_args()
    32	
    33	    random.seed(args.seed)
    34	
    35	    text = args.text
    36	    if os.path.isfile(text):
    37	        text = open(text).read()
    38	
    39	    #ransom = []
    40	    #for char in text:
    41	    #    ransom.append(char.upper() if random.choice([0, 1]) else char.lower())
    42	
    43	    #ransom = [c.upper() if random.choice([0, 1]) else c.lower() for c in text]
    44	
    45	    #ransom = map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(),
    46	    #             text)
    47	
    48	    f = lambda c: c.upper() if random.choice([0, 1]) else c.lower()
    49	    ransom = map(f, text)
    50	
    51	    print(''.join(ransom))
    52	
    53	
    54	# --------------------------------------------------
    55	if __name__ == '__main__':
    56	    main()
````

\pagebreak

# Chapter 10

# Simple Rhymer

Write a Python program called `rhymer.py` that will create new words by removing the consonant(s) from the beginning of the word and then creating new words by prefixing the remainder with all the consonants and clusters that were not at the beginning. That is, prefix with all the consonants in the alphabet plus these clusters:

    bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp 
    st sw th tr tw wh wr sch scr shr sph spl spr squ str thr

````
$ ./rhymer.py
usage: rhymer.py [-h] str
rhymer.py: error: the following arguments are required: str
$ ./rhymer.py -h
usage: rhymer.py [-h] str

Make rhyming "words"

positional arguments:
  str         A word

optional arguments:
  -h, --help  show this help message and exit
$ ./rhymer.py apple
Word "apple" must start with consonants  
$ ./rhymer.py take | head
bake
cake
dake
fake
gake
hake
jake
kake
lake
make
````

\pagebreak

# rhymer Solution

````
     1	#!/usr/bin/env python3
     2	"""Make rhyming words"""
     3	
     4	import argparse
     5	import re
     6	import string
     7	import sys
     8	from dire import die
     9	
    10	
    11	# --------------------------------------------------
    12	def get_args():
    13	    """get command-line arguments"""
    14	    parser = argparse.ArgumentParser(
    15	        description='Make rhyming "words"',
    16	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    17	
    18	    parser.add_argument('word', metavar='str', help='A word')
    19	
    20	    return parser.parse_args()
    21	
    22	
    23	# --------------------------------------------------
    24	def main():
    25	    """Make a jazz noise here"""
    26	    args = get_args()
    27	    word = args.word
    28	
    29	    vowels = 'aeiou'
    30	    if word[0] in vowels:
    31	        die('Word "{}" must start with consonants'.format(word))
    32	
    33	    consonants = [c for c in string.ascii_lowercase if c not in 'aeiou']
    34	    match = re.match('^([' + ''.join(consonants) + ']+)(.+)', word)
    35	
    36	    clusters = ('bl br ch cl cr dr fl fr gl gr pl pr sc '
    37	                'sh sk sl sm sn sp st sw th tr tw wh wr '
    38	                'sch scr shr sph spl spr squ str thr').split()
    39	
    40	    if match:
    41	        start, rest = match.group(1), match.group(2)
    42	        for c in filter(lambda c: c != start, consonants + clusters):
    43	            print(c + rest)
    44	
    45	
    46	# --------------------------------------------------
    47	if __name__ == '__main__':
    48	    main()
````

\pagebreak

# Chapter 11

# Rock, Paper, Scissors

Write a Python program called `rps.py` that will play the ever-popular "Rock, Paper, Scissors" game. As often as possible, insult the player by combining an adjective and a noun from the following lists:

Adjectives =
truculent fatuous vainglorious fatuous petulant moribund jejune
feckless antiquated rambunctious mundane misshapen glib dreary
dopey devoid deleterious degrading clammy brazen indiscreet
indecorous imbecilic dysfunctional dubious drunken disreputable
dismal dim deficient deceitful damned daft contrary churlish
catty banal asinine infantile lurid morbid repugnant unkempt
vapid decrepit malevolent impertinent decrepit grotesque puerile

Nouns =
abydocomist bedswerver bespawler bobolyne cumberworld dalcop
dew-beater dorbel drate-poke driggle-draggle fopdoodle fustylugs
fustilarian gillie-wet-foot gnashgab gobermouch
gowpenful-o’-anything klazomaniac leasing-monger loiter-sack
lubberwort muck-spout mumblecrust quisby raggabrash rakefire
roiderbanks saddle-goose scobberlotcher skelpie-limmer
smell-feast smellfungus snoutband sorner stampcrab stymphalist
tallowcatch triptaker wandought whiffle-whaffle yaldson zoilist

The program should accept a `-s|--seed` to pass to `random`.

````
$ ./rps.py
1-2-3-Go! [rps|q] r
You: Rock
Me : Scissors
You win. You are a clammy drate-poke.
1-2-3-Go! [rps|q] t
You dysfunctional dew-beater! Please choose from: p, r, s.
1-2-3-Go! [rps|q] p
You: Paper
Me : Rock
You win. You are a dismal gillie-wet-foot.
1-2-3-Go! [rps|q] q
Bye, you imbecilic fopdoodle!
````

\pagebreak

# rock_paper_scissors Solution

````
     1	#!/usr/bin/env python3
     2	"""Rock, Paper, Scissors"""
     3	
     4	import argparse
     5	import os
     6	import random
     7	import sys
     8	
     9	
    10	# --------------------------------------------------
    11	def get_args():
    12	    """Get command-line arguments"""
    13	
    14	    parser = argparse.ArgumentParser(
    15	        description='Rock, Paper, Scissors',
    16	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    17	
    18	    parser.add_argument('-s',
    19	                        '--seed',
    20	                        help='Random seed',
    21	                        metavar='int',
    22	                        type=int,
    23	                        default=None)
    24	
    25	    return parser.parse_args()
    26	
    27	
    28	# --------------------------------------------------
    29	def insult():
    30	    adjective = """
    31	    truculent fatuous vainglorious fatuous petulant moribund jejune
    32	    feckless antiquated rambunctious mundane misshapen glib dreary
    33	    dopey devoid deleterious degrading clammy brazen indiscreet
    34	    indecorous imbecilic dysfunctional dubious drunken disreputable
    35	    dismal dim deficient deceitful damned daft contrary churlish
    36	    catty banal asinine infantile lurid morbid repugnant unkempt
    37	    vapid decrepit malevolent impertinent decrepit grotesque puerile
    38	    """.split()
    39	
    40	    noun = """
    41	    abydocomist bedswerver bespawler bobolyne cumberworld dalcop
    42	    dew-beater dorbel drate-poke driggle-draggle fopdoodle fustylugs
    43	    fustilarian gillie-wet-foot gnashgab gobermouch
    44	    gowpenful-o’-anything klazomaniac leasing-monger loiter-sack
    45	    lubberwort muck-spout mumblecrust quisby raggabrash rakefire
    46	    roiderbanks saddle-goose scobberlotcher skelpie-limmer
    47	    smell-feast smellfungus snoutband sorner stampcrab stymphalist
    48	    tallowcatch triptaker wandought whiffle-whaffle yaldson zoilist
    49	    """.split()
    50	
    51	    return ' '.join([random.choice(adjective), random.choice(noun)])
    52	
    53	
    54	# --------------------------------------------------
    55	def main():
    56	    """Make a jazz noise here"""
    57	
    58	    args = get_args()
    59	    random.seed(args.seed)
    60	
    61	    valid = set('rps')
    62	    beats = {'r': 's', 's': 'p', 'p': 'r'}
    63	    display = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    64	
    65	    while True:
    66	        play = input('1-2-3-Go! [rps|q] ').lower()
    67	
    68	        if play.startswith('q'):
    69	            print('Bye, you {}!'.format(insult()))
    70	            sys.exit(0)
    71	
    72	        if play not in valid:
    73	            print('You {}! Please choose from: {}.'.format(
    74	                insult(), ', '.join(sorted(valid))))
    75	            continue
    76	
    77	        computer = random.choice(list(valid))
    78	
    79	        print('You: {}\nMe : {}'.format(display[play], display[computer]))
    80	
    81	        if beats[play] == computer:
    82	            print('You win. You are a {}.'.format(insult()))
    83	        elif beats[computer] == play:
    84	            print('You lose, {}!'.format(insult()))
    85	        else:
    86	            print('Draw, you {}.'.format(insult()))
    87	
    88	
    89	# --------------------------------------------------
    90	if __name__ == '__main__':
    91	    main()
````

\pagebreak

# Chapter 12

# Abuse

Write a Python program called `abuse.py` that generates some `-n|--number` of insults (default 3) by randomly combining some number of `-a|--adjectives` (default 2) with a noun (see below). Be sure your program accepts a `-s|--seed` argument to pass to `random.seed`.

Adjectives:

bankrupt base caterwauling corrupt cullionly detestable dishonest
false filthsome filthy foolish foul gross heedless indistinguishable
infected insatiate irksome lascivious lecherous loathsome lubbery old
peevish rascaly rotten ruinous scurilous scurvy slanderous
sodden-witted thin-faced toad-spotted unmannered vile wall-eyed

Nouns:

nouns = """
Judas Satan ape ass barbermonger beggar block boy braggart butt
carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
gull harpy jack jolthead knave liar lunatic maw milksop minion
ratcatcher recreant rogue scold slave swine traitor varlet villain worm

````
$ ./abuse.py -h
usage: abuse.py [-h] [-a int] [-n int] [-s int]

Argparse Python script

optional arguments:
  -h, --help            show this help message and exit
  -a int, --adjectives int
                        Number of adjectives (default: 2)
  -n int, --number int  Number of insults (default: 3)
  -s int, --seed int    Random seed (default: None)
$ ./abuse.py
You slanderous, rotten block!
You lubbery, scurilous ratcatcher!
You rotten, foul liar!
$ ./abuse.py -s 1 -n 2 -a 1
You rotten rogue!
You lascivious ape!
$ ./abuse.py -s 2 -n 4 -a 4
You scurilous, foolish, vile, foul milksop!
You cullionly, lubbery, heedless, filthy lunatic!
You foul, lecherous, infected, slanderous degenerate!
You base, ruinous, slanderous, false liar!
````

# Skills

* Setting random seed from argument
* Random selecting/sampling from a list
* Iterating through a loop a defined number of times
* Formatting string output

\pagebreak

# abuse Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import random
     5	import sys
     6	
     7	adjectives = """
     8	bankrupt base caterwauling corrupt cullionly detestable dishonest
     9	false filthsome filthy foolish foul gross heedless indistinguishable
    10	infected insatiate irksome lascivious lecherous loathsome lubbery old
    11	peevish rascaly rotten ruinous scurilous scurvy slanderous
    12	sodden-witted thin-faced toad-spotted unmannered vile wall-eyed
    13	""".strip().split()
    14	
    15	nouns = """
    16	Judas Satan ape ass barbermonger beggar block boy braggart butt
    17	carbuncle coward coxcomb cur dandy degenerate fiend fishmonger fool
    18	gull harpy jack jolthead knave liar lunatic maw milksop minion
    19	ratcatcher recreant rogue scold slave swine traitor varlet villain worm
    20	""".strip().split()
    21	
    22	
    23	# --------------------------------------------------
    24	def get_args():
    25	    """get command-line arguments"""
    26	    parser = argparse.ArgumentParser(
    27	        description='Argparse Python script',
    28	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    29	
    30	    parser.add_argument('-a',
    31	                        '--adjectives',
    32	                        help='Number of adjectives',
    33	                        metavar='int',
    34	                        type=int,
    35	                        default=2)
    36	
    37	    parser.add_argument('-n',
    38	                        '--number',
    39	                        help='Number of insults',
    40	                        metavar='int',
    41	                        type=int,
    42	                        default=3)
    43	
    44	    parser.add_argument('-s',
    45	                        '--seed',
    46	                        help='Random seed',
    47	                        metavar='int',
    48	                        type=int,
    49	                        default=None)
    50	
    51	    return parser.parse_args()
    52	
    53	
    54	# --------------------------------------------------
    55	def main():
    56	    """Make a jazz noise here"""
    57	    args = get_args()
    58	    num_adj = args.adjectives
    59	    num_insults = args.number
    60	
    61	    random.seed(args.seed)
    62	
    63	    for _ in range(num_insults):
    64	        adjs = random.sample(adjectives, k=num_adj)
    65	        noun = random.choice(nouns)
    66	        print('You {} {}!'.format(', '.join(adjs), noun))
    67	
    68	
    69	# --------------------------------------------------
    70	if __name__ == '__main__':
    71	    main()
````

\pagebreak

# Chapter 13

# BACRONYM

Write a Python program called `bacronym.py` that takes an string like "FBI" and retrofits some `-n|--number` (default 5) of acronyms by reading a `-w|--wordlist` argument (defualt "/usr/share/dict/words"), skipping over words to `-e|--exclude` (default "a, an, the") and randomly selecting words that start with each of the letters. Be sure to include a `-s|--seed` argument (default `None`) to pass to `random.seed` for the test suite.

````
$ ./bacronym.py
usage: bacronym.py [-h] [-n NUM] [-w STR] [-x STR] [-s INT] STR
bacronym.py: error: the following arguments are required: STR
$ ./bacronym.py -h
usage: bacronym.py [-h] [-n NUM] [-w STR] [-x STR] [-s INT] STR

Explain acronyms

positional arguments:
  STR                   Acronym

optional arguments:
  -h, --help            show this help message and exit
  -n NUM, --num NUM     Maximum number of definitions (default: 5)
  -w STR, --wordlist STR
                        Dictionary/word file (default: /usr/share/dict/words)
  -x STR, --exclude STR
                        List of words to exclude (default: a,an,the)
  -s INT, --seed INT    Random seed (default: None)
$ ./bacronym.py FBI -s 1
FBI =
 - Fecundity Brokage Imitant
 - Figureless Basketmaking Ismailite
 - Frumpery Bonedog Irregardless
 - Foxily Blastomyces Inedited
 - Fastland Bouncingly Idiospasm
````

# Skills

* Using `argparse`
* Reading words from a file into a list
* Randomly selecting words from a list
* Formatting string output

\pagebreak

# bacronym Solution

````
     1	#!/usr/bin/env python3
     2	"""Make guesses about acronyms"""
     3	
     4	import argparse
     5	import sys
     6	import os
     7	import random
     8	import re
     9	from collections import defaultdict
    10	
    11	
    12	# --------------------------------------------------
    13	def get_args():
    14	    """get arguments"""
    15	    parser = argparse.ArgumentParser(
    16	        description='Explain acronyms',
    17	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    18	
    19	    parser.add_argument('acronym', help='Acronym', type=str, metavar='STR')
    20	
    21	    parser.add_argument('-n',
    22	                        '--num',
    23	                        help='Maximum number of definitions',
    24	                        type=int,
    25	                        metavar='NUM',
    26	                        default=5)
    27	
    28	    parser.add_argument('-w',
    29	                        '--wordlist',
    30	                        help='Dictionary/word file',
    31	                        type=str,
    32	                        metavar='STR',
    33	                        default='/usr/share/dict/words')
    34	
    35	    parser.add_argument('-x',
    36	                        '--exclude',
    37	                        help='List of words to exclude',
    38	                        type=str,
    39	                        metavar='STR',
    40	                        default='a,an,the')
    41	
    42	    parser.add_argument('-s',
    43	                        '--seed',
    44	                        help='Random seed',
    45	                        type=int,
    46	                        metavar='INT',
    47	                        default=None)
    48	
    49	    return parser.parse_args()
    50	
    51	
    52	# --------------------------------------------------
    53	def main():
    54	    """main"""
    55	
    56	    args = get_args()
    57	    acronym = args.acronym
    58	    wordlist = args.wordlist
    59	    limit = args.num
    60	    goodword = r'^[a-z]{2,}$'
    61	    badwords = set(re.split(r'\s*,\s*', args.exclude.lower()))
    62	
    63	    random.seed(args.seed)
    64	
    65	    if not re.match(goodword, acronym.lower()):
    66	        print('"{}" must be >1 in length, only use letters'.format(acronym))
    67	        sys.exit(1)
    68	
    69	    if not os.path.isfile(wordlist):
    70	        print('"{}" is not a file.'.format(wordlist))
    71	        sys.exit(1)
    72	
    73	    seen = set()
    74	    words_by_letter = defaultdict(list)
    75	    for word in open(wordlist).read().lower().split():
    76	        clean = re.sub('[^a-z]', '', word)
    77	        if not clean:  # nothing left?
    78	            continue
    79	
    80	        if re.match(goodword,
    81	                    clean) and clean not in seen and clean not in badwords:
    82	            seen.add(clean)
    83	            words_by_letter[clean[0]].append(clean)
    84	
    85	    len_acronym = len(acronym)
    86	    definitions = []
    87	    for i in range(0, limit):
    88	        definition = []
    89	        for letter in acronym.lower():
    90	            possible = words_by_letter.get(letter, [])
    91	            if len(possible) > 0:
    92	                definition.append(
    93	                    random.choice(possible).title() if possible else '?')
    94	
    95	        if len(definition) == len_acronym:
    96	            definitions.append(' '.join(definition))
    97	
    98	    if len(definitions) > 0:
    99	        print(acronym.upper() + ' =')
   100	        for definition in definitions:
   101	            print(' - ' + definition)
   102	    else:
   103	        print('Sorry I could not find any good definitions')
   104	
   105	
   106	# --------------------------------------------------
   107	if __name__ == '__main__':
   108	    main()
````

\pagebreak

# Chapter 14

# Blackjack 

Write a Python program called `blackjack.py` that plays an abbreviated game of Blackjack. You will need to `import random` to get random cards from a deck you will construct, and so your program will need to accept a `-s|--seed` that will set `random.seed()` with the value that is passed in so that the test suite will work. The other arguments you will accept are two flags (Boolean values) of `-p|--player_hits` and `-d|--dealer_hits`. As usual, you will also have a `-h|--help` option for usage statement.

To play the game, the user will run the program and will see a display of what cards the dealer has (noted "D") and what cards the player has (noted "P") along with a sum of the values of the cards. In Blackjack, number cards are worth their value, face cards are worth 10, and the Ace will be worth 1 for our game (though in the real game it can alternate between 1 and 11).

To create your deck of cards, you will need to use the Unicode symbols for the suites ( ♥ ♠ ♣ ♦ ) [which won't display in the PDF, so consult the Markdown file].

Combine these with the numbers 2-10 and the letters "A", "J", "Q," and "K" (hint: look at `itertools.product`). Because your game will use randomness, you will need to sort your deck and then use the `random.shuffle` method so that your cards will be in the correct order to pass the tests.

When you make the initial deal, keep in mind how cards are actually dealt -- first one card to each of the players, then one to the dealer, then the players, then the dealer, etc. You might be tempted to use `random.choice` or something like that to select your cards, but you need to keep in mind that you are modeling an actual deck and so selected cards should no longer be present in the deck. If the `-p|--player_htis` flag is present, deal an additional card to the player; likewise with the `-d|--dealer_hits` flag.

After displaying the hands, the code should:

1. Check if the player has more than 21; if so, print 'Player busts! You lose, loser!' and exit(0)
2. Check if the dealer has more than 21; if so, print 'Dealer busts.' and exit(0)
3. Check if the player has exactly 21; if so, print 'Player wins. You probably cheated.' and exit(0)
4. Check if the dealer has exactly 21; if so, print 'Dealer wins!' and exit(0)
5. If the either the dealer or the player has less than 18, you should indicate "X should hit."

NB: Look at the Markdown format to see the actual output as the suites won't display in the PDF version!

````
$ ./blackjack.py
D [11]: ♠J ♥A
P [18]: ♦8 ♠10
Dealer should hit.
$ ./blackjack.py
D [13]: ♥3 ♦J
P [16]: ♥6 ♦10
Dealer should hit.
Player should hit.
$ ./blackjack.py -s 5
D [ 5]: ♣4 ♣A
P [19]: ♦10 ♦9
Dealer should hit.
$ ./blackjack.py -s 3 -p
D [19]: ♥K ♠9
P [22]: ♣3 ♥9 ♣J
Player busts! You lose, loser!
$ ./blackjack.py -s 15 -p
D [19]: ♠10 ♦9
P [21]: ♣10 ♥8 ♠3
Player wins. You probably cheated.
````

\pagebreak

# blackjack Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import random
     5	import re
     6	import sys
     7	from itertools import product
     8	from dire import die
     9	
    10	
    11	# --------------------------------------------------
    12	def get_args():
    13	    """get command-line arguments"""
    14	    parser = argparse.ArgumentParser(
    15	        description='Argparse Python script',
    16	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    17	
    18	    parser.add_argument(
    19	        '-s',
    20	        '--seed',
    21	        help='Random seed',
    22	        metavar='int',
    23	        type=int,
    24	        default=None)
    25	
    26	    parser.add_argument(
    27	        '-d',
    28	        '--dealer_hits',
    29	        help='Dealer hits',
    30	        action='store_true')
    31	
    32	    parser.add_argument(
    33	        '-p',
    34	        '--player_hits',
    35	        help='Player hits',
    36	        action='store_true')
    37	
    38	    return parser.parse_args()
    39	
    40	
    41	# --------------------------------------------------
    42	def bail(msg):
    43	    """print() and exit(0)"""
    44	    print(msg)
    45	    sys.exit(0)
    46	
    47	# --------------------------------------------------
    48	def card_value(card):
    49	    """card to numeric value"""
    50	    val = card[1:]
    51	    faces = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}
    52	    if val.isdigit():
    53	        return int(val)
    54	    elif val in faces:
    55	        return faces[val]
    56	    else:
    57	        die('Unknown card value for "{}"'.format(card))
    58	
    59	
    60	# --------------------------------------------------
    61	def main():
    62	    """Make a jazz noise here"""
    63	    args = get_args()
    64	
    65	    random.seed(args.seed)
    66	
    67	    # seed = args.seed
    68	    # if seed is not None:
    69	    #     random.seed(seed)
    70	
    71	    suites = list('♥♠♣♦')
    72	    values = list(range(2, 11)) + list('AJQK')
    73	    cards = sorted(map(lambda t: '{}{}'.format(*t), product(suites, values)))
    74	    random.shuffle(cards)
    75	
    76	    p1, d1, p2, d2 = cards.pop(), cards.pop(), cards.pop(), cards.pop()
    77	    player = [p1, p2]
    78	    dealer = [d1, d2]
    79	
    80	    if args.player_hits:
    81	        player.append(cards.pop())
    82	
    83	    if args.dealer_hits:
    84	        dealer.append(cards.pop())
    85	
    86	    player_hand = sum(map(card_value, player))
    87	    dealer_hand = sum(map(card_value, dealer))
    88	
    89	    print('D [{:2}]: {}'.format(dealer_hand, ' '.join(dealer)))
    90	    print('P [{:2}]: {}'.format(player_hand, ' '.join(player)))
    91	
    92	    if player_hand > 21:
    93	        bail('Player busts! You lose, loser!')
    94	    elif dealer_hand > 21:
    95	        bail('Dealer busts.')
    96	    elif player_hand == 21:
    97	        bail('Player wins. You probably cheated.')
    98	    elif dealer_hand == 21:
    99	        bail('Dealer wins!')
   100	
   101	    if dealer_hand < 18:
   102	        print('Dealer should hit.')
   103	
   104	    if player_hand < 18:
   105	        print('Player should hit.')
   106	
   107	
   108	# --------------------------------------------------
   109	if __name__ == '__main__':
   110	    main()
````

\pagebreak

# Chapter 15

# Family Tree

Write a program called `tree.py` that will take an input file as a single positional argument and produce a graph of the family tree described therein. The file can have only three kinds of statements:

1. `INITIALS = Full Name`
2. `person1 married person2`
3. `person1 and person2 begat child1[, child2...]`

Use the `graphviz` module to generate a graph like the `kyc.gv.pdf` included here that was generated from the following input:

````
$ cat tudor.txt
H7 = Henry VII
EOY = Elizabeth of York
H8 = Henry VIII
COA = Catherine of Aragon
AB = Anne Boleyn
JS = Jane Seymour
AOC = Anne of Cleves
CH = Catherine Howard
CP = Catherine Parr
HDC = Henry, Duke of Cornwall
M1 = Mary I
E1 = Elizabeth I
E6 = Edward VI

H7 married EOY
H7 and EOY begat H8
H8 married COA
H8 married AB
H8 married JS
H8 married AOC
H8 married CH
H8 married CP
H8 and COA begat HDC, M1
H8 and AB begat E1
H8 and JS begat E6
$ ./tree.py tudor.txt
Done, see output in "tudor.txt.gv".
````

\pagebreak

# family_tree Solution

````
     1	#!/usr/bin/env python3
     2	"""
     3	Author : kyclark
     4	Date   : 2019-05-24
     5	Purpose: Display a family tree
     6	"""
     7	
     8	import argparse
     9	import os
    10	import re
    11	import sys
    12	from graphviz import Digraph
    13	
    14	
    15	# --------------------------------------------------
    16	def get_args():
    17	    """Get command-line arguments"""
    18	
    19	    parser = argparse.ArgumentParser(
    20	        description='Display a family tree',
    21	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    22	
    23	    parser.add_argument('file',
    24	                        metavar='FILE',
    25	                        type=argparse.FileType('r'),
    26	                        help='File input')
    27	
    28	    parser.add_argument('-o',
    29	                        '--outfile',
    30	                        help='Output filename',
    31	                        metavar='str',
    32	                        type=str,
    33	                        default='')
    34	
    35	    return parser.parse_args()
    36	
    37	
    38	# --------------------------------------------------
    39	def main():
    40	    """Make a jazz noise here"""
    41	
    42	    args = get_args()
    43	    fh = args.file
    44	    out_file = args.outfile or os.path.basename(fh.name) + '.gv'
    45	
    46	    nodes, edges = parse_tree(fh)
    47	    dot = Digraph(comment='Tree')
    48	    for initials, name in nodes.items():
    49	        dot.node(name)
    50	
    51	    for n1, n2 in edges:
    52	        if n1 in nodes:
    53	            n1 = nodes[n1]
    54	        if n2 in nodes:
    55	            n2 = nodes[n2]
    56	
    57	        dot.edge(n1, n2)
    58	
    59	    dot.render(out_file, view=True)
    60	
    61	    print('Done, see output in "{}".'.format(out_file))
    62	
    63	# --------------------------------------------------
    64	def parse_tree(fh):
    65	    """parse input file"""
    66	
    67	    ini_patt = '([A-Za-z0-9]+)'
    68	    name_patt = ini_patt + '\s*=\s*(.+)'
    69	    begat_patt = ini_patt + '\s+and\s+' + ini_patt + '\s+begat\s+(.+)'
    70	    married_patt = ini_patt + '\s+married\s+' + ini_patt
    71	    edges = set()
    72	    nodes = {}
    73	
    74	    for line in fh:
    75	        name_match = re.match(name_patt, line)
    76	        begat_match = re.match(begat_patt, line)
    77	        married_match = re.match(married_patt, line)
    78	
    79	        if name_match:
    80	            initials, name = name_match.groups()
    81	            nodes[initials] = name
    82	        elif married_match:
    83	            p1, p2 = married_match.groups()
    84	            edges.add((p1, p2))
    85	        elif begat_match:
    86	            p1, p2, begat = begat_match.groups()
    87	            children = re.split('\s*,\s*', begat)
    88	            for parent in p1, p2:
    89	                for child in children:
    90	                    edges.add((parent, child))
    91	
    92	    return nodes, edges
    93	
    94	
    95	# --------------------------------------------------
    96	if __name__ == '__main__':
    97	    main()
````

\pagebreak

# Chapter 16

# Gematria

Write a Python program called `gematria.py` 

Gematria is a system for assigning a number to a word by summing the numeric values of each of the letters as defined by the Mispar godol (https://en.wikipedia.org/wiki/Gematria). For English characters, we can use the ASCII table (https://en.wikipedia.org/wiki/ASCII). It is not necessary, however, to encode this table in our program as Python provides the `ord` function to convert a character to its "ordinal" (order in the ASCII table) value as well as the `chr` function to convert a number to its "character."


````
>>> ord('A')
65
>>> ord('a')
97
>>> chr(88)
'X'
>>> chr(112)
'p'
````

To implement an ASCII version of gematria in Python, we need to turn each letter into a number and add them all together.  So, to start, note that Python can use a `for` loop to cycle through all the members of a list (in order):


````
>>> for char in ['p', 'y', 't', 'h', 'o', 'n']:
...     print(ord(char))
...
112
121
116
104
111
110
````

Now you just need to `sum` those up for each word!

````
$ ./gematria.py
usage: gematria.py [-h] str
gematria.py: error: the following arguments are required: str
$ ./gematria.py -h
usage: gematria.py [-h] str

Gematria

positional arguments:
  str         Input text or file

optional arguments:
  -h, --help  show this help message and exit
$ ./gematria.py 'foo bar baz'
324 309 317
$ ./gematria.py ../inputs/fox.txt
289 541 552 333 559 444 321 448 314
````

\pagebreak

# gematria Solution

````
     1	#!/usr/bin/env python3
     2	"""Gematria"""
     3	
     4	import argparse
     5	import os
     6	import re
     7	import sys
     8	
     9	
    10	# --------------------------------------------------
    11	def get_args():
    12	    """Get command-line arguments"""
    13	
    14	    parser = argparse.ArgumentParser(
    15	        description='Gematria',
    16	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    17	
    18	    parser.add_argument('text', metavar='str', help='Input text or file')
    19	
    20	    return parser.parse_args()
    21	
    22	
    23	# --------------------------------------------------
    24	def main():
    25	    """Make a jazz noise here"""
    26	
    27	    args = get_args()
    28	    text = args.text
    29	
    30	    if os.path.isfile(text):
    31	        text = open(text).read()
    32	
    33	    def clean(word):
    34	        return re.sub('[^a-zA-Z0-9]', '', word)
    35	
    36	    for line in text.splitlines():
    37	        words = line.rstrip().split()
    38	        nums = map(lambda word: str(sum(map(ord, clean(word)))), words)
    39	        print(' '.join(nums))
    40	
    41	
    42	# --------------------------------------------------
    43	if __name__ == '__main__':
    44	    main()
````

\pagebreak

# Chapter 17

# Guessing Game

Write a Python program called `guess.py` that plays a guessing game for a number between a `-m|--min` and `-x|--max` value (default 1 and 50, respectively) with a limited number of `-g|--guesses` (default 5). Complain if either `--min` or `--guesses` is less than 1. Accept a `-s|--seed` for `random.seed`. If the user guesses something that is not a number, complain about it.

The game is intended to actually be interactive, which makes it difficult to test. Here is how it should look in interactive mode:

````
$ ./guess.py -s 1
Guess a number between 1 and 50 (q to quit): 25
"25" is too high.
Guess a number between 1 and 50 (q to quit): foo
"foo" is not a number.
Guess a number between 1 and 50 (q to quit): 12
"12" is too high.
Guess a number between 1 and 50 (q to quit): 6
"6" is too low.
Guess a number between 1 and 50 (q to quit): 9
"9" is correct. You win!
````

Because I want to be able to write a test for this, I also want the program to accept an `-i|--inputs` option so that the game can also be played exactly the same but without the prompts for input:

````
$ ./guess.py -s 1 -i 25 foo 12 6 9
"25" is too high.
"foo" is not a number.
"12" is too high.
"6" is too low.
"9" is correct. You win!
````

You should be able to handle this in your inifinite game loop.

\pagebreak

# guess Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import random
     5	import re
     6	import sys
     7	from dire import die
     8	
     9	
    10	# --------------------------------------------------
    11	def get_args():
    12	    """get args"""
    13	    parser = argparse.ArgumentParser(
    14	        description='Guessing game',
    15	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    16	
    17	    parser.add_argument('-m',
    18	                        '--min',
    19	                        help='Minimum value',
    20	                        metavar='int',
    21	                        type=int,
    22	                        default=1)
    23	
    24	    parser.add_argument('-x',
    25	                        '--max',
    26	                        help='Maximum value',
    27	                        metavar='int',
    28	                        type=int,
    29	                        default=50)
    30	
    31	    parser.add_argument('-g',
    32	                        '--guesses',
    33	                        help='Number of guesses',
    34	                        metavar='int',
    35	                        type=int,
    36	                        default=5)
    37	
    38	    parser.add_argument('-s',
    39	                        '--seed',
    40	                        help='Random seed',
    41	                        metavar='int',
    42	                        type=int,
    43	                        default=None)
    44	
    45	    parser.add_argument('-i',
    46	                        '--inputs',
    47	                        help='Inputs',
    48	                        metavar='str',
    49	                        type=str,
    50	                        nargs='+',
    51	                        default=[])
    52	
    53	    return parser.parse_args()
    54	
    55	
    56	# --------------------------------------------------
    57	def main():
    58	    """main"""
    59	    args = get_args()
    60	    low = args.min
    61	    high = args.max
    62	    guesses_allowed = args.guesses
    63	    inputs = args.inputs
    64	    random.seed(args.seed)
    65	
    66	    if low < 1:
    67	        die('--min "{}" cannot be lower than 1'.format(low))
    68	
    69	    if guesses_allowed < 1:
    70	        die('--guesses "{}" cannot be lower than 1'.format(guesses_allowed))
    71	
    72	    if low > high:
    73	        die('--min "{}" is higher than --max "{}"'.format(low, high))
    74	
    75	    secret = random.randint(low, high)
    76	    prompt = 'Guess a number between {} and {} (q to quit): '.format(low, high)
    77	    num_guesses = 0
    78	
    79	    while True:
    80	        guess = inputs.pop(0) if inputs else input(prompt)
    81	        num_guesses += 1
    82	
    83	        if re.match('q(uit)?', guess.lower()):
    84	            print('Now you will never know the answer.')
    85	            sys.exit()
    86	
    87	        # Method 1: test if the guess is a digit
    88	        if not guess.isdigit():
    89	            print('"{}" is not a number.'.format(guess))
    90	            continue
    91	        num = int(guess)
    92	
    93	        # Method 2: try/except
    94	        num = 0
    95	        try:
    96	            num = int(guess)
    97	        except:
    98	            warn('"{}" is not an integer'.format(guess))
    99	            continue
   100	
   101	        if not low <= num <= high:
   102	            print('Number "{}" is not in the allowed range'.format(num))
   103	        elif num == secret:
   104	            print('"{}" is correct. You win!'.format(num))
   105	            break
   106	        else:
   107	            print('"{}" is too {}.'.format(num,
   108	                                           'low' if num < secret else 'high'))
   109	
   110	        if num_guesses >= guesses_allowed:
   111	            print(
   112	                'Too many guesses, loser! The number was "{}."'.format(secret))
   113	            sys.exit(1)
   114	
   115	
   116	# --------------------------------------------------
   117	if __name__ == '__main__':
   118	    main()
````

\pagebreak

# Chapter 18

# Kentucky Fryer

Write a Python program called `fryer.py` that reads some input text from a single positional argument on the command line (which could be a file to read) and transforms the text by dropping the "g" from words two-syllable words ending in "-ing" and also changes "you" to "y'all". Be mindful to keep the case the same on the first letter, e.g, "You" should become "Y'all," "Hunting" should become "Huntin'".

````
$ ./fryer.py
usage: fryer.py [-h] str
fryer.py: error: the following arguments are required: str
$ ./fryer.py -h
usage: fryer.py [-h] str

Southern fry text

positional arguments:
  str         Input text or file

optional arguments:
  -h, --help  show this help message and exit
$ ./fryer.py you
y'all
$ ./fryer.py Fishing
Fishin'
$ ./fryer.py string
string
$ cat tests/input1.txt
So I was fixing to ask him, "Do you want to go fishing?" I was dying
to go for a swing and maybe do some swimming, too.
$ ./fryer.py tests/input1.txt
So I was fixin' to ask him, "Do y'all want to go fishing?" I was dyin'
to go for a swing and maybe do some swimmin', too.
````

\pagebreak

# kentucky_fryer Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import os
     5	import re
     6	import sys
     7	
     8	
     9	# --------------------------------------------------
    10	def get_args():
    11	    """get command-line arguments"""
    12	    parser = argparse.ArgumentParser(
    13	        description='Southern fry text',
    14	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    15	
    16	    parser.add_argument('text', metavar='str', help='Input text or file')
    17	
    18	    return parser.parse_args()
    19	
    20	
    21	# --------------------------------------------------
    22	def fry(word):
    23	    """
    24	    Drop the 'g' from '-ing' words, change "you" to "y'all"
    25	    """
    26	
    27	    ing_word = re.search('(.+)ing([:;,.?])?$', word)
    28	    you = re.match('([Yy])ou$', word)
    29	
    30	    if ing_word:
    31	        prefix = ing_word.group(1)
    32	        if re.search('[aeiouy]', prefix):
    33	            return prefix + "in'" + (ing_word.group(2) or '')
    34	    elif you:
    35	        return you.group(1) + "'all"
    36	
    37	    return word
    38	
    39	
    40	# --------------------------------------------------
    41	def main():
    42	    """Make a jazz noise here"""
    43	
    44	    args = get_args()
    45	    text = args.text
    46	
    47	    if os.path.isfile(text):
    48	        text = open(text).read()
    49	
    50	    for line in text.splitlines():
    51	        print(' '.join(map(fry, line.rstrip().split())))
    52	
    53	
    54	# --------------------------------------------------
    55	if __name__ == '__main__':
    56	    main()
````

\pagebreak

# Chapter 20

# Markov Chains for Words

Write a Python program called `markov.py` that uses the Markov chain algorithm to generate new words from a set of training files. The program should take one or more positional arguments which are files that you read, word-by-word, and note the options of letters after a given `-k|--kmer_size` (default `2`) grouping of letters. E.g., in the word "alabama" with `k=1`, the frequency table will look like:

````
a = l, b, m
l = a
b = a
m = a
````

That is, given this training set, if you started with `l` you could only choose an `a`, but if you have `a` then you could choose `l`, `b`, or `m`.

The program should generate `-n|--num_words` words (default `10`), each a random size between `k` + 2 and a `-m|--max_word` size (default `12`). Be sure to accept `-s|--seed` to pass to `random.seed`. My solution also takes a `-d|--debug` flag that will emit debug messages to `.log` for you to inspect.

Chose the best words and create definitions for them:

* yulcogicism: the study of Christmas gnostics
* umjamp: skateboarding trick
* callots: insignia of officers in Greek army
* urchenev: fungal growth found under cobblestones

````
$ ./markov.py
usage: markov.py [-h] [-n int] [-k int] [-m int] [-s int] [-d] FILE [FILE ...]
markov.py: error: the following arguments are required: FILE
$ ./markov.py -h
usage: markov.py [-h] [-n int] [-k int] [-m int] [-s int] [-d] FILE [FILE ...]

Markov chain for characters/words

positional arguments:
  FILE                  Training file(s)

optional arguments:
  -h, --help            show this help message and exit
  -n int, --num_words int
                        Number of words to generate (default: 10)
  -k int, --kmer_size int
                        Kmer size (default: 2)
  -m int, --max_word int
                        Max word length (default: 12)
  -s int, --seed int    Random seed (default: None)
  -d, --debug           Debug to ".log" (default: False)
$ ./markov.py /usr/share/dict/words -s 1
  1: oveli
  2: uming
  3: uylatiteda
  4: owsh
  5: uuse
  6: ismandl
  7: efortai
  8: eyhopy
  9: auretrab
 10: ozogralach
$ ./markov.py ../inputs/const.txt -s 2 -k 3
  1: romot
  2: leasonsusp
  3: gdoned
  4: bunablished
  5: neithere
  6: achmen
  7: reason
  8: nmentyone
  9: effereof
 10: eipts
````

\pagebreak

# markov_words Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import logging
     5	import os
     6	import random
     7	import re
     8	import sys
     9	from collections import defaultdict
    10	
    11	
    12	# --------------------------------------------------
    13	def get_args():
    14	    """Get command-line arguments"""
    15	
    16	    parser = argparse.ArgumentParser(
    17	        description='Markov chain for characters/words',
    18	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    19	
    20	    parser.add_argument('file',
    21	                        metavar='FILE',
    22	                        nargs='+',
    23	                        help='Training file(s)')
    24	
    25	    parser.add_argument('-n',
    26	                        '--num_words',
    27	                        help='Number of words to generate',
    28	                        metavar='int',
    29	                        type=int,
    30	                        default=10)
    31	
    32	    parser.add_argument('-k',
    33	                        '--kmer_size',
    34	                        help='Kmer size',
    35	                        metavar='int',
    36	                        type=int,
    37	                        default=2)
    38	
    39	    parser.add_argument('-m',
    40	                        '--max_word',
    41	                        help='Max word length',
    42	                        metavar='int',
    43	                        type=int,
    44	                        default=12)
    45	
    46	    parser.add_argument('-s',
    47	                        '--seed',
    48	                        help='Random seed',
    49	                        metavar='int',
    50	                        type=int,
    51	                        default=None)
    52	
    53	    parser.add_argument('-d',
    54	                        '--debug',
    55	                        help='Debug to ".log"',
    56	                        action='store_true')
    57	
    58	    return parser.parse_args()
    59	
    60	
    61	# --------------------------------------------------
    62	def main():
    63	    """Make a jazz noise here"""
    64	
    65	    args = get_args()
    66	    k = args.kmer_size
    67	    random.seed(args.seed)
    68	
    69	    logging.basicConfig(
    70	        filename='.log',
    71	        filemode='w',
    72	        level=logging.DEBUG if args.debug else logging.CRITICAL)
    73	
    74	    # debate use of set/list in terms of letter frequencies
    75	    chains = defaultdict(list)
    76	    for file in args.file:
    77	        for line in open(file):
    78	            for word in line.lower().split():
    79	                word = re.sub('[^a-z]', '', word)
    80	                for i in range(0, len(word) - k):
    81	                    kmer = word[i:i + k + 1]
    82	                    chains[kmer[:-1]].append(kmer[-1])
    83	
    84	    logging.debug(chains)
    85	
    86	    kmers = list(chains.keys())
    87	    starts = set()
    88	
    89	    for i in range(1, args.num_words + 1):
    90	        word = ''
    91	        while not word:
    92	            kmer = random.choice(kmers)
    93	            if not kmer in starts and chains[kmer] and re.search(
    94	                    '[aeiou]', kmer):
    95	                starts.add(kmer)
    96	                word = kmer
    97	
    98	        length = random.choice(range(k + 2, args.max_word))
    99	        logging.debug('Make a word {} long starting with "{}"'.format(
   100	            length, word))
   101	        while len(word) < length:
   102	            if not chains[kmer]: break
   103	            char = random.choice(list(chains[kmer]))
   104	            logging.debug('char = "{}"'.format(char))
   105	            word += char
   106	            kmer = kmer[1:] + char
   107	
   108	        logging.debug('word = "{}"'.format(word))
   109	        print('{:3}: {}'.format(i, word))
   110	
   111	
   112	# --------------------------------------------------
   113	if __name__ == '__main__':
   114	    main()
````

\pagebreak

# Chapter 21

# Pig Latin

Write a Python program named `piggie.py` that takes one or more file names as positional arguments and converts all the words in them into "Pig Latin" (see rules below). Write the output to a directory given with the flags `-o|--outdir` (default `out-yay`) using the same basename as the input file, e.g., `input/foo.txt` would be written to `out-yay/foo.txt`. 

if a file argument names a non-existent file, print a warning to STDERR and skip that file. If the output directory does not exist, create it.

# Pig Latin Rules

1. If the word begins with consonants, e.g., "k" or "ch", move them to the end of the word and append "ay" so that "mouse" becomes "ouse-may" and "chair" becomes "air-chay."
2. If the word begins with a vowel, simple append "-yay" to the end, so "apple" is "apple-yay."

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
[cholla@~/work/python/playful_python/piggie]$ ./piggie.py
usage: piggie.py [-h] [-o str] FILE [FILE ...]
piggie.py: error: the following arguments are required: FILE
[cholla@~/work/python/playful_python/piggie]$ ./piggie.py -h
usage: piggie.py [-h] [-o str] FILE [FILE ...]

Convert to Pig Latin

positional arguments:
  FILE                  Input file(s)

optional arguments:
  -h, --help            show this help message and exit
  -o str, --outdir str  Output directory (default: out-yay)
$ ./piggie.py ../inputs/sonnet-29.txt
  1: sonnet-29.txt
Done, wrote 1 file to "out-yay".
$ head out-yay/sonnet-29.txt
onnet-Say 29-yay
illiam-Way akespeare-Shay

en-Whay, in-yay isgrace-day ith-way ortune-fay and-yay en-may’s-yay eyes-yay,
I-yay all-yay alone-yay eweep-bay y-may outcast-yay ate-stay,
And-yay ouble-tray eaf-day eaven-hay ith-way y-may ootless-bay ies-cray,
And-yay ook-lay upon-yay elf-mysay and-yay urse-cay y-may ate-fay,
ishing-Way e-may ike-lay o-tay one-yay ore-may ich-ray in-yay ope-hay,
eatured-Fay ike-lay im-hay, ike-lay im-hay ith-way iends-fray ossessed-pay,
esiring-Day is-thay an-may’s-yay art-yay and-yay at-thay an-may’s-yay ope-scay,
````

\pagebreak

# piggie Solution

````
     1	#!/usr/bin/env python3
     2	"""Convert text to Pig Latin"""
     3	
     4	import argparse
     5	import os
     6	import re
     7	import string
     8	from dire import warn
     9	
    10	
    11	# --------------------------------------------------
    12	def get_args():
    13	    """get command-line arguments"""
    14	
    15	    parser = argparse.ArgumentParser(
    16	        description='Convert to Pig Latin',
    17	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    18	
    19	    parser.add_argument('file',
    20	                        metavar='FILE',
    21	                        nargs='+',
    22	                        help='Input file(s)')
    23	
    24	    parser.add_argument('-o',
    25	                        '--outdir',
    26	                        help='Output directory',
    27	                        metavar='str',
    28	                        type=str,
    29	                        default='out-yay')
    30	
    31	    return parser.parse_args()
    32	
    33	
    34	# --------------------------------------------------
    35	def main():
    36	    """Make a jazz noise here"""
    37	
    38	    args = get_args()
    39	    out_dir = args.outdir
    40	
    41	    if not os.path.isdir(out_dir):
    42	        os.makedirs(out_dir)
    43	
    44	    num_files = 0
    45	    for i, file in enumerate(args.file, start=1):
    46	        basename = os.path.basename(file)
    47	        out_file = os.path.join(out_dir, basename)
    48	        out_fh = open(out_file, 'wt')
    49	        print('{:3}: {}'.format(i, basename))
    50	
    51	        if not os.path.isfile(file):
    52	            warn('"{}" is not a file.'.format(file))
    53	            continue
    54	
    55	        num_files += 1
    56	        for line in open(file):
    57	            for bit in re.split(r"([\w']+)", line):
    58	                out_fh.write(pig(bit))
    59	
    60	        out_fh.close()
    61	
    62	    print('Done, wrote {} file{} to "{}".'.format(
    63	        num_files, '' if num_files == 1 else 's', out_dir))
    64	
    65	
    66	# --------------------------------------------------
    67	def pig(word):
    68	    """Create Pig Latin version of a word"""
    69	
    70	    if re.match(r"^[\w']+$", word):
    71	        consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
    72	        match = re.match('^([' + consonants + ']+)(.+)', word)
    73	        if match:
    74	            word = '-'.join([match.group(2), match.group(1) + 'ay'])
    75	        else:
    76	            word = word + '-yay'
    77	
    78	    return word
    79	
    80	
    81	# --------------------------------------------------
    82	if __name__ == '__main__':
    83	    main()
````

\pagebreak

# Chapter 22

# Soundex Rhymer

Write a Python program called `rhymer.py` that uses the Soundex algorithm/module (https://en.wikipedia.org/wiki/Soundex, https://pypi.org/project/soundex/) to find words that rhyme with a given input word. When comparing words, it would be best to discount any leading consonants, e.g., the words "listen" and "glisten" rhyme but only if you compare the "isten" part. The program should take an optional `-w|--wordlist` argument (default "/usr/share/dict/words") for the comparisons.

````
$ ./rhymer.py
usage: rhymer.py [-h] [-w str] str
rhymer.py: error: the following arguments are required: str
[cholla@~/work/python/playful_python/soundex-rhymer]$ ./rhymer.py -h
usage: rhymer.py [-h] [-w str] str

Use Soundex to find rhyming words

positional arguments:
  str                   Word

optional arguments:
  -h, --help            show this help message and exit
  -w str, --wordlist str
                        Wordlist (default: /usr/share/dict/words)
$ ./rhymer.py orange | head
boring
borning
boronic
borrowing
chloranemic
chlorinize
chlorinous
chorionic
choromanic
clowring
````

\pagebreak

# soundex_rhymer Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import re
     5	import soundex
     6	import string
     7	import sys
     8	
     9	
    10	# --------------------------------------------------
    11	def get_args():
    12	    """get command-line arguments"""
    13	    parser = argparse.ArgumentParser(
    14	        description='Use Soundex to find rhyming words',
    15	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    16	
    17	    parser.add_argument('word', metavar='str', help='Word')
    18	
    19	    parser.add_argument('-w',
    20	                        '--wordlist',
    21	                        metavar='str',
    22	                        help='Wordlist',
    23	                        default='/usr/share/dict/words')
    24	
    25	    return parser.parse_args()
    26	
    27	
    28	# --------------------------------------------------
    29	def main():
    30	    """Make a jazz noise here"""
    31	    args = get_args()
    32	    word = args.word
    33	    wordlist = args.wordlist
    34	
    35	    stem = word
    36	    consonants = [c for c in string.ascii_lowercase if c not in 'aeiou']
    37	    regex = re.compile('^[' + ''.join(consonants) + ']+(.+)')
    38	
    39	    def stemmer(word):
    40	        match = regex.search(word)
    41	        return match.group(1) if match else word
    42	
    43	    sndx = soundex.Soundex()
    44	    cmp = sndx.soundex(stemmer(word))
    45	
    46	    for line in open(wordlist):
    47	        for w in line.split():
    48	            if w != word and sndx.soundex(stemmer(w)) == cmp:
    49	                print(w)
    50	
    51	
    52	# --------------------------------------------------
    53	if __name__ == '__main__':
    54	    main()
````

\pagebreak

# Chapter 23

# Substring Guessing Game

Write a Python program called `sub.py` that plays a guessing game where you read a `-f|--file` input (default `/usr/share/dict/words`) and use a given `-k|--ksize` to find all the words grouped by their shared kmers. Remove any kmers where the number of words is fewer than `-m|--min_words`. Also accept a `-s|--seed` for `random.seed` for testing purposes. Prompt the user to guess a word for a randomly chosen kmer. If their guess is not present in the shared list, taunt them mercilessly. If their guess is present, affirm their worth and prompt to guess again. Allow them to use `!` to quit and `?` to be provided a hint (a word from the list). For both successful guesses and hints, remove the word from the shared list. When they have quit or exhausted the list, quit play. At the end of the game, report the number of found words.

````
$ ./sub.py -h
usage: sub.py [-h] [-f str] [-s int] [-m int] [-k int]

Find words sharing a substring

optional arguments:
  -h, --help            show this help message and exit
  -f str, --file str    Input file (default: /usr/share/dict/words)
  -s int, --seed int    Random seed (default: None)
  -m int, --min_words int
                        Minimum number of words for a given kmer (default: 3)
  -k int, --ksize int   Size of k (default: 4)
$ ./sub.py
Name a word that contains "slak" [!=quit, ?=hint] (10 left) slake
Totes! "slake" is found!
Name a word that contains "slak" [!=quit, ?=hint] (9 left) ?
For instance, "breislakite"...
Name a word that contains "slak" [!=quit, ?=hint] (8 left) unslakable
Totes! "unslakable" is found!
Name a word that contains "slak" [!=quit, ?=hint] (7 left) q
What is wrong with you?
Name a word that contains "slak" [!=quit, ?=hint] (7 left) !
Quitter!
Hey, you found 2 words! Not bad.
````

\pagebreak

# substring Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import os
     5	import random
     6	import re
     7	import sys
     8	from collections import defaultdict
     9	from dire import die
    10	
    11	
    12	# --------------------------------------------------
    13	def get_args():
    14	    """get command-line arguments"""
    15	    parser = argparse.ArgumentParser(
    16	        description='Find words sharing a substring',
    17	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    18	
    19	    parser.add_argument('-f',
    20	                        '--file',
    21	                        metavar='str',
    22	                        help='Input file',
    23	                        type=str,
    24	                        default='/usr/share/dict/words')
    25	
    26	    parser.add_argument('-s',
    27	                        '--seed',
    28	                        help='Random seed',
    29	                        metavar='int',
    30	                        type=int,
    31	                        default=None)
    32	
    33	    parser.add_argument('-m',
    34	                        '--min_words',
    35	                        help='Minimum number of words for a given kmer',
    36	                        metavar='int',
    37	                        type=int,
    38	                        default=3)
    39	
    40	    parser.add_argument('-k',
    41	                        '--ksize',
    42	                        help='Size of k',
    43	                        metavar='int',
    44	                        type=int,
    45	                        default=4)
    46	
    47	    return parser.parse_args()
    48	
    49	
    50	# --------------------------------------------------
    51	def get_words(file):
    52	    """Get words from input file"""
    53	
    54	    if not os.path.isfile(file):
    55	        die('"{}" is not a file')
    56	
    57	    words = set()
    58	    for line in open(file):
    59	        for word in line.split():
    60	            words.add(re.sub('[^a-zA-Z0-9]', '', word.lower()))
    61	
    62	    if not words:
    63	        die('No usable words in "{}"'.format(file))
    64	
    65	    return words
    66	
    67	
    68	# --------------------------------------------------
    69	def get_kmers(words, k, min_words):
    70	    """ Find all words sharing kmers"""
    71	
    72	    if k <= 1:
    73	        die('-k "{}" must be greater than 1'.format(k))
    74	
    75	    shared = defaultdict(list)
    76	    for word in words:
    77	        for kmer in [word[i:i + k] for i in range(len(word) - k + 1)]:
    78	            shared[kmer].append(word)
    79	
    80	    # Select kmers having enough words (can't use `pop`!)
    81	
    82	    # Method 1: for loop
    83	    ok = dict()
    84	    for kmer in shared:
    85	        if len(shared[kmer]) >= min_words:
    86	            ok[kmer] = shared[kmer]
    87	
    88	    # Method 2: list comprehension
    89	    # ok = dict([(kmer, shared[kmer]) for kmer in shared
    90	    #            if len(shared[kmer]) >= min_words])
    91	
    92	    # Method 3: map/filter
    93	    # ok = dict(
    94	    #     map(lambda kmer: (kmer, shared[kmer]),
    95	    #         filter(lambda kmer: len(shared[kmer]) >= min_words,
    96	    #                shared.keys())))
    97	
    98	    return ok
    99	
   100	
   101	# --------------------------------------------------
   102	def main():
   103	    """Make a jazz noise here"""
   104	
   105	    args = get_args()
   106	
   107	    random.seed(args.seed)
   108	
   109	    shared = get_kmers(get_words(args.file), args.ksize, args.min_words)
   110	
   111	    # Choose a kmer, setup game state
   112	    kmer = random.choice(list(shared.keys()))
   113	    guessed = set()
   114	    found = []
   115	    prompt = 'Name a word that contains "{}" [!=quit, ?=hint] '.format(kmer)
   116	    compliments = ['Nice', 'Rock on', 'Totes', 'Fantastic', 'Excellent']
   117	    taunts = [
   118	        'Surely you jest!', 'Are you kidding me?',
   119	        'You must have rocks for brains.', 'What is wrong with you?'
   120	    ]
   121	
   122	    #print(kmer, shared[kmer])
   123	
   124	    while True:
   125	        num_left = len(shared[kmer])
   126	        if num_left == 0:
   127	            print('No more words!')
   128	            break
   129	
   130	        guess = input(prompt + '({} left) '.format(num_left)).lower()
   131	
   132	        if guess == '?':
   133	            # Provide a hint
   134	            pos = random.choice(range(len(shared[kmer])))
   135	            word = shared[kmer].pop(pos)
   136	            print('For instance, "{}"...'.format(word))
   137	
   138	        elif guess == '!':
   139	            # Bail
   140	            print('Quitter!')
   141	            break
   142	
   143	        elif guess in guessed:
   144	            # Chastise
   145	            print('You have already guessed "{}"'.format(guess))
   146	
   147	        elif guess in shared[kmer]:
   148	            # Remove the word, feedback with compliment
   149	            pos = shared[kmer].index(guess)
   150	            word = shared[kmer].pop(pos)
   151	            print('{}! "{}" is found!'.format(random.choice(compliments),
   152	                                              word))
   153	            found.append(word)
   154	            guessed.add(guess)
   155	
   156	        else:
   157	            # Taunt
   158	            print(random.choice(taunts))
   159	
   160	    # Game over, man!
   161	    if found:
   162	        n = len(found)
   163	        print('Hey, you found {} word{}! Not bad.'.format(
   164	            n, '' if n == 1 else 's'))
   165	    else:
   166	        print('Wow, you found no words. You suck!')
   167	
   168	
   169	# --------------------------------------------------
   170	if __name__ == '__main__':
   171	    main()
````

\pagebreak

# Chapter 24

# Tic-Tac-Toe Outcome

Create a Python program called `outcome.py` that takes a given Tic-Tac-Toe state as it's only (positional) argument and reports if X or O has won or if there is no winner. The state should only contain the characters ".", "O", and "X", and must be exactly 9 characters long. If there is not exactly one argument, print a "usage" statement.

````
$ ./outcome.py
Usage: outcome.py STATE
$ ./outcome.py ..X.OA..X
State "..X.OA..X" must be 9 characters of only ., X, O
$ ./outcome.py ..X.OX...
No winner
$ ./outcome.py ..X.OX..X
X has won
````

\pagebreak

# tictactoe Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import os
     4	import re
     5	import sys
     6	
     7	
     8	# --------------------------------------------------
     9	def main():
    10	    args = sys.argv[1:]
    11	
    12	    if len(args) != 1:
    13	        print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
    14	        sys.exit(1)
    15	
    16	    state = args[0]
    17	
    18	    if not re.search('^[.XO]{9}$', state):
    19	        print('State "{}" must be 9 characters of only ., X, O'.format(state),
    20	              file=sys.stderr)
    21	        sys.exit(1)
    22	
    23	    winning = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
    24	               [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    25	
    26	    winner = 'No winner'
    27	
    28	    # for player in ['X', 'O']:
    29	    #     for combo in winning:
    30	    #         i, j, k = combo
    31	    #         if state[i] == player and state[j] == player and state[k] == player:
    32	    #             winner = player
    33	    #             break
    34	
    35	    # for player in ['X', 'O']:
    36	    #     for combo in winning:
    37	    #         chars = []
    38	    #         for i in combo:
    39	    #             chars.append(state[i])
    40	
    41	    #         if ''.join(chars) == player * 3:
    42	    #             winner = player
    43	    #             break
    44	
    45	    # for player in ['X', 'O']:
    46	    #     for i, j, k in winning:
    47	    #         chars = ''.join([state[i], state[j], state[k]])
    48	    #         if ''.join(chars) == '{}{}{}'.format(player, player, player):
    49	    #             winner = player
    50	    #             break
    51	
    52	    for player in ['X', 'O']:
    53	        for i, j, k in winning:
    54	            combo = [state[i], state[j], state[k]]
    55	            if combo == [player, player, player]:
    56	                winner = '{} has won'.format(player)
    57	                break
    58	
    59	    # for combo in winning:
    60	    #     group = list(map(lambda i: state[i], combo))
    61	    #     for player in ['X', 'O']:
    62	    #         if all(x == player for x in group):
    63	    #             winner = player
    64	    #             break
    65	
    66	    print(winner)
    67	
    68	
    69	# --------------------------------------------------
    70	if __name__ == '__main__':
    71	    main()
````

\pagebreak

# Chapter 25

# Twelve Days of Christmas

Write a Python program called `twelve_days.py` that will generate the "Twelve Days of Christmas" song up to the `-n|--number_days` argument (default `12`), writing the resulting text to the `-o|--outfile` argument (default STDOUT).

````
$ ./twelve_days.py -h
usage: twelve_days.py [-h] [-o str] [-n int]

Twelve Days of Christmas

optional arguments:
  -h, --help            show this help message and exit
  -o str, --outfile str
                        Outfile (STDOUT) (default: )
  -n int, --number_days int
                        Number of days to sing (default: 12)
$ ./twelve_days.py -n 1
On the first day of Christmas,
My true love gave to me,
A partridge in a pear tree.

$ ./twelve_days.py -n 3
On the first day of Christmas,
My true love gave to me,
A partridge in a pear tree.

On the second day of Christmas,
My true love gave to me,
Two turtle doves,
And a partridge in a pear tree.

On the third day of Christmas,
My true love gave to me,
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

$ ./twelve_days.py -o out
$ wc -l out
     113 out
````

\pagebreak

# twelve_days_of_christmas Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import sys
     5	from dire import die
     6	
     7	
     8	# --------------------------------------------------
     9	def get_args():
    10	    """get command-line arguments"""
    11	    parser = argparse.ArgumentParser(
    12	        description='Twelve Days of Christmas',
    13	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    14	
    15	    parser.add_argument('-o',
    16	                        '--outfile',
    17	                        help='Outfile (STDOUT)',
    18	                        metavar='str',
    19	                        type=str,
    20	                        default='')
    21	
    22	    parser.add_argument('-n',
    23	                        '--number_days',
    24	                        help='Number of days to sing',
    25	                        metavar='int',
    26	                        type=int,
    27	                        default=12)
    28	
    29	    return parser.parse_args()
    30	
    31	
    32	# --------------------------------------------------
    33	def main():
    34	    """Make a jazz noise here"""
    35	
    36	    args = get_args()
    37	    out_file = args.outfile
    38	    num_days = args.number_days
    39	    out_fh = open(out_file, 'wt') if out_file else sys.stdout
    40	
    41	    days = {
    42	        12: 'Twelve drummers drumming',
    43	        11: 'Eleven pipers piping',
    44	        10: 'Ten lords a leaping',
    45	        9: 'Nine ladies dancing',
    46	        8: 'Eight maids a milking',
    47	        7: 'Seven swans a swimming',
    48	        6: 'Six geese a laying',
    49	        5: 'Five gold rings',
    50	        4: 'Four calling birds',
    51	        3: 'Three French hens',
    52	        2: 'Two turtle doves',
    53	        1: 'a partridge in a pear tree',
    54	    }
    55	
    56	    ordinal = {
    57	        12: 'twelfth', 11: 'eleven', 10: 'tenth',
    58	        9: 'ninth', 8: 'eighth', 7: 'seventh',
    59	        6: 'sixth', 5: 'fifth', 4: 'fourth',
    60	        3: 'third', 2: 'second', 1: 'first',
    61	    }
    62	
    63	    if not num_days in days:
    64	        die('Cannot sing "{}" days'.format(num_days))
    65	
    66	    for i in range(1, num_days + 1):
    67	        first = 'On the {} day of Christmas,\nMy true love gave to me,'
    68	        out_fh.write(first.format(ordinal[i]) + '\n')
    69	        for j in reversed(range(1, i + 1)):
    70	            if j == 1:
    71	                if i == 1:
    72	                    out_fh.write('{}.\n'.format(days[j].title()))
    73	                else:
    74	                    out_fh.write('And {}.\n'.format(days[j]))
    75	            else:
    76	                out_fh.write('{},\n'.format(days[j]))
    77	
    78	        if i < max(days.keys()):
    79	            out_fh.write('\n')
    80	
    81	
    82	# --------------------------------------------------
    83	if __name__ == '__main__':
    84	    main()
````

\pagebreak

# Chapter 26

# War

> The generation of random numbers is too important to be left to chance. -- Robert R. Coveyou

Create a Python program called "war.py" that plays the card game "War." The program will use the `random` module to shuffle a deck of cards, so your program will need to accept a `-s|--seed` argument (default: `None`) which you will use to call `random.seed`, if present.
 
First you program will need to create a deck of cards. You will need to use the Unicode symbols for the suites ( ♥ ♠ ♣ ♦ ) [which won't display in the PDF, so consult the Markdown file] and combine those with the numbers 2-10 and the letters "J", "Q," "K," and "A." (hint: look at `itertools.product`). 

````
>>> from itertools import product
>>> a = list('ABC')
>>> b = range(3)
>>> list(product(a, b))
[('A', 0), ('A', 1), ('A', 2), ('B', 0), ('B', 1), ('B', 2), ('C', 0), ('C', 1), ('C', 2)]
````

**NB**: You must sort your deck and then use the `random.shuffle` method so that your cards will be in the correct order to pass the tests!

In the real game of War, the cards are shuffled and then dealt one card each first to the non-dealer, then to the dealer, until all cards are dealt and each player has 26 cards. We will not be modeling this behavior. When writing your version of the game, simply `pop` two cards off the deck as the cards for player 1 and player 2, respectively. Compare the two cards by ignoring the suite and evaluating the value where 2 is the lowest and Aces are the highest. When two cards have the same values (e.g., two 5s or two Jacks), print "WAR!" In the real game, this initiates a sub-game of War which is a "recursive" algorithm which we will not bother modeling. Keep track of which player wins each round where no points are awarded in a tie. At the end, report the points for each player and state the winner. In the event of a tie, print "DRAW."

````
$ ./war.py -h
usage: war.py [-h] [-s int]

"War" cardgame

optional arguments:
  -h, --help          show this help message and exit
  -s int, --seed int  Random seed (default: None)
$ ./war.py -s 1
 ♠9  ♥J P2
 ♦A  ♠5 P1
 ♣4  ♠8 P2
 ♥6  ♥3 P1
 ♥5  ♦3 P1
 ♣K ♣10 P1
 ♠7  ♦7 WAR!
 ♠2  ♦4 P2
 ♥2 ♠10 P2
 ♦6  ♣5 P1
 ♣2  ♣6 P2
 ♠4  ♥8 P2
 ♠J  ♥9 P1
♥10  ♣Q P2
 ♣8  ♥7 P1
 ♦K  ♠Q P1
♦10  ♦2 P1
 ♣9  ♦9 WAR!
 ♦8  ♣J P2
 ♣3  ♦5 P2
 ♦Q  ♥4 P1
 ♠6  ♥A P2
 ♠K  ♣7 P1
 ♥Q  ♠3 P1
 ♣A  ♥K P1
 ♠A  ♦J P1
P1 14 P2 10: Player 1 wins
$ ./war.py -s 2
 ♠4  ♠6 P2
 ♦K  ♣J P1
 ♠J  ♦4 P1
 ♣7  ♣4 P1
 ♥Q ♣10 P1
 ♦5  ♠3 P1
 ♥K  ♦9 P1
 ♥2  ♣Q P2
 ♥7  ♦A P2
 ♥3  ♥A P2
 ♣5  ♥8 P2
 ♠2 ♦10 P2
♠10  ♠K P2
 ♣2  ♦3 P2
 ♠Q  ♦8 P1
 ♦6  ♦J P2
 ♥6  ♣8 P2
 ♠8  ♦7 P1
 ♥5  ♦2 P1
 ♣6  ♥J P2
 ♥9  ♠9 WAR!
 ♣K  ♣A P2
♥10  ♦Q P2
 ♠7  ♠5 P1
 ♣9  ♠A P2
 ♥4  ♣3 P1
P1 11 P2 14: Player 2 wins
$ ./war.py -s 10
 ♥J  ♠3 P1
 ♥2  ♥5 P2
 ♦Q ♠10 P1
♣10  ♥4 P1
 ♥6  ♣5 P1
 ♦3  ♠J P2
 ♦K  ♥8 P1
 ♦5  ♣8 P2
 ♠5  ♣3 P1
 ♣J ♦10 P1
♥10  ♦J P2
 ♥A  ♣7 P1
 ♠K  ♠Q P1
 ♦7  ♠A P2
 ♣9  ♠9 WAR!
 ♣2  ♠6 P2
 ♣K  ♦A P2
 ♦6  ♥Q P2
 ♠8  ♥9 P2
 ♥3  ♠7 P2
 ♦8  ♣Q P2
 ♣6  ♠4 P1
 ♥7  ♠2 P1
 ♣4  ♦4 WAR!
 ♦9  ♦2 P1
 ♥K  ♣A P2
P1 12 P2 12: DRAW
````

\pagebreak

# war Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import random
     5	import sys
     6	from itertools import product
     7	
     8	
     9	# --------------------------------------------------
    10	def get_args():
    11	    """get command-line arguments"""
    12	    parser = argparse.ArgumentParser(
    13	        description='"War" cardgame',
    14	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    15	
    16	    parser.add_argument('-s',
    17	                        '--seed',
    18	                        help='Random seed',
    19	                        metavar='int',
    20	                        type=int,
    21	                        default=None)
    22	
    23	    return parser.parse_args()
    24	
    25	
    26	# --------------------------------------------------
    27	def main():
    28	    """Make a jazz noise here"""
    29	    args = get_args()
    30	    seed = args.seed
    31	
    32	    if seed is not None:
    33	        random.seed(seed)
    34	
    35	    suits = list('♥♠♣♦')
    36	    values = list(map(str, range(2, 11))) + list('JQKA')
    37	    cards = sorted(map(lambda t: '{}{}'.format(*t), product(suits, values)))
    38	    random.shuffle(cards)
    39	
    40	    p1_wins = 0
    41	    p2_wins = 0
    42	
    43	    card_value = dict(
    44	        list(map(lambda t: list(reversed(t)), enumerate(list(values)))))
    45	
    46	    while cards:
    47	        p1, p2 = cards.pop(), cards.pop()
    48	        v1, v2 = card_value[p1[1:]], card_value[p2[1:]]
    49	        res = ''
    50	
    51	        if v1 > v2:
    52	            p1_wins += 1
    53	            res = 'P1'
    54	        elif v2 > v1:
    55	            p2_wins += 1
    56	            res = 'P2'
    57	        else:
    58	            res = 'WAR!'
    59	
    60	        print('{:>3} {:>3} {}'.format(p1, p2, res))
    61	
    62	    print('P1 {} P2 {}: {}'.format(
    63	        p1_wins, p2_wins, 'Player 1 wins' if p1_wins > p2_wins else
    64	        'Player 2 wins' if p2_wins > p1_wins else 'DRAW'))
    65	
    66	
    67	# --------------------------------------------------
    68	if __name__ == '__main__':
    69	    main()
````

\pagebreak

# Chapter 27

# Anagram

Write a program called `presto.py` that will find anagrams of a given positional argument. The program should take an optional `-w|--wordlist` (default `/usr/share/dict/words`) and produce output that includes combinations of `-n|num_combos` words (default `1`) that are anagrams of the given input.

````
$ ./presto.py
usage: presto.py [-h] [-w str] [-n int] [-d] str
presto.py: error: the following arguments are required: str
$ ./presto.py -h
usage: presto.py [-h] [-w str] [-n int] [-d] str

Find anagrams

positional arguments:
  str                   Input text

optional arguments:
  -h, --help            show this help message and exit
  -w str, --wordlist str
                        Wordlist (default: /usr/share/dict/words)
  -n int, --num_combos int
                        Number of words combination to test (default: 1)
  -d, --debug           Debug (default: False)
$ ./presto.py presto
presto =
   1. poster
   2. repost
   3. respot
   4. stoper
$ ./presto.py listen
listen =
   1. enlist
   2. silent
   3. tinsel
$ ./presto.py listen -n 2 | tail
  82. sten li
  83. te nils
  84. ten lis
  85. ten sil
  86. ti lens
  87. til ens
  88. til sen
  89. tin els
  90. tin les
  91. tinsel
````

\pagebreak

# anagram Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import logging
     5	import os
     6	import re
     7	import sys
     8	from collections import defaultdict, Counter
     9	from itertools import combinations, permutations, product, chain
    10	from dire import warn, die
    11	
    12	
    13	# --------------------------------------------------
    14	def get_args():
    15	    """get command-line arguments"""
    16	    parser = argparse.ArgumentParser(
    17	        description='Find anagrams',
    18	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    19	
    20	    parser.add_argument('text', metavar='str', help='Input text')
    21	
    22	    parser.add_argument('-w',
    23	                        '--wordlist',
    24	                        help='Wordlist',
    25	                        metavar='str',
    26	                        type=str,
    27	                        default='/usr/share/dict/words')
    28	
    29	    parser.add_argument('-n',
    30	                        '--num_combos',
    31	                        help='Number of words combination to test',
    32	                        metavar='int',
    33	                        type=int,
    34	                        default=1)
    35	
    36	    parser.add_argument('-d', '--debug', help='Debug', action='store_true')
    37	
    38	    return parser.parse_args()
    39	
    40	
    41	# --------------------------------------------------
    42	def main():
    43	    """Make a jazz noise here"""
    44	    args = get_args()
    45	    text = args.text
    46	    word_list = args.wordlist
    47	
    48	    if not os.path.isfile(word_list):
    49	        die('--wordlist "{}" is not a file'.format(word_list))
    50	
    51	    logging.basicConfig(
    52	        filename='.log',
    53	        filemode='w',
    54	        level=logging.DEBUG if args.debug else logging.CRITICAL)
    55	
    56	    words = defaultdict(set)
    57	    for line in open(word_list):
    58	        for word in line.split():
    59	            clean = re.sub('[^a-z0-9]', '', word.lower())
    60	            if len(clean) == 1 and clean not in 'ai':
    61	                continue
    62	            words[len(clean)].add(clean)
    63	
    64	    text_len = len(text)
    65	    counts = Counter(text)
    66	    anagrams = set()
    67	    lengths = list(words.keys())
    68	    for i in range(1, args.num_combos + 1):
    69	        key_combos = list(
    70	            filter(
    71	                lambda t: sum(t) == text_len,
    72	                set(
    73	                    map(lambda t: tuple(sorted(t)),
    74	                        combinations(chain(lengths, lengths), i)))))
    75	
    76	        for keys in key_combos:
    77	            logging.debug('Searching keys {}'.format(keys))
    78	            word_combos = list(product(*list(map(lambda k: words[k], keys))))
    79	
    80	            for t in word_combos:
    81	                if Counter(''.join(t)) == counts:
    82	                    for p in filter(
    83	                            lambda x: x != text,
    84	                            map(lambda x: ' '.join(x), permutations(t))):
    85	                        anagrams.add(p)
    86	
    87	            logging.debug('# anagrams = {}'.format(len(anagrams)))
    88	
    89	    logging.debug('Finished searching')
    90	
    91	    if anagrams:
    92	        print('{} ='.format(text))
    93	        for i, t in enumerate(sorted(anagrams), 1):
    94	            print('{:4}. {}'.format(i, t))
    95	    else:
    96	        print('No anagrams for "{}".'.format(text))
    97	
    98	
    99	# --------------------------------------------------
   100	if __name__ == '__main__':
   101	    main()
````

\pagebreak

# Chapter 28

# Hangman

Write a Python program called `hangman.py` that will play a game of Hangman which is a bit like "Wheel of Fortune" where you present the user with a number of elements indicating the length of a word. For our game, use the underscore `_` to indicate a letter that has not been guessed. The program should take `-n|--minlen` minimum length (default `5`) and `-l|--maxlen` maximum length options (default `10`) to indicate the minimum and maximum lengths of the randomly chosen word taken from the `-w|--wordlist` option (default `/usr/share/dict/words`). It also needs to take `-s|--seed` to for the random seed and the `-m|--misses` number of misses to allow the player.

To play, you will initiate an inifinite loop and keep track of the game state, e.g., the word to guess, the letters already guessed, the letters found, the number of misses. As this is an interactive game, I cannot write an test suite, so you can play my version and then try to write one like it. If the user guesses a letter that is in the word, replace the `_` characters with the letter. If the user guesses the same letter twice, admonish them. If the user guesses a letter that is not in the word, increment the misses and let them know they missed. If the user guesses too many times, exit the game and insult them. If they correctly guess the word, let them know and exit the game.

````
$ ./hangman.py -h
usage: hangman.py [-h] [-l MAXLEN] [-n MINLEN] [-m MISSES] [-s SEED]
                  [-w WORDLIST]

Hangman

optional arguments:
  -h, --help            show this help message and exit
  -l MAXLEN, --maxlen MAXLEN
                        Max word length (default: 10)
  -n MINLEN, --minlen MINLEN
                        Min word length (default: 5)
  -m MISSES, --misses MISSES
                        Max number of misses (default: 10)
  -s SEED, --seed SEED  Random seed (default: None)
  -w WORDLIST, --wordlist WORDLIST
                        Word list (default: /usr/share/dict/words)
$ ./hangman.py
_ _ _ _ _ _ _ _ (Misses: 0)
Your guess? ("?" for hint, "!" to quit) a
_ _ _ _ _ _ _ _ (Misses: 1)
Your guess? ("?" for hint, "!" to quit) i
_ _ _ _ _ _ i _ (Misses: 1)
Your guess? ("?" for hint, "!" to quit) e
_ _ _ _ _ _ i _ (Misses: 2)
Your guess? ("?" for hint, "!" to quit) o
_ o _ _ _ _ i _ (Misses: 2)
Your guess? ("?" for hint, "!" to quit) u
_ o _ _ _ _ i _ (Misses: 3)
Your guess? ("?" for hint, "!" to quit) y
_ o _ _ _ _ i _ (Misses: 4)
Your guess? ("?" for hint, "!" to quit) c
_ o _ _ _ _ i _ (Misses: 5)
Your guess? ("?" for hint, "!" to quit) d
_ o _ _ _ _ i _ (Misses: 6)
Your guess? ("?" for hint, "!" to quit) p
_ o _ _ _ _ i p (Misses: 6)
Your guess? ("?" for hint, "!" to quit) m
_ o _ _ _ _ i p (Misses: 7)
Your guess? ("?" for hint, "!" to quit) n
_ o _ _ _ _ i p (Misses: 8)
Your guess? ("?" for hint, "!" to quit) s
_ o s _ s _ i p (Misses: 8)
Your guess? ("?" for hint, "!" to quit) t
_ o s t s _ i p (Misses: 8)
Your guess? ("?" for hint, "!" to quit) h
You win. You guessed "hostship" with "8" misses!
$ ./hangman.py -m 2
_ _ _ _ _ _ _ _ _ _ (Misses: 0)
Your guess? ("?" for hint, "!" to quit) a
_ _ _ _ _ _ a _ _ a (Misses: 0)
Your guess? ("?" for hint, "!" to quit) b
_ _ _ _ _ _ a _ _ a (Misses: 1)
Your guess? ("?" for hint, "!" to quit) c
You lose, loser!  The word was "metromania."
````

\pagebreak

# hangman Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import os
     5	import random
     6	import re
     7	import sys
     8	from dire import die
     9	
    10	
    11	# --------------------------------------------------
    12	def get_args():
    13	    """parse arguments"""
    14	    parser = argparse.ArgumentParser(
    15	        description='Hangman',
    16	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    17	
    18	    parser.add_argument('-l',
    19	                        '--maxlen',
    20	                        help='Max word length',
    21	                        type=int,
    22	                        default=10)
    23	
    24	    parser.add_argument('-n',
    25	                        '--minlen',
    26	                        help='Min word length',
    27	                        type=int,
    28	                        default=5)
    29	
    30	    parser.add_argument('-m',
    31	                        '--misses',
    32	                        help='Max number of misses',
    33	                        type=int,
    34	                        default=10)
    35	
    36	    parser.add_argument('-s',
    37	                        '--seed',
    38	                        help='Random seed',
    39	                        type=str,
    40	                        default=None)
    41	
    42	    parser.add_argument('-w',
    43	                        '--wordlist',
    44	                        help='Word list',
    45	                        type=str,
    46	                        default='/usr/share/dict/words')
    47	
    48	    return parser.parse_args()
    49	
    50	
    51	# --------------------------------------------------
    52	def bail(msg):
    53	    """Print a message to STDOUT and quit with no error"""
    54	    print(msg)
    55	    sys.exit(0)
    56	
    57	
    58	# --------------------------------------------------
    59	def main():
    60	    """main"""
    61	    args = get_args()
    62	    max_len = args.maxlen
    63	    min_len = args.minlen
    64	    max_misses = args.misses
    65	    wordlist = args.wordlist
    66	
    67	    random.seed(args.seed)
    68	
    69	    if not os.path.isfile(wordlist):
    70	        die('--wordlist "{}" is not a file.'.format(wordlist))
    71	
    72	    if min_len < 1:
    73	        die('--minlen must be positive')
    74	
    75	    if not 3 <= max_len <= 20:
    76	        die('--maxlen should be between 3 and 20')
    77	
    78	    if min_len > max_len:
    79	        die('--minlen ({}) is greater than --maxlen ({})'.format(
    80	            min_len, max_len))
    81	
    82	    good_word = re.compile('^[a-z]{' + str(min_len) + ',' + str(max_len) +
    83	                           '}$')
    84	    words = [w for w in open(wordlist).read().split() if good_word.match(w)]
    85	
    86	    word = random.choice(words)
    87	    play({'word': word, 'max_misses': max_misses})
    88	
    89	
    90	# --------------------------------------------------
    91	def play(state):
    92	    """Loop to play the game"""
    93	    word = state.get('word') or ''
    94	
    95	    if not word: die('No word!')
    96	
    97	    guessed = state.get('guessed') or list('_' * len(word))
    98	    prev_guesses = state.get('prev_guesses') or set()
    99	    num_misses = state.get('num_misses') or 0
   100	    max_misses = state.get('max_misses') or 0
   101	
   102	    if ''.join(guessed) == word:
   103	        msg = 'You win. You guessed "{}" with "{}" miss{}!'
   104	        bail(msg.format(word, num_misses, '' if num_misses == 1 else 'es'))
   105	
   106	    if num_misses >= max_misses:
   107	        bail('You lose, loser!  The word was "{}."'.format(word))
   108	
   109	    print('{} (Misses: {})'.format(' '.join(guessed), num_misses))
   110	    new_guess = input('Your guess? ("?" for hint, "!" to quit) ').lower()
   111	
   112	    if new_guess == '!':
   113	        bail('Better luck next time, loser.')
   114	    elif new_guess == '?':
   115	        new_guess = random.choice([x for x in word if x not in guessed])
   116	        num_misses += 1
   117	
   118	    if not re.match('^[a-z]$', new_guess):
   119	        print('"{}" is not a letter'.format(new_guess))
   120	        num_misses += 1
   121	    elif new_guess in prev_guesses:
   122	        print('You already guessed that')
   123	    elif new_guess in word:
   124	        prev_guesses.add(new_guess)
   125	        last_pos = 0
   126	        while True:
   127	            pos = word.find(new_guess, last_pos)
   128	            if pos < 0:
   129	                break
   130	            elif pos >= 0:
   131	                guessed[pos] = new_guess
   132	                last_pos = pos + 1
   133	    else:
   134	        num_misses += 1
   135	
   136	    play({
   137	        'word': word,
   138	        'guessed': guessed,
   139	        'num_misses': num_misses,
   140	        'prev_guesses': prev_guesses,
   141	        'max_misses': max_misses
   142	    })
   143	
   144	
   145	# --------------------------------------------------
   146	if __name__ == '__main__':
   147	    main()
````

\pagebreak

# Chapter 29

# Markov Chain

Write a Python program called `markov.py` that takes one or more text files as positional arguments for training. Use the `-n|--num_words` argument (default `2`) to find clusters of words and the words that follow them, e.g., in "The Bustle" by Emily Dickinson:

    The bustle in a house
    The morning after death
    Is solemnest of industries
    Enacted upon earth,—

    The sweeping up the heart,
    And putting love away
    We shall not want to use again
    Until eternity.

If `n=1`, then we find that "The" can be followed by "bustle," "morning," and "sweeping. There is a "the" followed by "heart," but we're not going to alter the text in any way, including removing punctuation, so just use `str.split` on the text to break up the words. 

To begin your text, choose a random word (or words) that begin with an uppercase letter. Then randomly select the next word in the chain, keep track of the floating window of the `-n` words, and keep selecting the next words until you have matched or exceeded the `-l|--length` argument of the number of characters (default 500) to emit at which point you should stop when you find a word that terminates with `.`, `!`, or `?`.

If you use `str.split` to get the words from the training text, you'll be removing any newlines from the text, so use a `-w|--text_width` argument (default 70) to introduce newlines in the output before the text exceeds that number of characters on the line.

Because of the use of randomness, you should include a `-s|--seed` argument (default `None`) to pass to `random.seed`.

Occassionally you may chose a path that terminates. That is, in selecting the next word, you may find there is no next-next word. In that case, just exit the program.

My implementation includes a `-d|--debug` option that will write a `.log` file so you can inspect my data structures and logic as you write your own version.

You should find many diverse texts and use them all as training files with varying numbers for `-n` to see how the texts will be mixed. The results are endlessly entertaining.

````
$ ./markov.py
usage: markov.py [-h] [-l int] [-n int] [-s int] [-w int] [-d] FILE [FILE ...]
markov.py: error: the following arguments are required: FILE
$ ./markov.py -h
usage: markov.py [-h] [-l int] [-n int] [-s int] [-w int] [-d] FILE [FILE ...]

Markov Chain

positional arguments:
  FILE                  Training file(s)

optional arguments:
  -h, --help            show this help message and exit
  -l int, --length int  Output length (characters) (default: 500)
  -n int, --num_words int
                        Number of words (default: 2)
  -s int, --seed int    Random seed (default: None)
  -w int, --text_width int
                        Max number of characters per line (default: 70)
  -d, --debug           Debug to ".log" (default: False)
$ ./markov.py ../inputs/const.txt
Discoveries; To constitute Tribunals inferior to the seat of the
Senate and House of Representatives shall have been committed, which
district shall have the Qualifications requisite for Electors of the
sixth Year, so that one third may be imposed on such Importation, not
exceeding three on the Journal. Neither House, during the Time of
Adjournment, he may require it. No Bill of Attainder or ex post facto
Law shall be established by Law: but the Party convicted shall
nevertheless be liable and subject to their Consideration such
Measures as he shall nominate, and by and with the Advice and Consent
of the government of the United States under this Constitution, or,
on the List the said Office, the same State claiming Lands under
Grants of different States; between Citizens of each shall constitute
a Quorum to do Business; but a smaller number may adjourn from day to
day, and may be included within this Union, according to their
Consideration such Measures as he shall nominate, and by and with the
Advice and Consent of the United States.
````

\pagebreak

# markov_chain Solution

````
     1	#!/usr/bin/env python3
     2	"""Markov Chain"""
     3	
     4	import argparse
     5	import logging
     6	import os
     7	import random
     8	import string
     9	import sys
    10	from pprint import pprint as pp
    11	from collections import defaultdict
    12	
    13	
    14	# --------------------------------------------------
    15	def get_args():
    16	    """Get command-line arguments"""
    17	
    18	    parser = argparse.ArgumentParser(
    19	        description='Markov Chain',
    20	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    21	
    22	    parser.add_argument('training',
    23	                        metavar='FILE',
    24	                        nargs='+',
    25	                        type=argparse.FileType('r'),
    26	                        help='Training file(s)')
    27	
    28	    parser.add_argument('-l',
    29	                        '--length',
    30	                        help='Output length (characters)',
    31	                        metavar='int',
    32	                        type=int,
    33	                        default=500)
    34	
    35	    parser.add_argument('-n',
    36	                        '--num_words',
    37	                        help='Number of words',
    38	                        metavar='int',
    39	                        type=int,
    40	                        default=2)
    41	
    42	    parser.add_argument('-s',
    43	                        '--seed',
    44	                        help='Random seed',
    45	                        metavar='int',
    46	                        type=int,
    47	                        default=None)
    48	
    49	    parser.add_argument('-w',
    50	                        '--text_width',
    51	                        help='Max number of characters per line',
    52	                        metavar='int',
    53	                        type=int,
    54	                        default=70)
    55	
    56	    parser.add_argument('-d',
    57	                        '--debug',
    58	                        help='Debug to ".log"',
    59	                        action='store_true')
    60	
    61	    return parser.parse_args()
    62	
    63	
    64	# --------------------------------------------------
    65	def main():
    66	    """Make a jazz noise here"""
    67	
    68	    args = get_args()
    69	    num_words = args.num_words
    70	    char_max = args.length
    71	    text_width = args.text_width
    72	
    73	    random.seed(args.seed)
    74	
    75	    logging.basicConfig(
    76	        filename='.log',
    77	        filemode='w',
    78	        level=logging.DEBUG if args.debug else logging.CRITICAL)
    79	
    80	    all_words = defaultdict(list)
    81	    for fh in args.training:
    82	        words = fh.read().split()
    83	
    84	        for i in range(0, len(words) - num_words):
    85	            l = words[i:i + num_words + 1]
    86	            all_words[tuple(l[:-1])].append(l[-1])
    87	
    88	    logging.debug('all words = {}'.format(all_words))
    89	
    90	    prev = ''
    91	    while not prev:
    92	        start = random.choice(
    93	            list(
    94	                filter(lambda w: w[0][0] in string.ascii_uppercase,
    95	                       all_words.keys())))
    96	        if all_words[start]:
    97	            prev = start
    98	
    99	    logging.debug('Starting with "{}"'.format(prev))
   100	
   101	    p = ' '.join(prev)
   102	    char_count = len(p)
   103	    print(p, end=' ')
   104	    line_width = char_count
   105	
   106	    while True:
   107	        if not prev in all_words: break
   108	
   109	        new_word = random.choice(all_words[prev])
   110	        new_len = len(new_word) + 1
   111	        logging.debug('chose = "{}" from {}'.format(new_word, all_words[prev]))
   112	
   113	        if line_width + new_len > text_width:
   114	            print()
   115	            line_width = new_len
   116	        else:
   117	            line_width += new_len
   118	
   119	        char_count += new_len
   120	        print(new_word, end=' ')
   121	        if char_count >= char_max and new_word[-1] in '.!?': break
   122	        prev = prev[1:] + (new_word, )
   123	
   124	    logging.debug('Finished')
   125	    print()
   126	
   127	
   128	# --------------------------------------------------
   129	if __name__ == '__main__':
   130	    main()
````

\pagebreak

# Chapter 30

# Morse Encoder/Decoder

Write a Python program called `morse.py` that will encrypt/decrypt text to/from Morse code. The program should expect a single positional argument which is either the name of a file to read for the input or the character `-` to indicate reading from STDIN. The program should also take a `-c|--coding` option to indicate use of the `itu` or standard `morse` tables, `-o|--outfile` for writing the output (default STDOUT), and a `-d|--decode` flag to indicate that the action is to decode the input (the default is to encode it).

````
$ ./morse.py
usage: morse.py [-h] [-c str] [-o str] [-d] [-D] FILE
morse.py: error: the following arguments are required: FILE
$ ./morse.py -h
usage: morse.py [-h] [-c str] [-o str] [-d] [-D] FILE

Encode and decode text/Morse

positional arguments:
  FILE                  Input file or "-" for stdin

optional arguments:
  -h, --help            show this help message and exit
  -c str, --coding str  Coding version (default: itu)
  -o str, --outfile str
                        Output file (default: None)
  -d, --decode          Decode message from Morse to text (default: False)
  -D, --debug           Debug (default: False)
$ ./morse.py ../inputs/fox.txt
- .... .  --.- ..- .. -.-. -.-  -... .-. --- .-- -.  ..-. --- -..-  .--- ..- -- .--. ...  --- ...- . .-.  - .... .  .-.. .- --.. -.--  -.. --- --. .-.-.-
[cholla@~/work/python/playful_python/morse]$ ./morse.py ../inputs/fox.txt | ./morse.py -d -
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
````

\pagebreak

# morse Solution

````
     1	#!/usr/bin/env python3
     2	"""Morse en/decoder"""
     3	
     4	import argparse
     5	import logging
     6	import random
     7	import re
     8	import string
     9	import sys
    10	
    11	
    12	# --------------------------------------------------
    13	def get_args():
    14	    """Get command-line arguments"""
    15	
    16	    parser = argparse.ArgumentParser(
    17	        description='Encode and decode text/Morse',
    18	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    19	
    20	    parser.add_argument('input',
    21	                        metavar='FILE',
    22	                        help='Input file or "-" for stdin')
    23	
    24	    parser.add_argument('-c',
    25	                        '--coding',
    26	                        help='Coding version',
    27	                        metavar='str',
    28	                        type=str,
    29	                        choices=['itu', 'morse'],
    30	                        default='itu')
    31	
    32	    parser.add_argument('-o',
    33	                        '--outfile',
    34	                        help='Output file',
    35	                        metavar='str',
    36	                        type=str,
    37	                        default=None)
    38	
    39	    parser.add_argument('-d',
    40	                        '--decode',
    41	                        help='Decode message from Morse to text',
    42	                        action='store_true')
    43	
    44	    parser.add_argument('-D', '--debug', help='Debug', action='store_true')
    45	
    46	    return parser.parse_args()
    47	
    48	
    49	# --------------------------------------------------
    50	def encode_word(word, table):
    51	    """Encode word using given table"""
    52	
    53	    coded = []
    54	    for char in word.upper():
    55	        logging.debug(char)
    56	        if char != ' ' and char in table:
    57	            coded.append(table[char])
    58	
    59	    encoded = ' '.join(coded)
    60	    logging.debug('endoding "{}" to "{}"'.format(word, encoded))
    61	
    62	    return encoded
    63	
    64	
    65	# --------------------------------------------------
    66	def decode_word(encoded, table):
    67	    """Decode word using given table"""
    68	
    69	    decoded = []
    70	    for code in encoded.split(' '):
    71	        if code in table:
    72	            decoded.append(table[code])
    73	
    74	    word = ''.join(decoded)
    75	    logging.debug('dedoding "{}" to "{}"'.format(encoded, word))
    76	
    77	    return word
    78	
    79	
    80	# --------------------------------------------------
    81	def test_encode_word():
    82	    """Test Encoding"""
    83	
    84	    assert encode_word('sos', ENCODE_ITU) == '... --- ...'
    85	    assert encode_word('sos', ENCODE_MORSE) == '... .,. ...'
    86	
    87	
    88	# --------------------------------------------------
    89	def test_decode_word():
    90	    """Test Decoding"""
    91	
    92	    assert decode_word('... --- ...', DECODE_ITU) == 'SOS'
    93	    assert decode_word('... .,. ...', DECODE_MORSE) == 'SOS'
    94	
    95	
    96	# --------------------------------------------------
    97	def test_roundtrip():
    98	    """Test En/decoding"""
    99	
   100	    random_str = lambda: ''.join(random.sample(string.ascii_lowercase, k=10))
   101	    for _ in range(10):
   102	        word = random_str()
   103	        for encode_tbl, decode_tbl in [(ENCODE_ITU, DECODE_ITU),
   104	                                       (ENCODE_MORSE, DECODE_MORSE)]:
   105	
   106	            assert word.upper() == decode_word(encode_word(word, encode_tbl),
   107	                                               decode_tbl)
   108	
   109	
   110	# --------------------------------------------------
   111	def main():
   112	    """Make a jazz noise here"""
   113	    args = get_args()
   114	    action = 'decode' if args.decode else 'encode'
   115	    output = open(args.outfile, 'wt') if args.outfile else sys.stdout
   116	    source = sys.stdin if args.input == '-' else open(args.input)
   117	
   118	    coding_table = ''
   119	    if args.coding == 'itu':
   120	        coding_table = ENCODE_ITU if action == 'encode' else DECODE_ITU
   121	    else:
   122	        coding_table = ENCODE_MORSE if action == 'encode' else DECODE_MORSE
   123	
   124	    logging.basicConfig(
   125	        filename='.log',
   126	        filemode='w',
   127	        level=logging.DEBUG if args.debug else logging.CRITICAL)
   128	
   129	    word_split = r'\s+' if action == 'encode' else r'\s{2}'
   130	
   131	    for line in source:
   132	        for word in re.split(word_split, line):
   133	            if action == 'encode':
   134	                print(encode_word(word, coding_table), end='  ')
   135	            else:
   136	                print(decode_word(word, coding_table), end=' ')
   137	        print()
   138	
   139	
   140	# --------------------------------------------------
   141	def invert_dict(d):
   142	    """Invert a dictionary's key/value"""
   143	
   144	    #return dict(map(lambda t: list(reversed(t)), d.items()))
   145	    return dict([(v, k) for k, v in d.items()])
   146	
   147	
   148	# --------------------------------------------------
   149	# GLOBALS
   150	
   151	ENCODE_ITU = {
   152	    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
   153	    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
   154	    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
   155	    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
   156	    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3':
   157	    '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8':
   158	    '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!':
   159	    '-.-.--', '&': '.-...', ';': '-.-.-.', ':': '---...', "'": '.----.', '/':
   160	    '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
   161	}
   162	
   163	ENCODE_MORSE = {
   164	    'A': '.-', 'B': '-...', 'C': '..,.', 'D': '-..', 'E': '.', 'F': '.-.', 'G':
   165	    '--.', 'H': '....', 'I': '..', 'J': '-.-.', 'K': '-.-', 'L': '+', 'M':
   166	    '--', 'N': '-.', 'O': '.,.', 'P': '.....', 'Q': '..-.', 'R': '.,..', 'S':
   167	    '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '.-..', 'Y':
   168	    '..,..', 'Z': '...,.', '0': '+++++', '1': '.--.', '2': '..-..', '3':
   169	    '...-.', '4': '....-', '5': '---', '6': '......', '7': '--..', '8':
   170	    '-....', '9': '-..-', '.': '..--..', ',': '.-.-', '?': '-..-.', '!':
   171	    '---.', '&': '.,...', ';': '...,..', ':': '-.-,.,.', "'": '..-.,.-..', '/':
   172	    '..-,-', '-': '....,.-..', '(': '.....,.-..', ')': '.....,..,..',
   173	}
   174	
   175	DECODE_ITU = invert_dict(ENCODE_ITU)
   176	DECODE_MORSE = invert_dict(ENCODE_MORSE)
   177	
   178	# --------------------------------------------------
   179	if __name__ == '__main__':
   180	    main()
````

\pagebreak

# Chapter 31

# ROT13 (Rotate 13)

Write a Python program called `rot13.py` that will encrypt/decrypt input text by shifting the text by a given `-s|--shift` argument or will move each character halfway through the alphabet, e.g., "a" becomes "n," "b" becomes "o," etc. The text to rotate should be provided as a single positional argument to your program and can either be a text file, text on the command line, or `-` to indicate STDIN so that you can round-trip data through your program to ensure you are encrypting and decrypting properly.

The way I approached the solution is to think of adding time. If it's 8 in the morning and I want to know the time in 6 hours on a 12-hour (not military/24-hour) clock, I need to think in terms of 12 when the clock rolls over from AM to PM. To do that, I need to know the remainder of dividing by 12, which is given by the modulus `%` operator:

````
>>> now = 8
>>> (now + 6) % 12
2
````

And 6 hours from 8AM is, indeed, 2PM.

Similarly if I want to know how many hours (in decimal) are a particular number of minutes, I need to mod by 60:

````
>>> minutes = 90
>>> int(minutes / 60) + (minutes % 60) / 60
1.5
>>> minutes = 204
>>> int(minutes / 60) + (minutes % 60) / 60
3.4
````

If you `import string`, you can see all the lower/uppercase letters

````
>>> import string
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
````

So I think about "rot13" like adding 13 (or some other shift interval) to the position of the letter in the list and modding by the length of the list to wrap it around. If the shift is 13 and we are at "a" and want to know what the letter 13 way is, we can use `pos` to find "a" and add 13 to that:

````
>>> lcase = list(string.ascii_lowercase)
>>> lcase.index('a')
0
>>> lcase[lcase.index('a') + 13]
'n'
````

But if we want to know the value for something after the 13th letter in our list, we are in trouble!

````
>>> lcase[lcase.index('x') + 13]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
````

`%` to the rescue!

````
>>> lcase[(lcase.index('x') + 13) % len(lcase)]
'k'
````

It's not necessary in this algorithm to shift by any particular number. 13 is special because it's halfway through the alphabet, but we could shift by just 2 or 5 characters. If we want to round-trip our text, it's necessary to shift in the opposite direction on the second half of the trip, so be sure to use the negative value there!

````
$ ./rot13.py
usage: rot13.py [-h] [-s int] str
rot13.py: error: the following arguments are required: str
$ ./rot13.py -h
usage: rot13.py [-h] [-s int] str

Argparse Python script

positional arguments:
  str                  Input text, file, or "-" for STDIN

optional arguments:
  -h, --help           show this help message and exit
  -s int, --shift int  Shift arg (default: 0)
$ ./rot13.py AbCd
NoPq
$ ./rot13.py AbCd -s 2
CdEf
$ ./rot13.py fox.txt
Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
$ ./rot13.py fox.txt | ./rot13.py -
The quick brown fox jumps over the lazy dog.
$ ./rot13.py -s 3 fox.txt | ./rot13.py -s -3 -
The quick brown fox jumps over the lazy dog.
````

\pagebreak

# rot13 Solution

````
     1	#!/usr/bin/env python3
     2	
     3	import argparse
     4	import os
     5	import re
     6	import string
     7	import sys
     8	
     9	
    10	# --------------------------------------------------
    11	def get_args():
    12	    """get command-line arguments"""
    13	    parser = argparse.ArgumentParser(
    14	        description='ROT13 encryption',
    15	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    16	
    17	    parser.add_argument('text',
    18	                        metavar='str',
    19	                        help='Input text, file, or "-" for STDIN')
    20	
    21	    parser.add_argument('-s',
    22	                        '--shift',
    23	                        help='Shift arg',
    24	                        metavar='int',
    25	                        type=int,
    26	                        default=0)
    27	
    28	    return parser.parse_args()
    29	
    30	
    31	# --------------------------------------------------
    32	def main():
    33	    """Make a jazz noise here"""
    34	    args = get_args()
    35	    text = args.text
    36	
    37	    if text == '-':
    38	        text = sys.stdin.read()
    39	    elif os.path.isfile(text):
    40	        text = open(text).read()
    41	
    42	    lcase = list(string.ascii_lowercase)
    43	    ucase = list(string.ascii_uppercase)
    44	    num_lcase = len(lcase)
    45	    num_ucase = len(ucase)
    46	    lcase_shift = args.shift or int(num_lcase / 2)
    47	    ucase_shift = args.shift or int(num_ucase / 2)
    48	
    49	    def rot13(char):
    50	        if char in lcase:
    51	            pos = lcase.index(char)
    52	            rot = (pos + lcase_shift) % num_lcase
    53	            return lcase[rot]
    54	        elif char in ucase:
    55	            pos = ucase.index(char)
    56	            rot = (pos + ucase_shift) % num_ucase
    57	            return ucase[rot]
    58	        else:
    59	            return char
    60	
    61	    print(''.join(map(rot13, text)).rstrip())
    62	
    63	
    64	# --------------------------------------------------
    65	if __name__ == '__main__':
    66	    main()
````

\pagebreak

