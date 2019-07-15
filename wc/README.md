# Words Count

Write a Python program called `wc.py` that will emulate the venerable `wc` program in Unix that counts the lines, words, and characters in the given file arguments. If run with the `-h|--help` flag, the program should print usage:

````
$ ./wc.py -h
usage: wc.py [-h] [FILE [FILE ...]]

Argparse Python script

positional arguments:
  FILE        Input file(s) (default: [<_io.TextIOWrapper name='<stdin>'
              mode='r' encoding='UTF-8'>])

optional arguments:
  -h, --help  show this help message and exit
````

Given a non-existent file, it should print an error message and exit with a non-zero exit value:

````
$ ./wc.py foo
usage: wc.py [-h] FILE [FILE ...]
wc.py: error: argument FILE: can't open 'foo': \
[Errno 2] No such file or directory: 'foo'
````

Given one or more valid files, it should print the number of lines, words, and characters, each in columns 8 characters wide, followed by a space and then the name of the file:

````
$ ./wc.py ../inputs/scarlet.txt
    7035   68061  396320 ../inputs/scarlet.txt
$ ./wc.py ../inputs/*.txt
    1000    1000    5840 ../inputs/1000.txt
     100     100     657 ../inputs/1945-boys.txt
     100     100     684 ../inputs/1945-girls.txt
     872    7652   45119 ../inputs/const.txt
    2476    7436   41743 ../inputs/dickinson.txt
       1       9      45 ../inputs/fox.txt
      25     278    1476 ../inputs/gettysburg.txt
      37      91     499 ../inputs/issa.txt
       9      51     248 ../inputs/nobody.txt
       1      16      65 ../inputs/now.txt
       6      71     413 ../inputs/preamble.txt
    7035   68061  396320 ../inputs/scarlet.txt
      17     118     661 ../inputs/sonnet-29.txt
       3       7      45 ../inputs/spiders.txt
       9      34     192 ../inputs/the-bustle.txt
   37842   48990  369949 ../inputs/uscities.txt
     176    1340    8685 ../inputs/usdeclar.txt
````

Given no positional arguments, it should read from STDIN:

````
$ ./wc.py < ../inputs/fox.txt
       1       9      45 <stdin>
$ cat ../inputs/fox.txt | ./wc.py
       1       9      45 <stdin>
````

Hints:

* Use the `argparse` to validate the input files and use `nargs='*'` to indicate zero or more positional arguments; use `sys.stdin` for the default.
* Compare the results of your version to the `wc` installed on your system. Note that not every Unix-like system has the same `wc`, so results may vary.