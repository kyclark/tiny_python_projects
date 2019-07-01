The first thing to check is that the given word contains a vowel which is simple enough if you use regular expressions. We'll include "y" for this purpose:

````
>>> re.search('[aeiouy]', 'YYZ', re.IGNORECASE) or 'Fail'
<re.Match object; span=(0, 1), match='Y'>
>>> re.search('[aeiouy]', 'bbbb', re.IGNORECASE) or 'Fail'
'Fail'
````

Another way that doesn't use a regex could use a list comprehension to iterate over character in the given word to see if it is `in` the `list` of vowels 'aeiouy':

````
>>> [c in 'aeiouy' for c in 'CAT'.lower()]
[False, True, False]
````

You can then ask if `any` of these tests are true:

````
>>> any([c in 'aeiouy' for c in 'CAT'.lower()])
True
>>> any([c in 'aeiouy' for c in 'BCD'.lower()])
False
````

By far the regex version is simpler, but it's always interesting to think about other ways to accomplish a task. Anyway, if the given `word` does not have a vowel, I throw a `parser.error`.

## Using Soundex

The `soundex` module has you create a `Soundex` object and then call a `soundex` function, which all seems a bit repetitive. Still, it gives us a way to get a Soundex value for a given word:

````
>>> from soundex import Soundex
>>> sndx = Soundex()
>>> sndx.soundex('paper')
'p16'
````

The problem is that sometimes we want the stemmed version of the word:

````
>>> sndx.soundex('aper')
'a16'
````

So I wrote a `stemmer` function that does (or does not) stem the word using the value of the `--stem` option which I defined in `argparse` as a Boolean value. I tried to find a way to remove leading consonants both with and without regular expressions. The regex version builds a somewhat complicated regex. Let's start with how to match something at the start of a string that is *not* a vowel (again, because there are only 5 to list):

````
>>> import re
>>> re.search(r'^[^aeiou]+', 'chair')
<re.Match object; span=(0, 2), match='ch'>
````

So we saw earlier that `[aeiou]` is the character class that matches vowels, so we can *negate* the class with `^` **inside** the character class. It's a bit confusing because there is also a `^` at the beginning of the `r''` (raw) string that anchors the expression to the beginning of the string.

OK, so that find the non-vowels leading the word, but we want the bit afterwards. It seems like we could just write something like this:

````
>>> re.search(r'^[^aeiou]+(.+)$', 'chr')
<re.Match object; span=(0, 3), match='chr'>
````

Which seems to say "one or more non-vowels followed by one or more of anything" and it looks to work, but look further:

````
>>> re.search(r'^[^aeiou]+(.+)$', 'chr').groups()
('r',)
````

It finds the last `r`. We need to specify that after the non-vowels there needs to be at least one vowel:

````
>>> re.search(r'^[^aeiou]+([aeiou].*)', 'chr')
````

And now it works:

````
>>> re.search(r'^[^aeiou]+([aeiou].*)', 'chr')
>>> re.search(r'^[^aeiou]+([aeiou].*)', 'car')
<re.Match object; span=(0, 3), match='car'>
>>> re.search(r'^[^aeiou]+([aeiou].*)', 'car').groups()
('ar',)
````

So the `stemmer` works by first looking to see if we should even attempt to `stem`. If so, it attempts to match the regular expression. If that succeeds, then it returns the match. The `else` for everything is to return the original string `s`.

The two other versions of `stemmer` rely on some things I'll discuss later.

As stated in the intro, it was most helpful to me to add the `test_stemmer` function to ensure that all my versions of the `stemmer` function actually had the same behavior.

Once I have the `stemmer` function, I can apply it to the given `word` and every word in the `--wordlist` and then call the ``
