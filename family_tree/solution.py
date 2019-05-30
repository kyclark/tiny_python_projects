#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-24
Purpose: Display a family tree
"""

import argparse
import os
import re
import sys
from graphviz import Digraph


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Display a family tree',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='File input')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fh = args.file
    out_file = args.outfile or os.path.basename(fh.name) + '.gv'

    nodes, edges = parse_tree(fh)
    dot = Digraph(comment='Tree')
    for initials, name in nodes.items():
        dot.node(name)

    for n1, n2 in edges:
        if n1 in nodes:
            n1 = nodes[n1]
        if n2 in nodes:
            n2 = nodes[n2]

        dot.edge(n1, n2)

    dot.render(out_file, view=True)

    print('Done, see output in "{}".'.format(out_file))

# --------------------------------------------------
def parse_tree(fh):
    """parse input file"""

    ini_patt = '([A-Za-z0-9]+)'
    name_patt = ini_patt + '\s*=\s*(.+)'
    begat_patt = ini_patt + '\s+and\s+' + ini_patt + '\s+begat\s+(.+)'
    married_patt = ini_patt + '\s+married\s+' + ini_patt
    edges = set()
    nodes = {}

    for line in fh:
        name_match = re.match(name_patt, line)
        begat_match = re.match(begat_patt, line)
        married_match = re.match(married_patt, line)

        if name_match:
            initials, name = name_match.groups()
            nodes[initials] = name
        elif married_match:
            p1, p2 = married_match.groups()
            edges.add((p1, p2))
        elif begat_match:
            p1, p2, begat = begat_match.groups()
            children = re.split('\s*,\s*', begat)
            for parent in p1, p2:
                for child in children:
                    edges.add((parent, child))

    return nodes, edges


# --------------------------------------------------
if __name__ == '__main__':
    main()
