#!/usr/bin/env python3
"""
My best friend's sister's boyfriend's brother's girlfriend heard
from this guy who knows this kid who's going with the girl who
saw Ferris pass out at 31 Flavors last night.
"""

from graphviz import Digraph
nodes = ('Simone', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Ferris')
labels = ("best friend's", "sister's", "boyfriend's", "brother's",
          "girlfriend", "heard from", "knows", "going out with", "saw")

dot = Digraph('Simone')
for k in range(len(nodes) - 1):
    dot.edge(nodes[k], nodes[k+1], label=' ' + labels[k])

dot.render('simone.gv', view=True)
