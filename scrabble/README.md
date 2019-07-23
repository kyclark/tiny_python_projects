# Scrabble From The Apple

Scrabble (tm) is a tile-based spelling game. Each tile has a single letter, and you draw 7 at random to start the game. The first person spells a word entirely using their own tiles, but ever other play in the game requires you to build off existing tiles on the board. We will write a program called `scrabble.py` that will find all the possible words you can make from all possible combinations a set of 7 Scrabble tiles using some other letter. That is, how many 3-letter words can you make using 2 of your own tiles plus an additional letter?

The program should respond to `-h|--help` for usage.

````
$ ./scrabble.py -h
usage: scrabble.py [-h] [-t str] [-l int] [-s int] [-w FILE]

Scrabble

optional arguments:
  -h, --help            show this help message and exit
  -t str, --tiles str   Input tiles (default: )
  -l int, --length int  Word length (default: 0)
  -s int, --seed int    Random seed (default: None)
  -w FILE, --wordlist FILE
                        Wordlist (default: /usr/share/dict/words)
````

As usual, your program needs to accept a `-s|--seed` argument to pass to `random.seed` for testing purpose. The `-w|--wordlist` is a standard dictionary file of English words but could be any text. All text should be converted to uppercase to match the letter on the tiles. The `-l|--length` option is to have your program only emit words of a particular length. 

Lastly there is a `-t|--tiles` option to give the tiles on the command line. This is to help you cheat. When this is not present, you should randomly sample 7 tiles. The letters are not evenly distributed among the tiles. You will need to encode these letter frequencies into your program:

* Blank: 2
* A: 9
* B: 2
* C: 2
* D: 4
* E: 12
* F: 2
* G: 3
* H: 2
* I: 9
* J: 1
* K: 1
* L: 4
* M: 2
* N: 6
* O: 8
* P: 2
* Q: 1
* R: 6
* S: 4
* T: 6
* U: 4
* V: 2
* W: 2
* X: 1
* Y: 2
* Z: 1

When run in normal mode, it should select and show the tiles, then work through all combinations of 1 to 7 letters of the tiles and find all 2- to 8-letter words in the `--wordlist` that could be formed.

````
$ ./scrabble.py -s 1 > out
Tiles = "LNSHRAU"
     1: L => AL
     2: L => AL
     3: L => EL
     4: L => LA
$ tail -5 out
  1831: AHLRSU => RASHFUL
  1832: AHNRSU => RHAMNUS
  1833: AHNRSU => UNSHARP
  1834: AHLNRSU => RUSHLAND
  1835: AHLNRSU => UNLASHER
````

If given a `--tiles` argument, be sure it's only 7 characters long:

````
$ ./scrabble.py -t ABCDEFGHIJ
usage: scrabble.py [-h] [-t str] [-l int] [-s int] [-w FILE]
scrabble.py: error: --tiles "ABCDEFGHIJ" can only be 7 characters
````