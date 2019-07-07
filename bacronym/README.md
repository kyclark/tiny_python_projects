# Bacronym

Write a Python program called `bacronym.py` that takes a string like "FBI" and retrofits some `-n|--num` (default `5`) of acronyms by reading a `-w|--wordlist` argument (default `/usr/share/dict/words`), skipping over words to `-e|--exclude` (default `a, an, the`) and randomly selecting words that start with each of the letters. Be sure to include a `-s|--seed` argument (default `None`) to pass to `random.seed` for the test suite.

If provided the `-h|--help` flags or no arguments, the program should print a usage:

````
$ ./bacronym.py
usage: bacronym.py [-h] [-n NUM] [-w STR] [-x STR [STR ...]] [-s INT] STR
bacronym.py: error: the following arguments are required: STR
$ ./bacronym.py -h
usage: bacronym.py [-h] [-n NUM] [-w STR] [-x STR [STR ...]] [-s INT] STR

Explain acronyms

positional arguments:
  STR                   Acronym

optional arguments:
  -h, --help            show this help message and exit
  -n NUM, --num NUM     Maximum number of definitions (default: 5)
  -w STR, --wordlist STR
                        Dictionary/word file (default: /usr/share/dict/words)
  -x STR [STR ...], --exclude STR [STR ...]
                        List of words to exclude (default: ['a', 'an', 'the'])
  -s INT, --seed INT    Random seed (default: None)
````

Because I'm including a `--seed` argumment, you should get this exact output if using the same `--wordlist`:

````
$ ./bacronym.py -s 1 FBI
FBI =
 - Fecundity Brokage Imitant
 - Figureless Basketmaking Ismailite
 - Frumpery Bonedog Irregardless
 - Foxily Blastomyces Inedited
 - Fastland Bouncingly Idiospasm
````

The program should create errors and usage for `--num` less than 1:

````
$ ./bacronym.py -n -3 AAA
usage: bacronym.py [-h] [-n NUM] [-w STR] [-x STR [STR ...]] [-s INT] STR
bacronym.py: error: --num "-3" must be > 0
````

And for a bad `--wordlist`:

````
$ ./bacronym.py -w mnvdf AAA
usage: bacronym.py [-h] [-n NUM] [-w STR] [-x STR [STR ...]] [-s INT] STR
bacronym.py: error: argument -w/--wordlist: can't open 'mnvdf': \
[Errno 2] No such file or directory: 'mnvdf'
````

The acronym must be composed entirely of letters:

````
$ ./bacronym.py 666
usage: bacronym.py [-h] [-n NUM] [-w STR] [-x STR [STR ...]] [-s INT] STR
bacronym.py: error: Acronym "666" must be >1 in length, only use letters
````

And be greater than 1 character in length:

````
$ ./bacronym.py A
usage: bacronym.py [-h] [-n NUM] [-w STR] [-x STR [STR ...]] [-s INT] STR
bacronym.py: error: Acronym "A" must be >1 in length, only use letters
````

Hints:

* See how much error checking you can put into the `get_args` function and use `parser.error` to throw the errors
* The `--wordlist` need not be a system dictionary file with one lower-case word on each line. Assume that you can read any file with many words on each line and that might include punctuation. I suggest you use a regualar expression to remove anything that is not an alphabet character with `re.sub('[^a-z]', '')`. Be sure that words are only represented once in your list.
* In my version, I write two important functions: one (`group_words`) that reads the wordlist and returns a grouping of words by their first letter, and another (`make_definitions`) that produces plausible definitions from that grouping of words by letters for a given acronym. I place the following test functions into my program and run `pytest` to verify that the functions work properly.

````
def test_group_words():
    """Test group_words()"""

    words = io.StringIO('apple, "BANANA," The Coconut! Berry; A cabbage.')
    stop = 'a an the'.split()
    words_by_letter = group_words(words, stop)
    assert words_by_letter['a'] == ['apple']
    assert words_by_letter['b'] == ['banana', 'berry']
    assert words_by_letter['c'] == ['coconut', 'cabbage']
    assert 't' not in words_by_letter

def test_make_definitions():
    """Test make_definitions()"""

    words = {
        'a': ['apple'],
        'b': ['banana', 'berry'],
        'c': ['coconut', 'cabbage']
    }

    random.seed(1)
    assert make_definitions('ABC', words) == ['Apple Banana Cabbage']
    random.seed(2)
    assert make_definitions('ABC', words) == ['Apple Banana Coconut']
    random.seed(3)
    assert make_definitions('AAA', words) == ['Apple Apple Apple']
    random.seed(4)
    assert make_definitions('YYZ', words) == ['? ? ?']
    random.seed(None)
````