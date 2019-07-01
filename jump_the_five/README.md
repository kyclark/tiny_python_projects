# Jump the Five

!["When I get up, nothing gets me down." - D. L. Roth](images/jump.png)

Write a program called `jump.py` that will encode any number using "jump-the-five" algorithm that selects as a replacement for a given number one that is opposite on a US telephone pad if you jump over the 5. The numbers 5 and 0 will exchange with each other. So, "1" jumps the 5 to become "9," "6" jumps the 5 to become "4," "5" becomes "0," etc.

````
   1  2  3
   4  5  6
   7  8  9
   #  0  *
````

Print a usage statement for `-h|--help` or if there are no arguments.

````
$ ./jump.py
usage: jump.py [-h] str
jump.py: error: the following arguments are required: str
$ ./jump.py -h
usage: jump.py [-h] str

Jump the Five

positional arguments:
  str         Input text

optional arguments:
  -h, --help  show this help message and exit
````

Your program should replace numbers *anywhere* in the input string:

````  
$ ./jump.py 555-1212
000-9898
$ ./jump.py 'Call 1-800-329-8044 today!'
Call 9-255-781-2566 today!
````

Hints: 

* The numbers can occur anywhere in the text, so I recommend you think of how you can process the input character-by-character. 
* To me, the most natural way to represent the subsitution table is in a `dict`.
* Read the documentation on Python's `str` class to see what you can do with a string. For instance, there is a `replace` method. Could you use that?
