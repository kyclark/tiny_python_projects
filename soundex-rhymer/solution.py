#!/usr/bin/env python3

import argparse
import re
import soundex
import string
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Use Soundex to find rhyming words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='str', help='Word')

    parser.add_argument('-w',
                        '--wordlist',
                        metavar='str',
                        help='Wordlist',
                        default='/usr/share/dict/words')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    word = args.word
    wordlist = args.wordlist

    stem = word
    consonants = [c for c in string.ascii_lowercase if c not in 'aeiou']
    regex = re.compile('^[' + ''.join(consonants) + ']+(.+)')

    def stemmer(word):
        match = regex.search(word)
        return match.group(1) if match else word

    sndx = soundex.Soundex()
    cmp = sndx.soundex(stemmer(word))

    for line in open(wordlist):
        for w in line.split():
            if w != word and sndx.soundex(stemmer(w)) == cmp:
                print(w)


# --------------------------------------------------
if __name__ == '__main__':
    main()
