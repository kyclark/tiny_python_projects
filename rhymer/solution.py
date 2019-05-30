#!/usr/bin/env python3
"""Make rhyming words"""

import argparse
import re
import string
import sys
from dire import die


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='str', help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    word = args.word

    vowels = 'aeiou'
    if word[0] in vowels:
        die('Word "{}" must start with consonants'.format(word))

    consonants = [c for c in string.ascii_lowercase if c not in 'aeiou']
    match = re.match('^([' + ''.join(consonants) + ']+)(.+)', word)

    clusters = ('bl br ch cl cr dr fl fr gl gr pl pr sc '
                'sh sk sl sm sn sp st sw th tr tw wh wr '
                'sch scr shr sph spl spr squ str thr').split()

    if match:
        start, rest = match.group(1), match.group(2)
        for c in filter(lambda c: c != start, consonants + clusters):
            print(c + rest)


# --------------------------------------------------
if __name__ == '__main__':
    main()
