# Hamming Chain

Write a Python program called `chain.py` that takes a starting word as a positional argument and searches a `-w|--wordlist` argument (default `/usr/local/share/dict`) for words no more than `-d|--max_distance` Hamming distance for some number of `-i|--iteration` (default `20`). Be sure to accept a `-s|--seed` for `random.seed`. 

If the given word is not found in the word list, exit with an error and message. While searching for the next word in the chain, be sure not to repeat any words previously found or you might just go in circles! If you fail to find any new words before the end of the iterations, exit with an error and message as such.

````
$ ./chain.py
usage: chain.py [-h] [-w FILE] [-d int] [-i int] [-s int] [-D] word
chain.py: error: the following arguments are required: word
$ ./chain.py -h
usage: chain.py [-h] [-w FILE] [-d int] [-i int] [-s int] [-D] word

Hamming chain

positional arguments:
  word                  Starting word

optional arguments:
  -h, --help            show this help message and exit
  -w FILE, --wordlist FILE
                        File input (default: /usr/share/dict/words)
  -d int, --max_distance int
                        Maximum Hamming distance (default: 1)
  -i int, --iterations int
                        Random seed (default: 20)
  -s int, --seed int    Random seed (default: None)
  -D, --debug           Debug (default: False)
$ ./chain.py foobar
Unknown word "foobar"
$ ./chain.py -s 3 bike
bike ->
  1: boke
  2: yoke
  3: moke
  4: mome
  5: Rome
  6: dome
  7: Kome
  8: come
  9: coze
 10: cope
 11: dope
 12: doper
 13: doser
 14: loser
 15: poser
 16: power
 17: poker
 18: poler
 19: soler
 20: scler
$ ./chain.py -s 1 bicycle
bicycle ->
  1: bicycler
Failed to find more words!
$ ./chain.py -s 1 -d 2 bicycle
bicycle ->
  1: bicyclic
  2: bicyclism
  3: dicyclist
  4: bicyclist
Failed to find more words!
````
