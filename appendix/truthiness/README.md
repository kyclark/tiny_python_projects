# Truthiness

While it would seem Python has an actual Boolean (Yes/No, True/False) type, this idea can be seriously abused in many odd and confusing ways. First off, there are actual `True` and `False` values:

````
>>> True == True
True
>>> False == False
True
````

But they are equivalent to integers:

````
>>> True == 1
True
>>> False == 0
True
````

Which means, oddly, that you can add them:

````
>>> True + True
2
>>> True + True + False
2
````

Lots of things are `False`-ey when they are evaluated in a Boolean context. The `int` `0`, the `float` `0.0`, the empty string, an empty list, and the special value `None` are all considered `False`-ey:

````
>>> 'Hooray!' if 0 else 'Shucks!'
'Shucks!'
>>> 'Hooray!' if 0. else 'Shucks!'
'Shucks!'
>>> 'Hooray!' if [] else 'Shucks!'
'Shucks!'
>>> 'Hooray!' if '' else 'Shucks!'
'Shucks!'
>>> 'Hooray!' if None else 'Shucks!'
'Shucks!'
````

But note:

````
>>> 'Hooray!' if 'None' else 'Shucks!'
'Hooray!'
````

There are quotes around `'None'` so it's the literal string "None" and not the special value `None`, and, since this is not an empty string, it evaluates *in a Boolean context* to not-`False` which is basically `True`.

This behavior can introduce extremely subtle logical bugs into your programs that the Python compiler and linters cannot uncover. Consider the `dict.get` method that will safely return the value for a given key in a dictionary, returning `None` if the key does not exist. Given this dictionary:

````
>>> d = {'foo': 0, 'bar': None}
````

If we access a key that doesn't exist, Python generates an exception that, if not caught in our code, would immediately crash the program:

````
>>> d['baz']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'baz'
````

But we can use `d.get()` to do this safely:

````
>>> d.get('baz')
````

Hmm, that seems unhelpful! What did we get back?

````
>>> type(d.get('baz'))
<class 'NoneType'>
````

Ah, we got `None`! 

We could use an `or` to define a default value:

````
>>> d.get('baz') or 'NA'
'NA'
````

It turns out the `get` method accepts a second, optional argument of the default value to return:

````
>>> d.get('baz', 'NA')
'NA'
````

Great! So let's use that on the other values:

````
>>> d.get('foo', 'NA')
0
>>> d.get('bar', 'NA')
````

The call for `bar` returned nothing because we put an actual `None` as the value:

````
>>> type(d.get('bar', 'NA'))
<class 'NoneType'>
````

The key `bar` didn't fail because that key exists in the dictionary. The `dict.get` method only returns the second, default argument *if the key does not exist in the dictionary* which is entirely different from checking the *value* of the key in the dictionary. OK, so we go back to this:

````
>>> d.get('bar') or 'NA'
'NA'
````

Which seems to work, but notice this:

````
>>> d.get('foo') or 'NA'
'NA'
````

The value for `foo` is actually `0` which evaluates to `False` given the Boolean evaluation of the `or`. If this were a measurement of some value like the amount of sodium in water, then the string `NA` would indicate that no value was recorded whereas `0` indicates that sodium was measured and none detected. If some sort of important analysis rested on our interpretation of the strings in a spreadsheet, we might inadvertently introduce missing values because of the way Python coerces various non-Boolean values into Boolean values.

Perhaps a safer way to access these values would be:

````
>>> for key in ['foo', 'bar', 'baz']:
...   val = d[key] if key in d else 'NA'
...   val = 'NA' if val is None else val
...   print(key, val)
...
foo 0
bar NA
baz NA
````
