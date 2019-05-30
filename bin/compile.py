#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2019-05-29
Purpose: Compile my book
"""

import argparse
import os
import re
import sys
from subprocess import getstatusoutput, getoutput
from dire import die


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compile my book',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--dir',
                        help='Input dir',
                        metavar='str',
                        type=str,
                        default=os.getcwd())

    parser.add_argument('-f',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='playful_python.pdf')

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
        fh.write('\\setcounter{tocdepth}{1}\\tableofcontents\n\\newpage\n\n')

        top_readme = 'README.md'
        if os.path.isfile(top_readme):
            fh.write(open(top_readme).read())
            fh.write('\n\\newpage\n\n')

        outline = 'OUTLINE.md'
        if os.path.isfile(outline):
            fh.write(open(outline).read())
            fh.write('\n\\newpage\n\n')

        for i, dir_name in enumerate(map(str.rstrip, open(contents)), 1):
            print('{:3}: {}'.format(i, dir_name))
            readme = os.path.join(in_dir, dir_name, 'README.md')
            if os.path.isfile(readme):
                print('\tREADME')
                chapter = 'Chapter {}: '.format(i)
                text = open(readme).read()
                text = re.sub(r'^#\s+', '# ' + chapter, text)
                fh.write(text + '\n\\newpage\n\n')

            solution = os.path.join(in_dir, dir_name, 'solution.py')
            if os.path.isfile(solution):
                print('\tSOLUTION')
                fh.write('## Solution\n\n')
                fh.write('````\n')
                numbered = getoutput('cat -n {}'.format(solution))
                fh.write(numbered)
                fh.write('\n````\n')
                fh.write('\n\\newpage\n\n')

    cmd = 'pandoc {} --pdf-engine=xelatex -o {}'
    rv, out = getstatusoutput(cmd.format(book_file, args.outfile))

    if rv != 0:
        die('Error: {}'.format(out))


# --------------------------------------------------
if __name__ == '__main__':
    main()
