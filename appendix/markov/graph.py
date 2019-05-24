#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-24
Purpose: Markov chain for characters/words
"""

import argparse
import os
import re
import sys
from collections import defaultdict
from graphviz import Digraph


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Markov chain for characters/words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        help='Training file(s)')

    parser.add_argument('-k',
                        '--kmer_size',
                        help='Kmer size',
                        metavar='int',
                        type=int,
                        default=2)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='str',
                        type=str,
                        default='out.gv')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    k = args.kmer_size

    chains = defaultdict(list)
    for file in args.file:
        for line in open(file):
            for word in line.lower().split():
                word = re.sub('[^a-z]', '', word)
                for i in range(0, len(word) - k):
                    kmer = word[i:i + k + 1]
                    chains[kmer[:-1]].append(kmer[-1])


    dot = Digraph(comment='Paths for K={}'.format(k))
    edges = set()
    for kmer in chains:
        dot.node(kmer)
        for char in chains[kmer]:
            edges.add((kmer, kmer[1:] + char))

    dot.edges(edges)
    dot.render(args.outfile, view=True)


# --------------------------------------------------
if __name__ == '__main__':
    main()
