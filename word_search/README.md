# Word Search

Write a Python program called `search.py` that takes a file name as the single positional argument and finds the words hidden in the puzzle grid. 

````
$ ./search.py
usage: search.py [-h] FILE
search.py: error: the following arguments are required: FILE
$ ./search.py -h
usage: search.py [-h] FILE

Word search

positional arguments:
  FILE        The puzzle

optional arguments:
  -h, --help  show this help message and exit
````

If given a non-existent file, it should complain and exit with a non-zero status:

````
$ ./search.py lkdfak
usage: search.py [-h] FILE
search.py: error: argument FILE: can't open 'lkdfak': [Errno 2] No such file or directory: 'lkdfak'
````

The format of the puzzle file will be a grid of letters followed by an empty line followed by a list of words to find delimited by newlines, e.g.:

````
$ cat puzzle06.txt
ABC
DEF
GHI

DH
````

If the input grid is uneven, the program should error out:

````
$ cat bad_grid.txt
ABC
DEFG
HIJ

XYZ
$ ./search.py bad_grid.txt
Uneven number of columns
````

The output should be the input puzzle with only the letters showing for the words that are found replacing all the other letters with `.` (a period):

````
$ ./search.py puzzle06.txt
...
D..
.H.
$ cat ice_cream.txt
YMTRLCHOCOLATE
ASKCARTESOOMET
PYVANILLASNOTE
MKDETDEACFANAA
CATNLINNAOCOOE
OKPOAAGODKEAET
ECULNCAEFOPLRN
DOTAEENORYWEEE
OCBOAWYOTTEOIE
COIEAAARTSAOAR
RNTTCRALETNIAG
EEGDUFOSNIOVLT
DAORYKCORUACGT
AEETUNOCOCTPES

COTTON CANDY
MAPLE WALNUT
PECAN
BANANA
TIGER TAIL
MOOSE TRACKS
COCONUT
ROCKY ROAD
GREEN TEA
FUDGE
REESES
CHOCOLATE
VANILLA
$ ./search.py ice_cream.txt
.....CHOCOLATE
.SKCARTESOOM..
.YVANILLA.N...
M.D.T..A..A..A
.A.N.IN...C..E
..P.AAG...E..T
...LNC.E..P.RN
...AE.N.R..E.E
..B..W.O.TE..E
......A.TSA..R
.......LET.I.G
.EGDUF.SN.O.L.
DAORYKCORU.C..
...TUNOCOCT...
````
