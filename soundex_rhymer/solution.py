#!/usr/bin/env python3
"""Find rhyming words using the Soundex"""

import argparse
import re
import string
from soundex import Soundex


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find rhyming words using the Soundex',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='str', help='Word')

    parser.add_argument('-w',
                        '--wordlist',
                        metavar='str',
                        help='Wordlist',
                        type=argparse.FileType('r'),
                        default='/usr/share/dict/words')

    parser.add_argument('-s',
                        '--stem',
                        help='Stem the word (remove starting consonants',
                        action='store_true')

    args = parser.parse_args()

    #if not any([c in 'aeiouy' for c in args.word.lower()]):
    if not re.search('[aeiouy]', args.word, re.IGNORECASE):
        msg = 'word "{}" must contain at least one vowel'
        parser.error(msg.format(args.word))

    return args


# --------------------------------------------------
def stemmer(s: str, stem: bool) -> str:
    """Use regular expressions"""

    if stem:
        match = re.search(r'^[^aeiou]+([aeiou].*)', s, re.IGNORECASE)
        return match.group(1) if match else s
    return s


# --------------------------------------------------
# def stemmer(s: str, stem: bool) -> str:
#     """Manually `find` first vowel"""

#     if stem:
#         positions = list(
#             filter(lambda p: p >= 0, [s.lower().find(v) for v in 'aeiou']))
#         if positions:
#             first = min(positions)
#             return s[first:] if first else s
#     return s

# --------------------------------------------------
# def stemmer(s: str, stem: bool) -> str:
#     """Manually find first vowel with generator/next"""

#     if stem:
#         first = next(
#             (t[0] for t in enumerate(s) if t[1].lower() in 'aeiou'), False)
#         return s[first:] if first else s
#     return s


# --------------------------------------------------
def test_stemmer():
    """test stemmer"""

    assert stemmer('listen', True) == 'isten'
    assert stemmer('listen', False) == 'listen'
    assert stemmer('chair', True) == 'air'
    assert stemmer('chair', False) == 'chair'
    assert stemmer('apple', True) == 'apple'
    assert stemmer('apple', False) == 'apple'
    assert stemmer('xxxxxx', True) == 'xxxxxx'
    assert stemmer('xxxxxx', False) == 'xxxxxx'

    assert stemmer('LISTEN', True) == 'ISTEN'
    assert stemmer('LISTEN', False) == 'LISTEN'
    assert stemmer('CHAIR', True) == 'AIR'
    assert stemmer('CHAIR', False) == 'CHAIR'
    assert stemmer('APPLE', True) == 'APPLE'
    assert stemmer('APPLE', False) == 'APPLE'
    assert stemmer('XXXXXX', True) == 'XXXXXX'
    assert stemmer('XXXXXX', False) == 'XXXXXX'


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    given = args.word
    words = args.wordlist.read().split()

    def sndx(s):
        return Soundex().soundex(stemmer(s, args.stem))

    wanted = sndx(given)

    for word in words:
        if given != word and sndx(word) == wanted:
            print(word)

    # print('\n'.join(
    #     filter(lambda word: given != word and sndx(word) == wanted, words)))

    # print('\n'.join([
    #     word for word in words if given != word and sndx(word) == wanted
    # ]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
