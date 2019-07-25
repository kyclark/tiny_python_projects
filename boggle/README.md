# Boggle

Boggle (tm) is a game where you toss 16 dice, each 6-sided with a single letter on each side with the exception of "Qu." The goal of the game is to spell as many words as possible from the resulting 16 randomly chosen letters. 

The dice have the following composition:

    O  B  J  A  O  B
    F  F  S  K  A  P
    N  S  I  E  U  E
    E  G  H  W  E  N
    S  O  A  C  H  P
    T  T  R  E  Y  L
    R  N  Z  N  H  L
    R  E  V  L  Y  D
    T  U  I  C  M  O
    T  D  T  Y  S  I
    O  O  W  T  T  A
    N  A  E  A  E  G
    R  V  T  H  E  W
    L  X  E  D  R  I
    O  T  S  E  S  I
    U  QU H  M  N  I

Write a Python program called `boggle.py` that randomly chooses one side from each of the dice and displays the Boggle board with the chosen letters, e.g., with the seed `1` it should print:

````
B  A  N  H
S  E  N  L
O  Y  O  N
H  L  E  M
````

Then it should find all possible 3- to 16-letter words that can be spelled from these letters that are found in the `-w|--wordlist` file (default `/usr/share/dict/words`)( and print them to STDOUT or `-o|--output` file (default `None` or the empty string). Finally it should print a total of all the points for each word according to the following table:

````
3   1
4   1
5   2
6   3
7   5
8+  11
`````

Your program will also need to accept a `-s|--seed` option for `random.seed` and should print a usage for `-h|--help`:

````
$ ./boggle.py -h
usage: boggle.py [-h] [-s int] [-o FILE] [-w FILE]

Boggle

optional arguments:
  -h, --help            show this help message and exit
  -s int, --seed int    Random seed (default: None)
  -o FILE, --output FILE
                        Output words to file (default: None)
  -w FILE, --wordlist FILE
                        Wordlist (default: /usr/share/dict/words)
````

The initial board and the point total should always be printed to STDOUT. Only the words themselves should be optionally printed to the `--output` file.

````
$ ./boggle.py -s 1 -o out
B  A  N  H
S  E  N  L
O  Y  O  N
H  L  E  M
Total points = 2208
$ wc -l out
    1009 out
````

Optionally add a `-t|--timer` option (default 180 seconds) to wait for the user to write down their words before displaying the words your program finds.
