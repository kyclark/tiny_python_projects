# Rummikub

Rummikub is a game played with tiles that are very similar to playing cards. There are 4 colors (blue, black, yellow, red) each of which has numbers 1-13 which gives you the standard 52-card "deck." The deck is duplicated so that there are a total of 104 tiles. At the beginning of the game, each player takes 14 tiles and then tries to form sets of tiles where:

1. Three or four tiles are the same number and all different colors
2. Three or more tiles are consecutive numbers all of the same color

Write a Python program called `rummikub.py` where you create the tiles using `B` for "blue," `K` for "black," `Y` for "yellow," and `R` for "red" crossed with the numeric values 1-13 so that tiles will be displayed like `R10`. Use `random.shuffle` to shuffle the tiles, and then use `random.sample` to draw 14 tiles. Find all possible combinations of 3 or more tiles that create sets as described above. 

The only option your program needs to accept is `-s|--seed` for the `random.seed`. As always, it should respond to `-h|--help` for usage.

````
$ ./rummikub.py -h
usage: rummikub.py [-h] [-s int]

Rummikub

optional arguments:
  -h, --help          show this help message and exit
  -s int, --seed int  Random seed (default: None)
````

If no sets are found, let the user know:

````
$ ./rummikub.py -s 0
Found no sets.
````

When printing out the sets, be sure to only print unique sets and that they are sorted by the color and then the numeric value. The test suite does not care what order the sets are printed. You should number the sets as you print them:

````
$ ./rummikub.py -s 1
  1: B3 K3 Y3
$ ./rummikub.py -s 5
  1: K11 K12 K13
  2: B2 B3 B4
  3: B3 B4 B5
  4: B2 K2 Y2
  5: B2 B3 B4 B5
````
