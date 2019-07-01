![Also definitely not copyright infringement.](images/runny_babbit.png)

For this exercise, I thought I might move the logic to read an optionally named input *file* into the `get_args` function so that by the time I call `args = get_args()` the `args.text` really is just whatever "text" I need to consider, regardless if the source was the command line or a file. If I'm using `input1.txt`, then I essentially have this:

````
>>> text = open('input1.txt').read()
>>> text
'The bunny rabbit is cute.\n'
````

I need all the pairs of words, so that means I first need all the "words" which I'll get by naively using `str.split` (that is, I won't worry about punctation and such):

````
>>> words = text.split()
>>> words
['The', 'bunny', 'rabbit', 'is', 'cute.']
````

Now I need all *pairs* of words which I can get by going from the zeroth word to the second to last word:

````
>>> pairs = []
>>> for k in range(len(words) - 1):
...     pairs.append((words[k], words[k+1]))
...
>>> pairs
[('The', 'bunny'), ('bunny', 'rabbit'), ('rabbit', 'is'), ('is', 'cute.')
````

I need to find all the pairs where both words start with some consonant sounds and where neither of them is in my stop list, which I'll create like so:

````
>>> stop = set('before behind between beyond but by concerning'
...            'despite down during following for from into like near'
...            'plus since that the through throughout to towards'
...            'which with within without'.split())
````

How will I find words that start with consonants? I can easily list all the vowels:

````
>>> vowels = 'aeiouAEIOU'
````

And then create the complement from `string.ascii_lowercase`:

````
>>> import string
>>> consonants = ''.join([c for c in string.ascii_letters if c not in vowels])
>>> consonants
'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
````

And then build a regular expression that looks for the start of a string `^` followed by a character class of all the `consonants` followed by the character class of `vowels` maybe followed by something else. I'll use parentheses `()` to capture both parts:

````
>>> import re
>>> regex = re.compile('^([' + consonants + ']+)([' + vowels + '].*)')
>>> regex.search('chair')
<re.Match object; span=(0, 5), match='chair'>
>>> regex.search('chair').groups()
('ch', 'air')
````

Now I can iterate over the `pairs`. First I check if the either of the words is in the `stop` set by using the `set.intersection` function. For the first pair `('The', 'bunny')` we see there is an intersection:

````
>>> w1 = 'The'
>>> w2 = 'bunny'
>>> set([w1.lower(), w2.lower()]).intersection(stop)
{'the'}
````

For the next pair, there is not:

````
>>> w1 = 'bunny'
>>> w2 = 'rabbit'
>>> set([w1.lower(), w2.lower()]).intersection(stop)
set()
````

The next check in my code is whether I've previously determined that I need to skip these words, so I have to know their positions in the original list. I decided to use `enumerate` over the `words` to get the number of the pair which will equal the position of the first word of each tuple in the original list of `words`. 

Next I need to see if *both* words match my regular expression:

````
>>> m1 = regex.search(w1)
>>> m2 = regex.search(w2)
>>> m1
<re.Match object; span=(0, 5), match='bunny'>
>>> m2
<re.Match object; span=(0, 6), match='rabbit'>
````

They do! So I can use their `groups` to get the parts of each word to swap:

````
>>> m1.groups()
('b', 'unny')
>>> m2.groups()
('r', 'abbit')
>>> prefix1, suffix1 = m1.groups()
>>> prefix2, suffix2 = m2.groups()
````

This is the 2nd pair, so `i` would be equal to `1` in the actual code. I can use this to go mutate the `words` at positions `i` and `i + 1`:

````
>>> i = 1
>>> words[i] = prefix2 + suffix1
>>> words[i + 1] = prefix1 + suffix2
>>> words
['The', 'runny', 'babbit', 'is', 'cute.']
````

I need to be sure to add those positions to the `skip` set I created for the check that I discussed just above.

Finally we need to `print` the `words` back out, joining them on a blank and using `textwrap.wrap` with the `--width` argument to make it pretty:

````
>>> import textwrap
>>> print('\n'.join(textwrap.wrap(' '.join(words), width=70)))
The runny babbit is cute.
````