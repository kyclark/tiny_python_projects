The `text` argument for the program might be taken directly from the command line or from a named file. I chose to handle inside the `get_args` the reading of a file argument so that by the time I call `args = get_args()` I have the actual `text` I need to process.

## Reading lines of text

As mentioned in the description of the program, the test suite is looking for the lines of input text to be maintained in the output. It's straightforward to `read` an `open` file line-by-line:

````
>>> file = '../inputs/spiders.txt'
>>> for line in open(file):
...     print(line, end='')
...
Don’t worry, spiders,
I keep house
casually.
````

If I've taken the `text` from a file, then it's all just now just one string and a `for` loop on a string will iterate over each *character* not each line.

````
>>> text = open(file).read()
>>> text
'Don’t worry, spiders,\nI keep house\ncasually.\n'
>>> for char in text:
...     print(char, end='-')
...
D-o-n-’-t- -w-o-r-r-y-,- -s-p-i-d-e-r-s-,-
-I- -k-e-e-p- -h-o-u-s-e-
-c-a-s-u-a-l-l-y-.-
````

So instead we can use `str.splitlines()` to break `text` on the newlines:

````
>>> for line in text.splitlines():
...     print(line)
...
Don’t worry, spiders,
I keep house
casually.
````

## List comprehensions vs map

Like several other programs, we now are left with applying some function to each member of a list. That is, we want to turn each word into a number, and we've seen there are several ways to go about this. I will focus on two methods which I use twice each: list comprensions and the `map` function.

## Encoding one word

First let's take just one word. We've seen how we can use `ord` to turn one character into a number:

````
>>> ord('g')
103
````

We can use a list comprehension to do this for every character in a word:

````
>>> word = 'gematria'
>>> [ord(char) for char in word]
[103, 101, 109, 97, 116, 114, 105, 97]
````

And then the `sum` function will add those for us:

````
>>> sum([ord(char) for char in word])
842
````

We can do the same thing with `map`. The first argument to `map` is a function which is applied to every element in the second argument which must be something *iterable* like a `list` or a generator. Because the second argument is iterable, we don't have to spell out `for char in`. 

````
>>> map(ord, word)
<map object at 0x105c3c550>
````

We see this because `map` is a "lazy" function that doesn't actually produce results until they are actually required. For purposes of viewing in the REPL only, we can use `list` to see the values. (You do not have to use `list` in your actual code!)

````
>>> list(map(ord, word))
[103, 101, 109, 97, 116, 114, 105, 97]
````

And now we can `sum` that. Note that `sum` will consume the `map` object, so we don't have to use `list`. To me, this is an extremly clean bit of code:

````
>>> sum(map(ord, word))
842
````

Since ultimately I will be giving these numbers to `print` in a way that will expect strings, I will additionally coerce the number using `str`. We can put this into a function either writing it with `lambda` on one line:

````
>>> word2num = lambda word: str(sum(map(ord, word)))
>>> word2num('gematria')
'842'
````

Or using `def`:

````
>>> def word2num(word):
...     return str(sum(map(ord, word)))
...
>>> word2num('gematria')
'842'
````

## Finding the words

Just above we were applying the `ord` function to every character in a word. Now we want to apply our new `word2num` function to every word in a line. I hope you see it's the exact same problem, and both list comprehensions and `map` will serve equally. 

So how to find "words" in a line? We know that we can use `str.split()` to break each `line` into `words`:

````
>>> for line in text.splitlines():
...     words = line.split()
...     print(words)
...
['Don’t', 'worry,', 'spiders,']
['I', 'keep', 'house']
['casually.']
````

There's a small problem, though. Notice that we get `worry,` and not `worry` and `spiders,` instead of `spiders`. We don't want to encode the punctuation that is still attached to the words. Also, let's just say we also don't want to encode the apostrophe in `Don't`. So how can we remove these offending characters? The first step is in identifying what they are. If we say "remove anything that is not the a letter in the set A-Z or a number in the list 0-9", that helps. We can use regular expressions to describe that exactly using `[]` to create a "character class" and putting the allowed characters in there. Notice this filters out the unwanted characters:

````
>>> import re
>>> re.findall('[a-zA-Z0-9]', "Don't")
['D', 'o', 'n', 't']
>>> re.findall('[a-zA-Z0-9]', "spiders,")
['s', 'p', 'i', 'd', 'e', 'r', 's']
````

Or we could use the `re.sub` function to "substitute" any matches. We can negate our character class by putting a caret (`^`) just *inside* the start of the brackets to indicate we want to find anything that's *not* an English alphabet character or an Arabic number and replace it with the empty string:

````
>>> re.sub('[^a-zA-Z0-9]', '', "Don't")
'Dont'
>>> re.sub('[^a-zA-Z0-9]', '', "spiders,")
'spiders'
````

Let's put that into a function:

````
>>> def clean(word):
...     return re.sub('[^a-zA-Z0-9]', '', word)
...
>>> clean("Don't")
'Dont'
>>> clean("spiders,")
'spiders'
````

Compare this with the earlier version to see that we now have "clean" words to encode:

````
>>> for line in text.splitlines():
...     words = map(clean, line.split())
...     print(list(words))
...
['Dont', 'worry', 'spiders']
['I', 'keep', 'house']
['casually']
````

For convenience, let's update the `word2num` function to use that:

````
def word2num(word):
    word = re.sub('[^a-zA-Z0-9]', '', word)
    return str(sum(map(ord, word)))
>>> word2num('spiders,')
'762'
>>> word2num('spiders')
'762'
````

## Encoding all words

So we're finally to the point where we have lines of text and lists of words to encode. As we've seen, a list comprehension works adequately:

````
>>> words = ['Dont', 'worry', 'spiders']
>>> [word2num(word) for word in words]
['405', '579', '762']
````

But `map` is cleaner:

````
>>> list(map(word2num, words))
['405', '579', '762']
````

All that is left is to `print` the encoded words back out:

````
>>> for line in text.splitlines():
...     print(' '.join(map(word2num, line.split())))
...
405 579 762
73 421 548
862
````