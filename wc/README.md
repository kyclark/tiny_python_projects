# Words Count

Write a Python program called `wc.py` that will emulate the venerable `wc` program in Unix that counts the lines, words, and characters in the given file arguments.

````
$ ./wc.py
usage: wc.py [-h] FILE [FILE ...]
wc.py: error: the following arguments are required: FILE
$ ./wc.py -h
usage: wc.py [-h] FILE [FILE ...]

Argparse Python script

positional arguments:
  FILE        Input file(s)

optional arguments:
  -h, --help  show this help message and exit
````



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