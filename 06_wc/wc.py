#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-12
Purpose: Tiny Python Projects word count in Python exercise
"""

import argparse
import sys


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-c',
                        '--characters',
                        help='Print character count',
                        action='store_true')


    parser.add_argument('-l',
                        '--lines',
                        help='Print line count',
                        action='store_true')


    parser.add_argument('-w',
                        '--words',
                        help='Print word count',
                        action='store_true')


    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='*',
                        default=[sys.stdin])

    args =  parser.parse_args()
    if (not args.characters) and (not args.lines) and (not args.words):
        args.characters = args.lines = args.words = True #display all columns if none are specified
    return args


def main():
    """Main program"""

    args = get_args()
    total_files = 0
    total_lines = 0
    total_words = 0
    total_bytes = 0
    for file_handle in args.file:
        file_lines = 0
        file_words = 0
        file_bytes = 0
        for line in file_handle:
            file_lines += 1
            file_words += len(line.split())
            file_bytes += len(line)
        total_files += 1
        total_lines += file_lines
        total_words += file_words
        total_bytes += file_bytes
        if (args.lines): print(f'{file_lines:8}', end='')
        if (args.words): print(f'{file_words:8}', end='')
        if (args.characters): print(f'{file_bytes:8}', end='')
        print(f' {file_handle.name}')
    if total_files > 1:
        if (args.lines): print(f'{total_lines:8}', end='')
        if (args.words): print(f'{total_words:8}', end='')
        if (args.characters): print(f'{total_bytes:8}', end='')
        print(f' total')
    
if __name__ == '__main__':
    main()
