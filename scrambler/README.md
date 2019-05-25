# Scrambler

Write a Python program called `scrambler.py` that will take a single position positional argument that is text or a text file and then convert each word into a scrambled version. The scrambling should only work on words greater than 3 characters in length and should only scramble the letters in the middle, leaving the first and last characters unchanged. The program should take a `-s|--seed` argumen to pass to `random.seed`.

````
$ ./scrambler.py
usage: scrambler.py [-h] [-s int] STR
scrambler.py: error: the following arguments are required: STR
$ ./scrambler.py -h
usage: scrambler.py [-h] [-s int] STR

Scramble the letters of words

positional arguments:
  STR                 Input text or file

optional arguments:
  -h, --help          show this help message and exit
  -s int, --seed int  Random seed (default: None)
$ ./scrambler.py -s 1 foobar
faobor
$ ./scrambler.py -s 1 "foobar bazquux"
faobor buuzaqx
$ ./scrambler.py -s 1 ../inputs/the-bustle.txt
The blutse in a hsoue
The monrnig atefr dteah
Is snleoemst of iusinedrts
Eatcend upon e,athr—

The sewnpeig up the hater,
And pntutig lvoe aawy
We shall not wnat to use again
Until etnyreti.
````
