#!/usr/bin/env python3
"""Mad Libs"""

import argparse
import os
import re
import sys
from dire import die


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Input file')

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='str',
                        type=str,
                        nargs='+',
                        required=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs = args.inputs
    regex = re.compile('([<][^>]+[>])')
    text = args.file.read().rstrip()
    blanks = list(regex.finditer(text))

    if not blanks: die('File "{}" has no placeholders'.format(args.file.name))

    for blank in blanks:
        name = blank.group(1)
        answer = inputs.pop(0) if inputs else input('{}: '.format(
            name.replace('<', '').replace('>', '')))
        text = re.sub(name, answer, text, count=1)

    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
