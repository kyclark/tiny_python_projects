#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-04-23
Purpose: Write files to Pig Latin
"""

import argparse
import os
import re
import string
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Convert to Pig Latin',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file', metavar='FILE', nargs='+', help='Input file(s)')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='str',
        type=str,
        default='out-yay')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    num_files = 0
    for i, file in enumerate(args.file, start=1):
        basename = os.path.basename(file)
        out_file = os.path.join(out_dir, basename)
        out_fh = open(out_file, 'wt')
        print('{:3}: {}'.format(i, basename))

        if not os.path.isfile(file):
            warn('"{}" is not a file.'.format(file))
            continue

        num_files += 1
        for line in open(file):
            for word in line.split():
                clean = re.sub("[^a-zA-Z0-9']", '', word)
                out_fh.write(pig(clean) + ' ')
            out_fh.write('\n')

        out_fh.close()

    print('Done, wrote {} file{} to "{}".'.format(
        num_files, '' if num_files == 1 else 's', out_dir))


# --------------------------------------------------
def pig(word):
    """Create Pig Latin version of a word"""

    consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
    match = re.match('^([' + consonants + ']+)(.+)', word)
    if match:
        return '-'.join([match.group(2), match.group(1) + 'ay'])
    else:
        return word + '-yay'


# --------------------------------------------------
if __name__ == '__main__':
    main()
