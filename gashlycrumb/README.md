# Gashlycrumb

Write a Python program called `gashlycrumb.py` that takes a letter of the alphabet as an argument and looks up the line in a `-f|--file` argument (default `gashlycrumb.txt`) and prints the line starting with that letter. It should generate usage with no arguments or for `-h|--help`:

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
````

You can see the structure of the default "gashlycrumb.txt" file:

````
$ head -3 gashlycrumb.txt
A is for Amy who fell down the stairs.
B is for Basil assaulted by bears.
C is for Clara who wasted away.
````

![D is for Donald, who died from gas.](images/donald.png)

You will use the first character of the line as a lookup value:

````
$ ./gashlycrumb.py a
A is for Amy who fell down the stairs.
$ ./gashlycrumb.py z
Z is for Zillah who drank too much gin.
````

If given a value that does not exist in the list of first characters on the lines from the input file (when searched with regard to case), you should print a message:

````
$ ./gashlycrumb.py 3
I do not know "3".
$ ./gashlycrumb.py CH
I do not know "CH".
````

If provided a `--file` argument that does not exist, your program should exit with an error and message:

````
$ ./gashlycrumb.py -f sdfl b
usage: gashlycrumb.py [-h] [-f str] str
gashlycrumb.py: error: argument -f/--file: can't open 'sdfl': \
[Errno 2] No such file or directory: 'sdfl'
````

Hints:

* To validate that the `--filename` is actually a readable file, look into using `argparse.FileType('r')` to describe the `type` of the `--file` argument so that `argparse` will do the check and create the error. 
* A dictionary is a natural data structure that you can use to associate some value like the letter "A" to some phrase like "A is for Amy who fell down the stairs."
* Once you have an open file handle to the `--filename` (which is exactly what you get when use `argparse.FileType`), you can `read` the file line-by-line with a `for` loop.
* Each line of text is a string. How can you get the first character of a string?
* Using that first character, how can you set the value of a `dict` to be the key and the line itself to be the value?
* Once you have constructed the dictionary of letters to lines, how can you check that the user's `letter` argument is `in` the dictionary?
* Can you solve this without a `dict`?