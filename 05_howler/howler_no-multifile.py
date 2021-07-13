#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-12
Purpose: Tiny Python Projects map to uppercase
"""

import argparse
import os
import sys
import io


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Map input to uppercase',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-l',
                        '--lowercase',
                        help='Map input to lowercase',
                        action='store_true')
    
    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or filename')

    # parser.add_argument('-i',
    #                     '--int',
    #                     help='A named integer argument',
    #                     metavar='int',
    #                     type=int,
    #                     default=0)

    # parser.add_argument('-f',
    #                     '--file',
    #                     help='A readable file',
    #                     metavar='FILE',
    #                     type=argparse.FileType('rt'),
    #                     default=None)


    args = parser.parse_args()
    
    if (os.path.isfile(args.text)):
        args.text = open(args.text)
    else:
        args.text = io.StringIO(args.text + '\n')
    
    return args

def main():
    """Output uppercase string"""

    args = get_args()

    outfile_handle = open(args.outfile, 'wt') if args.outfile else sys.stdout
    for line in args.text:
        outfile_handle.write(line.upper()) if not args.lowercase else outfile_handle.write(line.lower())
    outfile_handle.close()

if __name__ == '__main__':
    main()
