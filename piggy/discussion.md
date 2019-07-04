As with so many other exercises that want files as input, I'm going to rely on `argparse` to verify that the `type=argparse.FileType('r')` for the `file` argument. I will also specify `nargs='+'` to indicate "one or more." The `--outdir` is just a `str` and the directory it names may or may not exist, so there's really nothing to validate. I set the `default='out-yay'`.

Testing to see if a string names a directory is rather straightforward:

````
>>> import os
>>> out_dir = 'out-yay'
>>> os.path.isdir(out_dir)
False
````

If it doesn't exist, we use `os.makedirs` which is equivalent to `mkdir -p` on the command line in that parent directories will be created along the way if needed. That is, if the user specifies `~/python/pigsty/out_files` and you try to use `os.mkdir`, it will fail. This is why I never use `os.mkdir`:

````
>>> out_dir = '~/python/pigsty/out_files'
>>> os.path.isdir(out_dir)
False
>>> os.mkdir(out_dir)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: \
'~/python/pigsty/out_files'
````

## The Pigifier

Let's start with the actual Pig Latinification of any given word. According to the rules, we add "-yay" to words starting with vowels, so "apple" becomes "apple-yay"; otherwise, we move consonant sounds to the end and add "ay", so "chair" becomes "air-chay." We've seen this same problem in other exercises like Runny Babbit and the rhymers. As in those solutions, to identify consonants I will complement the set of vowels:

````
>>> import string, re
>>> vowels = 'aeiouAEIOU'
>>> consonants = re.sub('[' + vowels + ']', '', string.ascii_letters)
>>> consonants
'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
````

I'm looking for the start of a string, so I will use the caret (`^`) to anchor a character class of consonants. I will verify this works:

````
>>> regex = '^[' + consonants + ']+'
>>> regex
'^[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]+'
>>> re.search(regex, 'chair')
<re.Match object; span=(0, 2), match='ch'>
````

There needs to be at least one vowel after this:

````
>>> regex = '^[' + consonants + ']+[' + vowels + ']'
>>> regex
'^[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]+[aeiouAEIOU]'
>>> re.search(regex, 'chair')
<re.Match object; span=(0, 3), match='cha'>
````

And then anything else which is represented with a dot `.` and any number which is a star `*`:

````
>>> regex = '^[' + consonants + ']+[' + vowels + '].*'
>>> re.search(regex, 'chair')
<re.Match object; span=(0, 5), match='chair'>
````

Finally we want to capture the first thing and the second thing, so we add parentheses so we can access the `match.groups()` method:

````
>>> regex = '^([' + consonants + ']+)([' + vowels + '].*)'
>>> regex
'^([bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]+)([aeiouAEIOU].*)'
>>> re.search(regex, 'chair')
>>> re.search(regex, 'chair').groups()
('ch', 'air')
````

So *if* the `search` succeeds and we get a `match` object, we can use the `groups` to move the first group to the end with "ay"; otherwise, we just add "-yay" to the end:

````
>>> word = 'chair'
>>> match = re.match('^([' + consonants + ']+)(['+ vowels + '].*)', word)
>>> if match:
...     word = '-'.join([match.group(2), match.group(1) + 'ay'])
... else:
...     word = word + '-yay'
...
>>> word
'air-chay'
````

Let's make this into a function:

````
>>> def pig(word):
...     """Create Pig Latin version of a word"""
...     if re.match(r"^[\w']+$", word):
...         vowels = 'aeiouAEIOU'
...         consonants = re.sub('[' + vowels + ']', '', string.ascii_letters)
...         match = re.match('^([' + consonants + ']+)(['+ vowels + '].*)', word)
...         if match:
...             word = '-'.join([match.group(2), match.group(1) + 'ay'])
...         else:
...             word = word + '-yay'
...     return word
...
````

And manually verify it:

````
>>> pig('chair')
'air-chay'
>>> pig('apple')
'apple-yay'
````

In my solution, I added a `test_pig` function that uses the  `assert` function to verify that `pig('apple')` return "apple-yay" and so forth. If I run `pytest` on my `piggy.py` program, it will execute any function that starts with `test_`. This way I can be sure that my function continues to work if I make changes to the program.

## Pigification of words

Now we have a problem we've seen in many other examples: we want to apply our `pig` function to all the words in a file. I've shown my preference for the `map` function, but we can also use `for` loops or list comprehensions. They will all accomplish the task. 

First we have to deal with fact that we can have several input files. Since I defined the `file` argument with `nargs='+'`, then `args.file` will be a `list`. Even if the user defined only one file, `args.file` will be a `list` with one element. I can use a `for` loop to iterate through the files. Additionally, I want to list the number of the file as I'm processing them, so I will use the `enumerate` function to give me both the position in the list and the name of each file. Because I don't want to start counting at `0`, I'll use the `start=1` option:

````
>>> files = ['../inputs/spiders.txt', '../inputs/fox.txt']
>>> list(enumerate(files, start=1))
[(1, '../inputs/spiders.txt'), (2, '../inputs/fox.txt')]
````

That returns a `list` of tuples which I can unpack into a `i` ("integer", a common throwaway name for an incrementing counter) and `fh` ("file handle" which it is because `argparse` has already performed an `open` on the file). I will use a format string to print the `i` in a space three characters wide (right-justified), followed by a colon and then the name of the file:

````
>>> files = map(open, ['../inputs/spiders.txt', '../inputs/fox.txt'])
>>> for i, fh in enumerate(files, start=1):
...     print('{:3}: {}'.format(i, fh.name))
...
  1: ../inputs/spiders.txt
  2: ../inputs/fox.txt
````

I want to maintain the original line endings for each file, so I will read each file line-by-line using a `for` loop:

````
>>> fh = open('../inputs/spiders.txt')
>>> for line in fh:
...     print(line, end='')
...
Don’t worry, spiders,
I keep house
casually.
````

Now here is a problem: We can't just use `split` to read the input text because punctuation will still be attached:

````
>>> line = "Don't worry, spiders,"
>>> line.split()
["Don't", 'worry,', 'spiders,']
````

Our `pig` fails with this input:

````
>>> pig('worry,')
'worry,'
>>> list(map(pig, line.split()))
["on't-Day", 'worry,', 'spiders,']
````

We could use regular expressions to remove anything not a character, but then we'd lose the original structure of the document. We need to find just the words themselves but not lose anything along the way. We can use `re.split` on `\W+` to define "one or more of any non-word character":

````
>>> re.split('\W+', line)
['Don', 't', 'worry', 'spiders', '']
````

But that splits "Don't" into two words, and we lose all the punctionation. Oddly, we can add capturing parens around the split pattern to get all the parts of the string:

````
>>> re.split('(\W+)', line)
['Don', "'", 't', ' ', 'worry', ', ', 'spiders', ',', '']
````

But that doesn't stop "Don't" being split. We need a far more complicated pattern:

````
>>> splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
>>> splitter.split(line)
['', "Don't", ' ', 'worry', ', ', 'spiders', ',']
````

Wow! I'll confess that I did not create that myself. I found it on StackOverflow, but the magical thing is that it was from a Java question. Regular expressions, however, is an idea separate from any one programming language. They are mostly compatible from Perl to Ruby to Rust. I searched for "regex split text word boundaries apostrophe" because I wanted a pattern that wouldn't split on a single quote (an apostrophe). I was able to use the exact pattern from an answer in Java because the regex is (usually) the same no matter where you use it!

Now I can `map` the `pig` function onto each part of the split line:

````
>>> list(map(pig, splitter.split(line)))
['', "on't-Day", ' ', 'orry-way', ', ', 'iders-spay', ',']
````

Or a list comprehension:

````
>>> [pig(w) for w in splitter.split(line)]
['', "on't-Day", ' ', 'orry-way', ', ', 'iders-spay', ',']
````

This is a rare exercise where you are required to write an output file. To create the ouput file name, we need the "basename" of the file which we can get with `os.path.basename`. Then use `os.path.join` to add the `out_dir` (which we created if needed) to the basename. Then we `open` that with the flags `w` for "write" and `t` for "text" which can be combined `wt`:

````
>>> fh.name
'../inputs/spiders.txt'
>>> basename = os.path.basename(fh.name)
>>> basename
'spiders.txt'
>>> out_file = os.path.join(out_dir, basename)
>>> out_file
'~/python/pigsty/out_files/spiders.txt'
>>> out_fh = open(out_file, 'wt')
````

I've called my output file handle `out_fh` so I can remember what it is. For each line of input text, we use `out_fh.write()` to print our text. It's important to remember that `print` will add a newline unless you tell it not to (using `end=''`), but `fh.write` will *not* add a newline unless you tell it to (by adding `+ '\n'` to your output string). In our case, the lines we are reading have a newline still attached, so we don't need to add another. Be sure to `close` the file handle when you are done.

````
>>> out_fh = open(out_file, 'wt')
>>> for line in fh:
...     out_fh.write(''.join(map(pig, splitter.split(line))))
...
>>> out_fh.close()
````

That is the crux of the program. All that is left is to report to the user how many files were processed and to remind them of the output directory.
