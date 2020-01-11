#!/usr/bin/env python3
"""Print ASCII table"""

import argparse
import os
import sys
import string
from itertools import zip_longest


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    for chunk in chunker(range(128), 8):
        print('  '.join(map(cell, chunk)))


# --------------------------------------------------
def cell(n):
    """Format a cell"""

    return '{:3} {:2}'.format(n, chr(n) if n >= 33 else 'NA')


# --------------------------------------------------
def chunker(seq, size):
    """Chunk a list into bits"""

    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


# --------------------------------------------------
if __name__ == '__main__':
    main()
