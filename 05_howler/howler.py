#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-12
Purpose: Tiny Python Projects map to uppercase with multifile input
"""

import argparse
from genericpath import isdir
import os
import sys
import io


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Map input(s) to uppercase',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outdir',
                        help='output directory',
                        metavar='str',
                        type=str,
                        default=None)

    parser.add_argument('-l',
                        '--lowercase',
                        help='map input to lowercase',
                        action='store_true')
    
    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        nargs='+',
                        help='input string or list of input files')

    args = parser.parse_args()
    
    args.handles = []
    if args.outdir:
        if not isdir(args.outdir):
            os.mkdir(args.outdir)
        for file in args.text:
            basename = os.path.basename(file)
            args.handles.append((open(file), open(os.path.join(args.outdir, basename), 'wt')))
    else:
        args.handles.append((io.StringIO(' '.join(args.text) + '\n'), sys.stdout))

    return args

def main():
    """Output uppercase string"""

    args = get_args()
    for streampairs in args.handles:
        for line in streampairs[0]:
            streampairs[1].write(line.upper()) if not args.lowercase else streampairs[1].write(line.lower())
        streampairs[1].close()

if __name__ == '__main__':
    main()
