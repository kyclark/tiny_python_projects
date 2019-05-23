#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 24 October 2018
Purpose: Python program to write a Python program
"""

import argparse
import os
import subprocess
import sys
from datetime import date
from dire import die


# --------------------------------------------------
def get_args():
    """Get arguments"""

    parser = argparse.ArgumentParser(
        description='Create Python argparse/simple program',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('program', help='Program name', type=str)

    parser.add_argument('-s',
                        '--simple',
                        help='Use simple format',
                        action='store_true')

    parser.add_argument('-f',
                        '--force',
                        help='Overwrite existing',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_file = args.program.strip().replace('-', '_')

    if not out_file: die('Not a usable filename "{}"'.format(out_file))

    if not out_file.endswith('.py'): out_file += '.py'

    if os.path.isfile(out_file) and not args.force:
        answer = input('"{}" exists.  Overwrite? [yN] '.format(out_file))
        if not answer.lower().startswith('y'):
            print('Will not overwrite. Bye!')
            sys.exit()

    out_fh = open(out_file, 'w')
    preamble = PREAMBLE.format(os.getenv('USER'), str(date.today()))
    text = SIMPLE if args.simple else ARGPARSE

    out_fh.write(preamble)
    out_fh.write(text)
    subprocess.run(['chmod', '+x', out_file])
    print('Done, see new script "{}."'.format(out_file))


# --------------------------------------------------
PREAMBLE = """#!/usr/bin/env python3
\"\"\"
Author : {}
Date   : {}
Purpose: Rock the Casbah
\"\"\"
"""

# --------------------------------------------------
SIMPLE = """
import os
import sys


# --------------------------------------------------
def main():
    \"\"\"Make a jazz noise here\"\"\"

    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} ARG'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    arg = args[0]

    print('Arg is "{}"'.format(arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
"""

# --------------------------------------------------
ARGPARSE = """
import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    \"\"\"Get command-line arguments\"\"\"

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-f',
                        '--flag',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    \"\"\"Make a jazz noise here\"\"\"

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    flag_arg = args.flag
    pos_arg = args.positional

    print('str_arg = "{}"'.format(str_arg))
    print('int_arg = "{}"'.format(int_arg))
    print('flag_arg = "{}"'.format(flag_arg))
    print('positional = "{}"'.format(pos_arg))


# --------------------------------------------------
if __name__ == '__main__':
    main()
"""

# --------------------------------------------------
if __name__ == '__main__':
    main()
