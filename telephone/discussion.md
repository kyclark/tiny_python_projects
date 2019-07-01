![Telephones are for communication.](images/telephone.png)

The number of mutations will be proportional to the length of the text

````
>>> text = 'The quick brown fox jumps over the lazy dog.'
>>> len_text = len(text)
>>> len_text
44
````

Since we chose the `--mutations` to be a `float` between 0 and 1, we can multiply that by the length to get the number of mutations to introduce. Since that number will likely be another `float` and we can introduce a partial number of mutations, we can use `int` to truncate the number to an integer value.

````
>>> mutations = .1
>>> int(mutations * len_text)
4
````

So we can use that number in a `for` loop with `range(4)` to modify four characters. To choose a character in the text to modify, I suggested to use `random.choice`:

````
>>> import random
>>> random.choice(range(len_text))
1
>>> random.choice(range(len_text))
22
````

If you assign that to a value like `i` (for "integer" and/or "index", it's pretty common to use `i` for this kind of value), then you could get the character at that position:

````
>>> i = random.choice(range(len_text))
>>> i
4
>>> text[i]
'q'
````

Now we saw earlier that we can't just change the `text`:

````
>>> text[i] = 'x'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
````

So we're going to have to create a *new* string using the text before and after `i` which we can get with string slices using `text[start:stop]`. If you leave out "start", Python starts at `0` (the beginning of the string), and if you leave out "stop" then it goes to the end, so `text[:]` is a copy of the entire string.

The bit before `i` is:

````
>>> text[:i]
'The '
````

And after `i` (skipping `i` itself, of course):

````
>>> text[i+1:]
'uick brown fox jumps over the lazy dog.'
````

There are many ways to join strings together into new strings, and the `+` operator is perhaps the simplest. So now we need some new character to insert in the middle which we can get with `random.choice` again, this time choosing from all the letters of the alphabet plus punctuation:

````
>>> import string
>>> alpha = string.ascii_letters + string.punctuation
>>> random.choice(alpha)
'n'
````

So to put it together, we overwrite the existing `text` so as to accumulate the changes over the iterations:

````
>>> text = text[:i] + random.choice(alpha) + text[i+1:]
>>> text
'The vuick brown fox jumps over the lazy dog.'
````

## Mutations in DNA

For what it's worth, this is (sort of) how DNA changes over time. The machinery to copy DNA makes mistakes, and mutations randomly occur. Many times the change has no deleterious affect on the organism. Our example only changes characters to other characters, what are called "point mutations" or "single nucleotide variations" (SNV) or "single nucleotide polymorphisms" (SNP) in biology, but we could write a version that would also randomly delete or insert new characters which are called them "in-dels" (insertion-deletions) in biology.

Mutations (that don't result in the demise of the organism) occur at a fairly standard rate, so counting the number of mutations between a conserved region of any two organisms can allow an estimate of how long ago they diverged from a common ancestor! We can revisit the output of this program later by using the Hamming distance to find how many changes we'd need to make to the output to regain the input.

