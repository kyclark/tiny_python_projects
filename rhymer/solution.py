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
    consonants = ''.join([c for c in string.ascii_lowercase if c not in vowels])
    pattern = ('([' + consonants + ']+)?' # capture one or more, optional
               '('                        # start capture
               '[' + vowels + ']'         # at least one vowel
               '.*'                       # zero or more of by anything else
               ')?')                      # end capture, optional group
    match = re.match(pattern, word, re.IGNORECASE)
    return (match.group(1) or '', match.group(2) or '') if match else ('', '')

    # word = word.lower()
    # pos = list(
    #     filter(lambda v: v >= 0,
    #            map(lambda c: word.index(c) if c in word else -1, vowels)))
    # if pos:
    #     first = min(pos)
    #     return (word[:first], word[first:])
    # else:
    #     return (word, '')


# --------------------------------------------------
def test_stemmer():
    """test the stemmer"""

    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('apple') == ('', 'apple')
    assert stemmer('bbb') == ('bbb', '')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()

    start, rest = stemmer(args.word.lower())
    if rest:
        print('\n'.join(sorted([p + rest for p in prefixes if p != start])))
    else:
        print('Cannot rhyme "{}"'.format(args.word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
