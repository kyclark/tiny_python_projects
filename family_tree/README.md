# Family Tree

![Partial Tudor family tree](family_tree/tudor.txt.gv.pdf)

Write a program called `tree.py` that will take an input file as a single positional argument and produce an `-o|--outfile` graph of the family tree described therein. There should be a '-v|--view' flag to have the image opened when done (default `False`). The program should produce a usage with no arguments or if given `-h|--help` flags:

````
$ ./tree.py
usage: tree.py [-h] [-o str] [-v] FILE
tree.py: error: the following arguments are required: FILE
$ ./tree.py -h
usage: tree.py [-h] [-o str] [-v] FILE

Display a family tree

positional arguments:
  FILE                  File input

optional arguments:
  -h, --help            show this help message and exit
  -o str, --outfile str
                        Output filename (default: )
  -v, --view            View image (default: False)
````

The input file can have only three kinds of statements:

1. `INITIALS = Full Name`
2. `INITIALS married INTIALLS`
3. `INITIALS and INITIALS begat INITIALS[, INITIALS...]`

Use the `graphviz` module to generate a graph like the one shown above from the following input:

````
$ cat tudor.txt
H7 = Henry VII
EOY = Elizabeth of York
H8 = Henry VIII
COA = Catherine of Aragon
AB = Anne Boleyn
JS = Jane Seymour
AOC = Anne of Cleves
CH = Catherine Howard
CP = Catherine Parr
HDC = Henry, Duke of Cornwall
M1 = Mary I
E1 = Elizabeth I
E6 = Edward VI

H7 married EOY
H7 and EOY begat H8
H8 married COA
H8 married AB
H8 married JS
H8 married AOC
H8 married CH
H8 married CP
H8 and COA begat HDC, M1
H8 and AB begat E1
H8 and JS begat E6
````

If given no `-o|--outfile`, the default should be the name of the input file with `.gv` appended:

````
$ ./tree.py tudor.txt
Done, see output in "tudor.txt.gv".
````

Technically your input file doesn't need the "INITIALS = Full Name" lines. Those are just to make it a bit easier to spell out all the marrying and begetting that people do. Here is a very simple tree:

````
$ cat joanie.txt
Joanie married Chachi
$ ./tree.py joanie.txt
Done, see output in "joanie.txt.gv".
````

![Joanie Loves Chachi](family_tree/joanie.txt.gv.pdf)

## Graphs

You are creating a graph that describes the relationships among entities. Graphs have "nodes" (or "vertices") and "edges" that connect them. In the phrase "My best friend's sister's boyfriend's brother's girlfriend heard from this guy who knows this kid who's going with the girl who saw Ferris pass out at 31 Flavors last night," there are 10 nodes:

1. the speaker (Simone)
2. my best friend
3. sister
4. boyfriend
5. brother
6. girlfriend
7. this guy
8. this kid
9. the girl
10. Ferris

If we call all the unnamed people by a letter like `A`, then we could write code to visualize this graph:

````
from graphviz import Digraph
nodes = ('Simone', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Ferris')
labels = ("best friend's", "sister's", "boyfriend's", "brother's",
          "girlfriend", "heard from", "knows", "going out with", "saw")

dot = Digraph('Simone')
for k in range(len(nodes) - 1):
    dot.edge(nodes[k], nodes[k+1], label=' ' + labels[k])

dot.render('simone.gv', view=True)
````

![Thank you, Simone.](family_tree/simone.gv.pdf)