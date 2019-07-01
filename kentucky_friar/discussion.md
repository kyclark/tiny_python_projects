The heart of this program for me is the `fry` function. The `main` and `get_args` should look pretty standard by now. We get some argument that is either the text or the name of a file with the text. I chose to handle the input line-by-line because of the need to `print` the output. I don't want to worry about messing up the existing new lines, so I decided to read a line, strip off the newline, process the words, and `print` it all back out.

I wouldn't want to try to solve this problem without regular expressions, so I didn't really bother exploring a way that doesn't use them. For one thing, I use `re.split` to split the text on things that do and do not look like words. The first argument to this function is the regex that matches the thing you want to split on. Normally this is thrown away, for instance, if I `split` on any amount of whitespace, then the whitespace is not included:

````
>>> import re
>>> s = 'I said, "How do you do?"'
>>> re.split('\s+', s)
['I', 'said,', '"How', 'do', 'you', 'do?"']
````

It's a funny trick with this method that if you put the regex in capturing parens, it will return both the splitting text and the bits in between. The expression `\w` is any "word"-like character, so `\W` is the complement (non-word characters). The plus sign means "one or more", and so it finds all the non-word characters between the words. This is important because I don't want to lose them!

````
>>> re.split(r'(\W+)', s)
['I', ' ', 'said', ', "', 'How', ' ', 'do', ' ', 'you', ' ', 'do', '?"', '']
````

Now I need to process any string that ends in "ing":

````
>>> re.search('(.+)ing$', 'spam')
>>> re.search('(.+)ing$', 'fishing')
<re.Match object; span=(0, 7), match='fishing'>
````

I only want to remove the "g" from two-syllable words, though. A rough guess is to look for a vowel in the part of the work before the "ing", so I wrote the regex to capture the first part:

````
>>> match = re.search('(.+)ing$', 'fishing')
>>> prefix = match.group(1)
>>> prefix
'fish'
>>> re.search('[aeiouy]', prefix)
<re.Match object; span=(1, 2), match='i'>
````

But a word like "swing" would not work:

````
>>> match = re.search('(.+)ing$', 'swing')
>>> prefix = match.group(1)
>>> prefix
'sw'
>>> re.search('[aeiouy]', prefix)
````

If all the conditions are true, I `return` the `prefix` of the word with "in'".

The other word to match is "you" either with an upper- or lowercase "y" which I can represent with a character class `[Yy]` for "either 'Y' or 'y'" which I additionally capture so as to reuse it and maintain the proper case:

````
>>> match = re.match('([Yy])ou$', 'You')
>>> match.group(1) + "'all"
"Y'all"
````

Finally we need to apply our `fry` function to all the pieces we got from splitting the input text. I know that a list comprehension is more "Pythonic," but I just prefer how `map` reads. I also understand that `map` is a bit slower due to the overhead of calling another function, but I don't usually choose Python for performace.

````
>>> def fry(word):
...     ing_word = re.search('(.+)ing$', word)
...     you = re.match('([Yy])ou$', word)
...     if ing_word:
...         prefix = ing_word.group(1)
...         if re.search('[aeiouy]', prefix):
...             return prefix + "in'"
...     elif you:
...         return you.group(1) + "'all"
...     return word
...
>>> s = "Hunting and fishing all you care about."
>>> ''.join([fry(w) for w in re.split(r'(\W+)', s)])
"Huntin' and fishin' all y'all care about."
>>> ''.join(map(fry, re.split(r'(\W+)', s)))
"Huntin' and fishin' all y'all care about."
````