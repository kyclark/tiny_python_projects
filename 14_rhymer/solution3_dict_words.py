#!/usr/bin/env python3
"""Make rhyming words"""

import argparse
import io
from pydash import flatten


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='str', help='A word to rhyme')

    parser.add_argument('-w',
                        '--wordlist',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='/usr/share/dict/words',
                        help='Wordlist to verify authenticity')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()

    dict_words = read_wordlist(args.wordlist)

    def is_dict_word(word):
        return word.lower() in dict_words if dict_words else True

    start, rest = stemmer(args.word)
    if rest:
        print('\n'.join(
            sorted(
                filter(is_dict_word,
                       [p + rest for p in prefixes if p != start]))))
    else:
        print(f'Cannot rhyme "{args.word}"')


# --------------------------------------------------
def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""

    word = word.lower()
    pos = list(
        filter(lambda v: v >= 0,
               map(lambda c: word.index(c) if c in word else -1, 'aeiou')))
    if pos:
        first = min(pos)
        return (word[:first], word[first:])
    else:
        return (word, '')


# --------------------------------------------------
def test_stemmer():
    """test the stemmer"""

    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')


# --------------------------------------------------
def read_wordlist(fh):
    """Read the wordlist file"""

    return set(
        flatten([line.lower().strip().split() for line in fh] if fh else []))


# --------------------------------------------------
def test_read_wordlist():
    """test"""

    assert read_wordlist(io.StringIO('foo\nbar\nfoo')) == set(['foo', 'bar'])
    assert read_wordlist(io.StringIO('foo bar\nbar foo\nfoo')) == set(
        ['foo', 'bar'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
