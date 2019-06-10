This program can accept a variable number of arguments which are all the same thing, so the most appropriate way to represent this with `argparse` is shown on lines 15-19 where we define an `item` agument with `nargs='+'` where `nargs` is the *number of arguments* and `'+'` means *one or more*. Remember, even if the user provides only one argument, you will still get a `list` with just one element.

We put the `items` into a variable on line 28. Note that I call it by the plural `items` because it's probably going to be more than one. Also, I call the variable something informative, not just `args` or something too generic. Lastly, I need to decide how to format the items. As in the article selector, I'm using an `if` *expression* rather than an `if` *statement that would look like this:

````
bringing = ''
if num == 1:
    bringing = items[0]
elif num == 2:
    bringing = ' and '.join(items)
else:
    bringing = ', '.join(items[:-1] + [ 'and ' + items[-1]]) 
````

But I chose to condense this down into a double `if` expression with the following form:

````
bringing = one_item if num == 1 else two_items if num == 2 else three_items
````

Finally to `print` the output, I'm using a format string where the `{}` indicates a placeholder for some value like so:

````
>>> 'I spy something {}!'.format('blue')
'I spy something blue!'
````

You can also put names inside the `{}` and pass in key/value pairs in any order:

````
>>> 'Give {person} the {thing}!'.format(thing='bread', person='Maggie')
'Give Maggie the bread!'
````

Depending on your version of Python, you may be able to use *f-strings*:

````
>>> color = 'blue'
>>> f'I spy something {color}!'
'I spy something blue!'
````