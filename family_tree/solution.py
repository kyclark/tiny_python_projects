#!/usr/bin/env python3
"""Display a family tree"""

import argparse
import os
import re
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

    parser.add_argument('-v', '--view', help='View image', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fh = args.file
    out_file = args.outfile or os.path.basename(fh.name) + '.gv'

    nodes, edges = parse_tree(fh)

    if not nodes and not edges:
        print('No nodes or edges in "{}".'.format(fh.name))
        sys.exit(1)

    dot = Digraph(comment='Tree')

    # keys are initials which we don't need
    for _, name in nodes.items():
        dot.node(name)

    for n1, n2 in edges:
        # see if node has alias in nodes, else use node itself
        n1 = nodes.get(n1, n1)
        n2 = nodes.get(n2, n2)
        dot.edge(n1, n2)

    dot.render(out_file, view=args.view)

    print('Done, see output in "{}".'.format(out_file))


# --------------------------------------------------
def parse_tree(fh):
    """parse input file"""

    name_patt = r'(.+)\s*=\s*(.+)'
    married_patt = r'(.+)\s+married\s+(.+)'
    begat_patt = r'(.+)\s+and\s+(.+)\s+begat\s+(.+)'

    edges = set()
    nodes = {}

    for line in fh:
        name_match = re.match(name_patt, line)
        begat_match = re.match(begat_patt, line)
        married_match = re.match(married_patt, line)

        if name_match:
            initials, name = name_match.groups()
            nodes[initials.strip()] = name.strip()
        elif married_match:
            p1, p2 = married_match.groups()
            edges.add((p1.strip(), p2.strip()))
        elif begat_match:
            p1, p2, begat = begat_match.groups()
            children = re.split(r'\s*,\s*', begat)
            for parent in p1, p2:
                for child in children:
                    edges.add((parent.strip(), child.strip()))

    return nodes, edges


# --------------------------------------------------
if __name__ == '__main__':
    main()
