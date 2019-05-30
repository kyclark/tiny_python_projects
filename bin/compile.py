#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-29
Purpose: Compile my book
"""

import argparse
import os
import sys
from subprocess import getstatusoutput, getoutput
from dire import die


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compile my book',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('positional',
    #                     metavar='str',
    #                     help='A positional argument')

    parser.add_argument('-i',
                        '--dir',
                        help='Input dir',
                        metavar='str',
                        type=str,
                        default=os.getcwd())

    parser.add_argument('-o',
                        '--outdir',
                        help='Output dir',
                        metavar='str',
                        type=str,
                        default=os.getcwd())

    parser.add_argument('-c',
                        '--contents',
                        help='Table of contents',
                        metavar='str',
                        type=str,
                        default=None)

    # parser.add_argument('-i',
    #                     '--int',
    #                     help='A named integer argument',
    #                     metavar='int',
    #                     type=int,
    #                     default=0)

    # parser.add_argument('-f',
    #                     '--flag',
    #                     help='A boolean flag',
    #                     action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    in_dir = args.dir
    out_dir = args.outdir
    contents = args.contents

    if not contents:
        cur_dir = os.path.dirname(sys.argv[0])
        contents = os.path.join(cur_dir, 'contents.txt')

    if not os.path.isfile(contents):
        die('Bad --contents "{}"'.format(contents))

    book_file = os.path.join(out_dir, 'book.md')
    with open(book_file, 'wt') as fh:
        for i, dir_name in enumerate(map(str.rstrip, open(contents)), 1):
            print('{:3}: {}'.format(i, dir_name))
            readme = os.path.join(in_dir, dir_name, 'README.md')
            if os.path.isfile(readme):
                print('\tREADME')
                fh.write('# Chapter {}\n\n'.format(i))
                fh.write(open(readme).read())
                fh.write('\n\\pagebreak\n\n')

            solution = os.path.join(in_dir, dir_name, 'solution.py')
            if os.path.isfile(solution):
                print('\tSOLUTION')
                fh.write('# {} Solution\n\n'.format(dir_name))
                fh.write('````\n')
                #fh.write(open(solution).read())
                numbered = getoutput('cat -n {}'.format(solution))
                fh.write(numbered)
                fh.write('\n````\n')
                fh.write('\n\\pagebreak\n\n')

    cmd = 'pandoc {} --pdf-engine=xelatex -o book.pdf'
    rv, out = getstatusoutput(cmd.format(book_file))

    if rv != 0:
        die('Error: {}'.format(out))

# --------------------------------------------------
if __name__ == '__main__':
    main()
