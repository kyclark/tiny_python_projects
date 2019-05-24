#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-05-22
Purpose: Rock the Casbah
"""

import argparse
import soundex
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='str', help='Word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    word = args.word
    sndx = soundex.Soundex()
    cmp = sndx.soundex(word)
    wordlist = '/usr/share/dict/words'

    for line in open(wordlist):
        for w in line.split():
            #print(' '.join([word, w, cmp, sndx.soundex(w)]))
            if sndx.soundex(w) == cmp:
                print(w)

# --------------------------------------------------
if __name__ == '__main__':
    main()
