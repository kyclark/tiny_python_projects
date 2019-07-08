# Gibberish Generator

Write a Python program called `gibberish.py` that uses the Markov chain algorithm to generate new words from the words in a set of training files. The program should take one or more positional arguments which are files that you read, word-by-word, and note the options of letters after a given `-k|--kmer_size` (default `2`) grouping of letters. E.g., in the word "alabama" with `k=1`, the frequency table will look like:

````
a = l, b, m
l = a
b = a
m = a
````

That is, given this training set, if you started with `l` you could only choose an `a`, but if you have `a` then you could choose `l`, `b`, or `m`.

The program should generate `-n|--num_words` words (default `10`), each a random size between `k` + 2 and a `-m|--max_word` size (default `12`). Be sure to accept `-s|--seed` to pass to `random.seed`. My solution also takes a `-d|--debug` flag that will emit debug messages to `.log` for you to inspect.

If provided no arguments or the `-h|--help` flag, generate a usage:
 
````
$ ./gibberish.py
usage: gibberish.py [-h] [-n int] [-k int] [-m int] [-s int] [-d] FILE [FILE ...]
gibberish.py: error: the following arguments are required: FILE
$ ./gibberish.py -h
usage: gibberish.py [-h] [-n int] [-k int] [-m int] [-s int] [-d] FILE [FILE ...]

Markov chain for characters/words

positional arguments:
  FILE                  Training file(s)

optional arguments:
  -h, --help            show this help message and exit
  -n int, --num_words int
                        Number of words to generate (default: 10)
  -k int, --kmer_size int
                        Kmer size (default: 2)
  -m int, --max_word int
                        Max word length (default: 12)
  -s int, --seed int    Random seed (default: None)
  -d, --debug           Debug to ".log" (default: False)
````

Create new English words by training on a dictionary:

````
$ ./gibberish.py /usr/share/dict/words -s 1 -n 5
  1: salva
  2: xeroolizati
  3: upst
  4: azeconi
  5: woco
````

Create different words by training on the US Constitution:

````
$ ./gibberish.py ../inputs/const.txt -s 2 -k 3 -n 4
  1: lfare
  2: sachmentit
  3: such
  4: rcessadopti
```` 

Generate new names for boys:

```` 
$ ./gibberish.py -k 2 -n 6 ../inputs/1945-boys.txt
  1: marthomart
  2: danie
  3: muel
  4: osep
  5: tomandrenny
  6: alberber
````

Chose the best words and create definitions for them:

* yulcogicism: the study of Christmas gnostics
* umjamp: skateboarding trick
* callots: insignia of officers in Greek army
* urchenev: fungal growth found under cobblestones

## Kmers

To create the Markov chains, you'll need to read all the words from each file. Use `str.lower` to lowercase all the text and then remove any character that is not in the regular English alphabet (a-z). You'll need to extract "k-mers" or "n-grams" from each word. In the text "abcd," if `k=2` then the 2-mers are "ab," "bc," and "cd." If `k=3`, then the 3-mers are "abc" and "bcd." It may be helpful to know the number `n` of kmers `k` is proportional to the length `l` of the string `n = l - k + 1`. 

Consider writing a function `kmers(text, k=1)` that only extracts kmers from some text, and then add this function to your program:

````
def test_kmers():
    """Test kmers"""

    assert kmers('abcd') == list('abcd')
    assert kmers('abcd', 2) == ['ab', 'bc', 'cd']
    assert kmers('abcd', 3) == ['abc', 'bcd']
    assert kmers('abcd', 4) == ['abcd']
    assert kmers('abcd', 5) == []
````

Run your program with `pytest -v gibberish.py` and see if it passes.

## Chains

To create the Markov chains, you'll need to get all the kmers for `k+1` for all the words in all the texts. That is, if `k=3` you need to find all the 4-mers so that you can find the character *after* the 3-mers in the texts. For example, in the text "The quick brown fox jumps over the lazy dog.", we need to create a data structure that looks like this:

````
>>> from pprint import pprint as pp
>>> pp(chains)
{'bro': ['w'],
 'jum': ['p'],
 'laz': ['y'],
 'ove': ['r'],
 'qui': ['c'],
 'row': ['n'],
 'uic': ['k'],
 'ump': ['s']}
````

For every 3-mer, we need to know all the characters that follow each. Obviously this is not very exciting given the small size of the input text.

Consider writing a function `read_training(fhs, k=1)` that reads the input training files and returns a dictionary of kmer chains. Then add this function to test that is works properly:

````
def test_read_training():
    """Test read_training"""

    text = 'The quick brown fox jumps over the lazy dog.'

    expected3 = {
        'qui': ['c'],
        'uic': ['k'],
        'bro': ['w'],
        'row': ['n'],
        'jum': ['p'],
        'ump': ['s'],
        'ove': ['r'],
        'laz': ['y']
    }
    assert read_training([io.StringIO(text)], k=3) == expected3

    expected4 = {'quic': ['k'], 'brow': ['n'], 'jump': ['s']}
    assert read_training([io.StringIO(text)], k=4) == expected4
````

## Making new words

Once you have the chains of letters that follow each kmer, you need can use `random.choice` to find a starting kmer from the `keys` of your chain dictionary. Also use that function to select a length for your new word from the range of `k + 2` to the `args.max_word` (which defaults to `12`). Build up your new word by again using `random.choice` to select from the possibilities for the kmer which will change through each iteration.

That is, if you `k=3` and you start with the randomly selected kmer `ero`, you might get `n` as your next letter. On the next iteration of the loop, the `kmer` will be `ron` and you will look to see what letters follow that 3-mer. You might get `d`, and so the next time you would look for those letters following `ond`, and so forth. Continue until you've built a word that is the length you selected.

Hints: 

* Define the input files with `type=argparse.FileType('r')` so that `argparse` will validate the user provides readable files and then will `open` them for you.
* Consider using the `logging` module to print out debugging messages. Run the `solution.py` with the `-d` flag and then inspect the `.log` file.