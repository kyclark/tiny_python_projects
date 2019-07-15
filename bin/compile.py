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
from subprocess import getstatusoutput, getoutput, run
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
                        '--chapters',
                        help='Chapters listing',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-a',
                        '--appendix',
                        help='Appendix listing',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)

    return parser.parse_args()

# --------------------------------------------------
def make_outline(dir_name, chapters):
    """Find all the precis.txt files and make OUTLINE.md"""

    assert os.path.isdir(dir_name)

    outline = open(os.path.join(dir_name, 'OUTLINE.md'), 'wt')
    outline.write(f'## Outline\n')

    for i, chapter in enumerate(chapters, start=1):
        precis = os.path.join(dir_name, chapter, 'precis.txt')
        assert os.path.isfile(precis)
        text = open(precis).read()
        outline.write(f'{i}. **{chapter}**: {text}')

    outline.close()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    in_dir = args.dir
    out_dir = args.outdir
    chapters = args.chapters
    appendix = args.appendix
    cur_dir = os.path.dirname(sys.argv[0])

    if not chapters:
        chapters = os.path.join(cur_dir, 'chapters.txt')

    if not os.path.isfile(chapters):
        die('--chapters "{}" is not a file'.format(chapters))

    if not appendix:
        appendix = os.path.join(cur_dir, 'appendices.txt')

    if appendix and not os.path.isfile(appendix):
        die('--appendix "{}" is not a file'.format(appendix))

    book_file = os.path.join(out_dir, 'book.md')
    chapter_list = list(map(str.rstrip, filter(lambda s: s[0] != '#', open(chapters))))

    make_outline(in_dir, chapter_list)

    with open(book_file, 'wt') as fh:
        #fh.write('\\setcounter{tocdepth}{2}\\tableofcontents\n\\newpage\n\n')

        title = 'TITLE.md'
        if os.path.isfile(title):
            fh.write(open(title).read())
            fh.write('\n\n\\newpage\n\n')

        fh.write('\\setcounter{tocdepth}{2}\\tableofcontents\n\n')
        fh.write('\n\\newpage\n\n')

        top_readme = 'README.md'
        if os.path.isfile(top_readme):
            fh.write(open(top_readme).read())
            fh.write('\n\\newpage\n\n')

        outline = 'OUTLINE.md'
        if os.path.isfile(outline):
            fh.write(open(outline).read())
            fh.write('\n\\newpage\n\n')

        for i, dir_name in enumerate(chapter_list, 1):
            print('Chapter {}: {}'.format(i, dir_name))
            readme = os.path.join(in_dir, dir_name, 'README.md')
            if os.path.isfile(readme):
                print('\tREADME')
                chapter = 'Chapter {}: '.format(i)
                text = open(readme).read()
                text = re.sub(r'^#\s+', '# ' + chapter, text)
                fh.write(text + '\n\\newpage\n\n')

            solution_py = os.path.join(in_dir, dir_name, 'solution.py')
            if os.path.isfile(solution_py):
                print('\tSOLUTION')
                fh.write('## Solution\n\n')
                fh.write('````\n')
                numbered = getoutput('cat -n {}'.format(solution_py))
                fh.write(numbered)
                #fh.write(open(solution_py).read())
                fh.write('\n````\n')
                fh.write('\n\\newpage\n\n')
            else:
                print('\t>>>>>>> MISSING SOLUTION <<<<<<<<\n\n')

            solution_md = os.path.join(in_dir, dir_name, 'discussion.md')
            if os.path.isfile(solution_md):
                print('\tDISCUSSION')
                fh.write('## Discussion\n\n')
                fh.write(open(solution_md).read())
                fh.write('\n\\newpage\n\n')

        if appendix:
            for i, dir_name in enumerate(map(str.rstrip, open(appendix)), 1):
                print('Appendix {}: {}'.format(i, dir_name))
                readme = os.path.join(in_dir, 'appendix', dir_name, 'README.md')
                if os.path.isfile(readme):
                    print('\tREADME')
                    header = 'Appendix {}: '.format(i)
                    text = open(readme).read()
                    text = re.sub(r'^#\s+', '# ' + header, text)
                    fh.write(text + '\n\\newpage\n\n')

    cmd = 'pandoc {} --pdf-engine=xelatex -o {}'
    rv, out = getstatusoutput(cmd.format(book_file, args.outfile))

    if rv != 0:
        die('Error: {}'.format(out))

# --------------------------------------------------
if __name__ == '__main__':
    main()
