# Soundex Rhymer

Write a Python program called `rhymer.py` that uses the Soundex algorithm/module (https://en.wikipedia.org/wiki/Soundex, https://pypi.org/project/soundex/) to find words that rhyme with a given input word. When comparing words, it would be best to discount any leading consonants, e.g., the words "listen" and "glisten" rhyme but only if you compare the "isten" part. The program should take an optional `-w|--wordlist` argument (default "/usr/share/dict/words") for the comparisons.

````
$ ./rhymer.py
usage: rhymer.py [-h] [-w str] str
rhymer.py: error: the following arguments are required: str
[cholla@~/work/python/playful_python/soundex-rhymer]$ ./rhymer.py -h
usage: rhymer.py [-h] [-w str] str

Use Soundex to find rhyming words

positional arguments:
  str                   Word

optional arguments:
  -h, --help            show this help message and exit
  -w str, --wordlist str
                        Wordlist (default: /usr/share/dict/words)
$ ./rhymer.py orange | head
boring
borning
boronic
borrowing
chloranemic
chlorinize
chlorinous
chorionic
choromanic
clowring
````
