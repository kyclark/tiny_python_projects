If you define the `file` with `type=argparse.FileType('r')`, then `argparse` with verify that the value is a file, creating an error and usage if it is not, and then will `open` it for you. Quite the time saver. I also define `--inputs` with `nargs='+'` so that I can get any number of strings as a `list`. If none are provided, the default value will be `None`, so be sure you don't assume it's a list and try doing list operations on a `None`.

The first thing we need to do is `read` the input file:

````
>>> from pprint import pprint as pp
>>> text = open('help.txt').read()
>>> pp(text)
('<exclamation>! I need <noun>!\n'
 '<exclamation>! Not just <noun>!\n'
 '<exclamation>! You know I need <noun>!\n'
 '<exclamation>!\n')
````

We need to find all the `<...>` bits, so let's use a regular expression. We can find a literal `<` character like so:

````
>>> import re
>>> re.search('<', text)
<re.Match object; span=(0, 1), match='<'>
````

Now let's find it's mate pair. The `.` means "anything," and we can add a `+` after it to mean "one or more":

````
>>> re.search('<.+>', text)
<re.Match object; span=(0, 28), match='<exclamation>! I need <noun>'>
````

Hmm, that matched all the way to the end of the string instead of stopping at the first available `>`. Often we find that regexes are "greedy" in that they will keep matching beyond where we want them to. If we add a `?` after the `+`, that will make it "non-greedy":

````
>>> re.search('<.+?>', text)
<re.Match object; span=(0, 13), match='<exclamation>'>
````

Another way is to say that we want to match one or more of anything that is *not* a `>`. We can create a character class `[>]` and then put a caret (`^`) *inside* it to negate the class. We'll add parens `()` to capture the whole mess as well as parens to capture the bit inside the `<>`

````
>>> re.search('(<([^>]+)>)', text)
<re.Match object; span=(0, 13), match='<exclamation>'>
````
 
Now we can `re.findall` if we just want the matching text:

````
>>> pp(re.findall('(<([^>]+)>)', text))
['<exclamation>',
 '<noun>',
 '<exclamation>',
 '<noun>',
 '<exclamation>',
 '<noun>',
 '<exclamation>']
````

But I wanted to use each match object, so I used `re.finditer` to return an iterator over the matches:

````
>>> it = re.finditer('(<([^>]+)>)', text)
>>> type(it)
<class 'callable_iterator'>
````

Iterables are "lazy", so if I `print` it, I'll just get a message about it being an object:

````
>>> pp(it)
<callable_iterator object at 0x1015a30f0>
````

In the REPL, I can call `list` to force Python to evaluate the iterable to the end:

````
>>> pp(list(it))
[<re.Match object; span=(0, 13), match='<exclamation>'>,
 <re.Match object; span=(22, 28), match='<noun>'>,
 <re.Match object; span=(30, 43), match='<exclamation>'>,
 <re.Match object; span=(54, 60), match='<noun>'>,
 <re.Match object; span=(62, 75), match='<exclamation>'>,
 <re.Match object; span=(93, 99), match='<noun>'>,
 <re.Match object; span=(101, 114), match='<exclamation>'>]
````

But note that it has not been exhausted and cannot be iterated again:

````
>>> pp(list(it))
[]
````

Which is why I convert it to a `list` right away so that I can evaluate if I found any (by inspecting the length) and then iterate over them:

````
>>> blanks = list(re.finditer('(<([^>]+)>)', text))
>>> len(blanks)
7
>>> for match in blanks:
...     print(match.group(1))
...
<exclamation>
<noun>
<exclamation>
<noun>
<exclamation>
<noun>
<exclamation>
````

The `groups` are defined in the order that you create them by counting the opening parenthesis. In our case, the second group is inside the first group, which is fine. If you start getting lots of groups, it might be best to name them:

````
>>> blanks = list(re.finditer(r'(?P<placeholder><(?P<name>[^>]+)>)', text))
>>> for match in blanks:
...     print(match.group('name'))
...
exclamation
noun
exclamation
noun
exclamation
noun
exclamation
````

Now to get the values from the user. We can use the `name` as the prompt for `input`:

````
>>> blanks = list(re.finditer(r'(<([^>]+)>)', text))
>>> for match in blanks:
...     name = match.group(2)
...     answer = input('{}: '.format(name))
...
exclamation: Dude!
````

But I will make it a bit more flexible by using an `if` *expression to take `pop` a value from the `inputs` list if that is available, otherwise I will use the `input`:

````
>>> inputs = ['Wow']
>>> answer = inputs.pop(0) if inputs else input('{}: '.format(name))
>>> answer
'Wow'
````

Now we need to put the user's `answer` into the original `text` which we can do with `re.sub` (substitute):

````
>>> pp(text)
('<exclamation>! I need <noun>!\n'
 '<exclamation>! Not just <noun>!\n'
 '<exclamation>! You know I need <noun>!\n'
 '<exclamation>!\n')
>>> placeholder = '<exclamation>'
>>> text = re.sub(placeholder, answer, text, count=1)
>>> pp(text)
('Wow! I need <noun>!\n'
 '<exclamation>! Not just <noun>!\n'
 '<exclamation>! You know I need <noun>!\n'
 '<exclamation>!\n')
````

The `count=1` is necessary to prevent `re.sub` from replacing *every* instance of the pattern. After doing that for every placeholder in the `text`, we can `print(text)` and we are done!
