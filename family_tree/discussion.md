There are two main parts to the program:

1. Parsing the input file for nodes and edges
2. Using nodes and edges with the `graphviz` module to produce a graph

## Parsing input file

Since there are only three types of statements we expect in the input file, I will create three regular expressions to match each. 

### Parsing name line

The first allowed expression is something along the lines of "INITIALS = Full Name":

````
>>> line = 'H7 = Henry VII'
````

I could look for an equal sign in the line and `split` it if found:

````
>>> if '=' in line:
...     line.split('=')
...
['H7 ', ' Henry VII']
````

Or I could `import re` to bring in the regular expression module and write a pattern to match "something, an equal sign, something else". The dot `.` means "anything" and I can use `.+` to say "one or more of anything". This regex matches the whole line:

````
>>> import re
>>> re.match('.+', line)
<re.Match object; span=(0, 14), match='H7 = Henry VII'>
````

There may or may not be whitespace around the equal signs. Whitespace is `\s`, and we can use `\s*` to indicate "zero or more whitespace". The equal sign is a literal `=`, and then more optional whitespace. This regex takes up to the space after the `=`:

````
>>> re.match('.+\s*=\s*', line)
<re.Match object; span=(0, 5), match='H7 = '>
````

We can finish it off with the same pattern at the beginning and put parentheses `()` around the parts of the pattern we want to capture:

````
>>> re.match('(.+)\s*=\s*(.+)', line)
<re.Match object; span=(0, 14), match='H7 = Henry VII'>
>>> match = re.match('(.+)\s*=\s*(.+)', line)
>>> match.groups()
('H7 ', 'Henry VII')
````

There is some trailing whitespace around the first group, so I'll be sure to `strip` it to remove spaces from the beginning and end.

### Parsing married line

The "A married B" line can be found in a very similar fashion. Instead of `=` we can substitute `married`:

````
>>> line = 'H8 married COA'
>>> re.match(r'(.+)\s+married\s+(.+)', line)
<re.Match object; span=(0, 14), match='H8 married COA'>
````

And get the parts from `groups`:

````
>>> match = re.match(r'(.+)\s+married\s+(.+)', line)
>>> match.groups()
('H8', 'COA')
````

### Parsing begat line

The previous patterns could have just as easily been handled by looking for the `=` or `married` in the `line` and using `line.split` on the string. The "begat" line is the most complicated and really makes use of regular expressions. 

The pattern still looks similar:

````
>>> line = 'H8 and COA begat HDC, M1'
>>> re.match(r'(.+)\s+and\s+(.+)\s+begat\s+(.+)', line).groups()
('H8', 'COA', 'HDC, M1')
````

The parents are groups 1 and 2, and the children (group 3) can be split with another regex:

````
>>> re.split('\s*,\s*', 'HDC, M1')
['HDC', 'M1']
````

## Building the graph

I chose to represent my graph with two structures:

1. nodes: a `dict` from initials to full names
2. edges: a `set` of 2-tuples of node names

I said in the intro that the "INTIALS = Full Name" was optional, and so technically the "nodes" can be empty. You saw in the `simone.py` example that Graphviz will automatically create nodes as needed when you add edges that name nodes that do not yet exist.

When parsing the input file, I decided to create a `parse_tree` function that takes the input file handle, reads it line-by-line, and tries to match each line to the three regular expressions described above. If I match the "initials" line, I add the initials and names to the `nodes` dictionary. If I find a "married" line, I add the two nodes to the `edges` set. If I find a "begat" line, I add an edge from each parent to each child.

## Using graphviz

The `graphviz` module is an interface to the `graphviz` program which is a stand-alone program you can use directly. Mostly the Python module makes it fairly easy to write the graph structure that `graphviz` expects, giving us an interface to add nodes and edges using the objects provided by the module. Here is a very simple tree:

````
>>> from graphviz import Digraph
>>> dot = Digraph()
>>> dot.edge('Joanie', 'Chachi')
>>> dot.render(view=True)
'Digraph.gv.pdf'
````

To make a more complicated graph, I added the full names from my `nodes` dictionary, and then use those full names to expand the initials from the `edges`, if present. In the end, the code isn't much more complicated that these few lines.