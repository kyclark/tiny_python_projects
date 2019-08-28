#!/usr/bin/env python3
"""Make rhyming words"""

import argparse
import re
import string


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='str', help='A word to rhyme')

    return parser.parse_args()


# --------------------------------------------------
def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""

    vowels = 'aeiou'
    consonants = ''.join(
        filter(lambda c: c not in vowels, string.ascii_lowercase))
    match = re.match('^([' + consonants + ']*)([' + vowels + '].*)', word)
    return match.groups() if match else (word, '')


# --------------------------------------------------
def test_stemmer():
    """Test the stemmer"""

    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('apple') == ('', 'apple')
    assert stemmer('bbb') == ('bbb', '')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    word = args.word
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw wh wr'
        'sch scr shr sph spl spr squ str thr').split()

    start, rest = stemmer(word.lower())
    if rest:
        print('\n'.join([p + rest for p in prefixes if p != start]))
    else:
        print('Cannot rhyme "{}"'.format(word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
