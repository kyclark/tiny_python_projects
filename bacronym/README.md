# BACRONYM

Write a Python program called `bacronym.py` that takes an string like "FBI" and retrofits some `-n|--number` (default 5) of acronyms by reading a `-w|--wordlist` argument (defualt "/usr/share/dict/words"), skipping over words to `-e|--exclude` (default "a, an, the") and randomly selecting words that start with each of the letters. Be sure to include a `-s|--seed` argument (default `None`) to pass to `random.seed` for the test suite.

````
$ ./bacronym.py
usage: bacronym.py [-h] [-n NUM] [-w STR] [-x STR] [-s INT] STR
bacronym.py: error: the following arguments are required: STR
$ ./bacronym.py -h
usage: bacronym.py [-h] [-n NUM] [-w STR] [-x STR] [-s INT] STR

Explain acronyms

positional arguments:
  STR                   Acronym

optional arguments:
  -h, --help            show this help message and exit
  -n NUM, --num NUM     Maximum number of definitions (default: 5)
  -w STR, --wordlist STR
                        Dictionary/word file (default: /usr/share/dict/words)
  -x STR, --exclude STR
                        List of words to exclude (default: a,an,the)
  -s INT, --seed INT    Random seed (default: None)
$ ./bacronym.py FBI -s 1
FBI =
 - Fecundity Brokage Imitant
 - Figureless Basketmaking Ismailite
 - Frumpery Bonedog Irregardless
 - Foxily Blastomyces Inedited
 - Fastland Bouncingly Idiospasm
````
