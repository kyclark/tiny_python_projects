#!/usr/bin/env python3
"""Gematria"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        print(' '.join(map(word2num, line.split())))


# --------------------------------------------------
def word2num(word):
    """Sum the ordinal values of all the characters"""
    word2numList=[]
    sum=0
    for i in word:
        asciinumber=ord(i)
        if (i>47 and i<58) or  (i>64 and i<123) :
            sum+=asciinumber
        else:
            if i==32:
                word2numList.append(sum)
                sum=0
      
    return word2numList


# --------------------------------------------------
def test_word2num():
    """Test word2num"""

    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"


# --------------------------------------------------
if __name__ == '__main__':
    main()
