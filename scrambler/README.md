# Scrambler

Write a Python program called `scrambler.py` that will take a single position positional argument that is text or a text file and then convert each word into a scrambled version. The scrambling should only work on words greater than 3 characters in length and should only scramble the letters in the middle, leaving the first and last characters unchanged. The program should take a `-s|--seed` argumen to pass to `random.seed`.

Cf. Typoglycemia https://www.dictionary.com/e/typoglycemia/

We'll need to use the same algorithm for scrambling the words. I used the `random.shuffle` method to mix up the letters in the middle, being sure that the word that gets created is not the same as the word that you are given. If the word is 3 characters or shorter, just return the word unchanged.

Another very tricky bit is that we want to scramble all the "words" on each line and leave everything that's not a "word" unchanged. We'll use a regular expression that looks for strings composed only of the characters a-z, A-Z, and the single quote so we can find words like `can't` or `Susie's`. Everything else will be consider not a word. Here is the regex you should use:

````
regex = re.compile(r"([a-zA-Z']+)")
````

Now feel free to pop this function into your code to split the text on that regular expression:

````
# --------------------------------------------------
def splitter(s, regex, fn=None):
    """
    Params:
    - a string to split on
    - a regular expression
    - an optional function to apply to the regex matches
    Returns:
    - the input string broken into the parts that match the
      regex (optionally transformed by the fn) and the bits
      in between the parts that match the regex
    """

    # Find all the parts of the string that match the regex
    # This will be a list like [(0, 2), (3, 8), (9, 12)]
    spans = [m.span() for m in regex.finditer(s)]

    # Flatten that into [0, 2, 3, 8, 9, 12]
    gaps = list(chain(*spans))

    # Bail if there is nothing
    if not gaps: return []

    # Make sure the list includes the start and end of the string
    if gaps[0] != 0: gaps.insert(0, 0)
    if gaps[-1] != len(s): gaps.append(len(s))

    # Find all the substrings, optionally apply the function if the
    # (start, stop) was in the list of spans matched by the regex.
    for i in range(0, len(gaps) - 1):
        start = gaps[i]
        stop = gaps[i + 1]
        substr = s[start:stop]
        if (start, stop) in spans and fn:
            substr = fn(substr)

        yield substr
````

And now you just need to write the function that will scramble any one word and pass that to the function a la:

````
for line in text.splitlines():
    print(''.join(splitter(line, regex, scramble)))
````

Here is how the program should perform:

````
$ ./scrambler.py
usage: scrambler.py [-h] [-s int] STR
scrambler.py: error: the following arguments are required: STR
$ ./scrambler.py -h
usage: scrambler.py [-h] [-s int] STR

Scramble the letters of words

positional arguments:
  STR                 Input text or file

optional arguments:
  -h, --help          show this help message and exit
  -s int, --seed int  Random seed (default: None)
$ ./scrambler.py -s 1 foobar
faobor
$ ./scrambler.py -s 1 "foobar bazquux"
faobor buuzaqx
$ ./scrambler.py -s 1 ../inputs/the-bustle.txt
The blutse in a hsoue
The monrnig atefr dteah
Is snleoemst of iusinedrts
Eatcend uopn etarh,--

The sewnpeig up the hreat,
And ptunitg lvoe aawy
We slahl not wnat to use agian
Utnil ertiteny.
````
