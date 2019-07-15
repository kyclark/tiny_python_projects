# Soundex Rhymer

> "What words rhyme with 'buried alive'?" -- TMBG

Write a Python program called `rhymer.py` that uses the Soundex algorithm/module to find words that rhyme with a given input word. When comparing words, you sometimes want to discount any leading consonants, e.g., the words "listen" and "glisten" rhyme but only if you compare the "isten" part, so the program should have an optional flag `-s|--stem` to indicate that the given word and the words you compare should both be trimmed to the "stem". The program should take an optional `-w|--wordlist` argument (default `/usr/share/dict/words`) for the comparisons and should respond, as always, to `-h|--help` for usage.

For more background on the Soundex algorithm, I recommend the Wikipedia page and the PyPi module documentation for `soundex`.

````
$ ./rhymer.py -h
usage: rhymer.py [-h] [-w str] [-s] str

Find rhyming words using the Soundex

positional arguments:
  str                   Word

optional arguments:
  -h, --help            show this help message and exit
  -w str, --wordlist str
                        Wordlist (default: /usr/share/dict/words)
  -s, --stem            Stem the word (remove starting consonants (default:
                        False)
````

With my words list, I can find 37 words that rhyme with "listen" and 161 words that rhyme with the "isten" part:

````
$ ./rhymer.py listen | wc -l
      37
$ ./rhymer.py -s listen | wc -l
     161
````

I can verify that "glisten" only turns up when stemming is on:	   

````
$ ./rhymer.py listen | grep glisten
$ ./rhymer.py -s listen | grep glisten
glisten
````

Here is a sample of the words that my version finds:

````
$ ./rhymer.py listen | head -3
lackeydom
lactam
lactation
````

This program could be useful in creating custom input for the Gashlycrumb program.

Hints:

* You need to be sure that the given `word` actually has a vowel. 
* If you are going to remove consonants from the beginning of a string, it might be easiest to find a regular expression to find things that are not vowels (because there are fewer of them to list).
* Another way to remove leading consonants would be to manually find the position of the first vowel in the string and then use a list slice on the given word to take the substring from that position to the end
* I suggest you use the `soundex` module 

## Testing the stemmer

I found the stemming part somewhat challenging, especially as I explored three different methods. I added the following test inside my `rhymer.py`:

````
def test_stemmer():
    """test stemmer"""

    assert stemmer('listen', True) == 'isten'
    assert stemmer('listen', False) == 'listen'
    assert stemmer('chair', True) == 'air'
    assert stemmer('chair', False) == 'chair'
    assert stemmer('apple', True) == 'apple'
    assert stemmer('apple', False) == 'apple'
    assert stemmer('xxxxxx', True) == 'xxxxxx'
    assert stemmer('xxxxxx', False) == 'xxxxxx'

    assert stemmer('LISTEN', True) == 'ISTEN'
    assert stemmer('LISTEN', False) == 'LISTEN'
    assert stemmer('CHAIR', True) == 'AIR'
    assert stemmer('CHAIR', False) == 'CHAIR'
    assert stemmer('APPLE', True) == 'APPLE'
    assert stemmer('APPLE', False) == 'APPLE'
    assert stemmer('XXXXXX', True) == 'XXXXXX'
    assert stemmer('XXXXXX', False) == 'XXXXXX'
````

And them I modified `make test` to include `rhymer.py` in the list of files to test. The `pytest` module looks for any function name that starts with `test_` and runs them. The `assert` will halt execution of the program if the test fails.

Some of the words in my system dictionary don't have vowels, so some of methods that assumed the presence of a vowel failed. Writing a test just for this one function really helped me find errors in my code.