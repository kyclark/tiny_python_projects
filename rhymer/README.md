# Simple Rhymer

Write a Python program called `rhymer.py` that will create new words by removing the consonant(s) from the beginning (if any) of a given word and then create new words by prefixing the remainder with all the consonants and clusters that were not at the beginning. That is, prefix with all the consonants in the alphabet plus these clusters:

    bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp 
    st sw th tr tw wh wr sch scr shr sph spl spr squ str thr

If given no arguments or the `-h|--help` flags, print a usage statement:

````
$ ./rhymer.py
usage: rhymer.py [-h] str
rhymer.py: error: the following arguments are required: str
$ ./rhymer.py -h
usage: rhymer.py [-h] str

Make rhyming "words"

positional arguments:
  str         A word

optional arguments:
  -h, --help  show this help message and exit
````  
  
If the word starts with a vowel, use the word as-is:

````
$ ./rhymer.py apple | head -3
bapple
capple
dapple
````

If the word begins with any consonants, remove them and append all the prefixes above making sure not to include any prefixes that match what you removed:

````
$ ./rhymer.py take | head -3
bake
cake
dake
$ ./rhymer.py take | grep take
stake
````

If the word doesn't match one of the above conditions, e.g., it is entirely consonants, print a message that you cannot rhyme it.

````
$ ./rhymer.py RDNZL
Cannot rhyme "RDNZL"
````

Hints:

The heart of the program for me is the stemming of the word. Do you even need to stemp it? Not if it begins with a vowel, so how can you detect that? I ended up writing a function called `stemmer` and inserted this into my `rhymer.py`:

````
def test_stemmer():
    """Test the stemmer"""

    assert ('c', 'ake') == stemmer('cake')
    assert ('ch', 'air') == stemmer('chair')
    assert ('', 'apple') == stemmer('apple')
    assert stemmer('bbb') is None
````

If you notice the `make test` target also include `rhymer.py`:

````
pytest -xv rhymer.py test.py
````

I wrote my `stemmer(word)` to return a tuple of `(prefix, stem)` where `prefix` will be the empty string when the `word` starts with a vowel. If the word starts with a consonant and can be split, I return the two parts of the word e.g., `chair` become `('ch', 'air')`. Otherwise I return `None` to indicate a failure to communicate.

If you choose to do the same, you can add the `test_stemmer` to your program and  `pytest` will find any function with a name starting with `test_` to run. You can use this to verify that your `stemmer` does what you expect.