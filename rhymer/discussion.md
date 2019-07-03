As stated in the description, I spent most of my time working out how to stem a word. Some other programs in the book require this idea (Soundex rhymer, Runny Babbit), so you might look there, too. I decided to write a function `stemmer(word)` that will return a tuple of `(prefix, stem)`.

We need to check if the word can be split into one or more consonants followed by at least one vowel and maybe some other stuff, e.g., `'ha'` could be `('h', 'a')`. The easiest way is to write a regular expression using the `re` module. We've already defined the `vowels`, so we can use those to find the complement of `consonants`. I can iterate through the letters of the alphabet by using `string.ascii_lowercase` and find those not in the `vowels`:

````
>>> import string
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> vowels = 'aeiou'
>>> consonants = ''.join(
...     filter(lambda c: c not in vowels, string.ascii_lowercase))
>>> consonants
'bcdfghjklmnpqrstvwxyz'
````

Here we see the use of `filter` which is a "higher-order" function takes a *another function* as the first argument and an iterable as the second argument. The `lambda c` keyword creates an anonymous function with a single argument I call `c` (for "character") which can then be referenced in the function body. 

The more Pythonic way to write this would be a list comprehension:

````
>>> consonants = ''.join([c for c in string.ascii_lowercase if c not in vowels])
>>> consonants
'bcdfghjklmnpqrstvwxyz'
````

Both ways are fine. It's mostly preference, though true Pythonistas would probably disagree. If nothing else, the `filter` might be slower than a comprehension, especially if the iterable were large, so choose whichever way makes more sense for your style and application.

The regular expression is a bit tricky. We want to find consonants at the beginning, so we can use the caret (`^`) to anchor the regex to the start of the string. 

````
>>> r = '^'
>>> r
'^'
````

Then we create a "character class" using `[]` and enumerate inside all the characters that are allowed:

````
>>> r = '^[' + consonants + ']'
>>> r
'^[bcdfghjklmnpqrstvwxyz]'
````

We will want to "capture" these so we can extract them later, so we put parentheses `()` around the character class to group them:

````
>>> r = '^([' + consonants + '])'
>>> r
'^([bcdfghjklmnpqrstvwxyz])'
````

Let's try that and see what we get:

````
>>> import re
>>> re.search(r, 'chair')
<re.Match object; span=(0, 1), match='c'>
````

Hmm, it didn't match `ch` because we didn't tell the regex *how many* to match, so it just matched one. We can add `*` to indicate "zero or more":

````
>>> r = '^([' + consonants + ']*)'
>>> r
'^([bcdfghjklmnpqrstvwxyz]*)'
>>> re.search(r, 'chair')
<re.Match object; span=(0, 2), match='ch'>
````

Very nice. Sometimes you'll see `+` to mean that a pattern can be repeated, but that one means "one or more." By using `*`, I'm relying on the fact that "zero" matches will always be true, so this will also help me find any `word` that begins with a vowel (although it doesn't seem like it just yet):

````
>>> re.search(r, 'apple')
<re.Match object; span=(0, 0), match=''>
````

Now I want to say that after some optional consonant prefix there must be at least one vowel:

````
>>> r = '^([' + consonants + ']*)' + '([' + vowels + '])'
>>> r
'^([bcdfghjklmnpqrstvwxyz]*)([aeiou])'
>>> re.search(r, 'chair')
<re.Match object; span=(0, 3), match='cha'>
>>> re.search(r, 'apple')
<re.Match object; span=(0, 1), match='a'>
````

Getting closer, but we need the regular expression to reach the end of the word now, so we add `.*` where `.` means "one of anything" and `*` means "zero or more":

````
>>> r = '^([' + consonants + ']*)' + '([' + vowels + '].*)'
>>> r
'^([bcdfghjklmnpqrstvwxyz]*)([aeiou].*)'
>>> re.search(r, 'chair')
<re.Match object; span=(0, 5), match='chair'>
>>> re.search(r, 'apple')
<re.Match object; span=(0, 5), match='apple'>
````

Great! We're matching the entire word. The true magic comes in when we look at the capture `groups`:

````
>>> re.search(r, 'chair').groups()
('ch', 'air')
>>> re.search(r, 'apple').groups()
('', 'apple')
````

That is exactly what I wanted to return! For what it's worth, I can get each `group` individually by referencing their order:

````
>>> re.search(r, 'chair').group(1)
'ch'
>>> re.search(r, 'apple').group(2)
'apple'
````

If I can't `match` a string:

````
>>> type(re.search(r, 'RDNZL'))
<class 'NoneType'>
````

I return `None` from my function:

````
>>> def stemmer(word):
...     vowels = 'aeiou'
...     consonants = ''.join(
...         filter(lambda c: c not in vowels, string.ascii_lowercase))
...     match = re.match('^([' + consonants + ']*)([' + vowels + '].*)', word)
...     if match:
...         return match.groups()
...     return None
...
>>> stemmer('apple')
('', 'apple')
>>> stemmer('chair')
('ch', 'air')
>>> stemmer('RDNZL')
````

So, given a working `stemmer` I try to stem a given `word`. If there is no result, I print the message that I cannot rhyme the word. Otherwise I iterate over all the prefixes:

````
>>> prefixes = list('bcdfghjklmnpqrstvwxyz') + (
...     'bl br ch cl cr dr fl fr gl gr pl pr sc '
...     'sh sk sl sm sn sp st sw th tr tw wh wr'
...     'sch scr shr sph spl spr squ str thr').split()
````

And add them to the stem of the word, being sure to avoid any prefix that was the same as the original word:

````
>>> start, rest = stemmer('chair')
>>> start
'ch'
>>> rest
'air'
>>> [p + rest for p in prefixes if p != start][:3]
['bair', 'cair', 'dair']
````