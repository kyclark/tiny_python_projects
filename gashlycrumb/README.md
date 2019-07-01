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

You will use the first character of the line as a lookup value:

````
$ ./gashlycrumb.py a
A is for Amy who fell down the stairs.
$ ./gashlycrumb.py z
Z is for Zillah who drank too much gin.
````

If given a value that does not exist (when searched with regard to case), you should print a message:

````
$ ./gashlycrumb.py 3
I do not know "3".
````

You expect the positional argument to be exactly one character long. If it is not, exit with an error:

````
$ ./gashlycrumb.py CH
"CH" is not 1 character.
````

If you provide a `--file` argument that does not exist, you should exit with an error and message:

````
$ ./gashlycrumb.py -f sdfl b
usage: gashlycrumb.py [-h] [-f str] str
gashlycrumb.py: error: argument -f/--file: can't open 'sdfl': \
[Errno 2] No such file or directory: 'sdfl'
````

For those last two, look into using `argparse.FileType('r')` to describe the `type` of the `--file` argument so that `argparse` will do the check and create the error. For the length of the `letter` argument, look into using `parser.error`.

