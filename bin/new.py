#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Purpose: Python program to write a Python program
Modified by Lee A. Congdon <lee@lcongdon.com> 2021-07-10
"""

import argparse
import os
import platform
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

from typing import NamedTuple


class Args(NamedTuple):
    program: str
    name: str
    email: str
    purpose: str
    overwrite: bool


# --------------------------------------------------
def get_args() -> Args:
    """Get arguments"""

    parser = argparse.ArgumentParser(
        description='Create Python argparse program',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    defaults = get_defaults()
    username = os.getenv('USER') or 'Anonymous'
    hostname = os.getenv('HOSTNAME') or 'localhost'

    parser.add_argument('program', help='Program name', type=str)

    parser.add_argument('-n',
                        '--name',
                        type=str,
                        default=defaults.get('name', username),
                        help='Name for docstring')

    parser.add_argument('-e',
                        '--email',
                        type=str,
                        default=defaults.get('email', f'{username}@{hostname}'),
                        help='Email for docstring')

    parser.add_argument('-p',
                        '--purpose',
                        type=str,
                        default=defaults.get('purpose', 'Rock the Casbah'),
                        help='Purpose for docstring')

    parser.add_argument('-f',
                        '--force',
                        help='Overwrite existing',
                        action='store_true')

    args = parser.parse_args()

    args.program = args.program.strip().replace('-', '_')

    if not args.program:
        parser.error(f'Not a usable filename "{args.program}"')

    return Args(args.program, args.name, args.email, args.purpose, args.force)


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()
    program = args.program

    if os.path.isfile(program) and not args.overwrite:
        answer = input(f'"{program}" exists.  Overwrite? [yN] ')
        if not answer.lower().startswith('y'):
            sys.exit('Will not overwrite. Bye!')

    print(body(args), file=open(program, 'wt'), end='')

    if platform.system() != 'Windows':
        subprocess.run(['chmod', '+x', program], check=True)

    print(f'Done, see new script "{program}."')


# --------------------------------------------------
def body(args: Args) -> str:
    """ The program template """

    today = (date.today()).isoformat()

    return f"""#!/usr/bin/env python3
\"\"\"
Author : {args.name}{' <' + args.email + '>' if args.email else ''}
Date   : {today}
Purpose: {args.purpose}
\"\"\"

import argparse


def get_args():
    \"\"\"Parse arguments\"\"\"

    parser = argparse.ArgumentParser(
        description='{args.purpose}',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-a',
                        '--arg',
                        default='',
                        type=str,
                        help='A named string argument',
                        metavar='str',


    parser.add_argument('-i',
                        '--int',
                        default=0,
                        type=int,
                        help='A named integer argument',
                        metavar='int')


    parser.add_argument('-f',
                        '--file',
                        default=None,
                        type=argparse.FileType('rt'),
                        help='A readable file',
                        metavar='FILE')


    parser.add_argument('-o',
                        '--on',
                        action='store_true',
                        help='A boolean flag')


    parser.add_argument('positional',
                        nargs='+',
                        help='A positional argument',
                        metavar='str')


    return parser.parse_args()


def main():
    \"\"\"Main program\"\"\"

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{{str_arg}}"')
    print(f'int_arg = "{{int_arg}}"')
    print('file_arg = "{{}}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{{flag_arg}}"')
    print(f'positional = "{{pos_arg}}"')


if __name__ == '__main__':
    main()
"""


# --------------------------------------------------
def get_defaults():
    """Get defaults from ~/.new.py"""

    rc = os.path.join(str(Path.home()), '.new.py')
    defaults = {}
    if os.path.isfile(rc):
        for line in open(rc):
            match = re.match('([^=]+)=([^=]+)', line)
            if match:
                key, val = map(str.strip, match.groups())
                if key and val:
                    defaults[key] = val

    return defaults


# --------------------------------------------------
if __name__ == '__main__':
    main()
