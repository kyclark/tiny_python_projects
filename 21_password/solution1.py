#!/usr/bin/env python3
"""Password maker, https://xkcd.com/936/"""

import argparse
import random
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='*',
                        help='Input file(s)',
                        default=[open('/usr/share/dict/words')])

    parser.add_argument('-n',
                        '--num',
                        metavar='int',
                        type=int,
                        default=3,
                        help='Number of passwords to generate')

    parser.add_argument('-w',
                        '--num_words',
                        metavar='int',
                        type=int,
                        default=4,
                        help='Number of words to use for password')

    parser.add_argument('-m',
                        '--min_word_len',
                        metavar='int',
                        type=int,
                        default=4,
                        help='Minimum word length')

    parser.add_argument('-s',
                        '--seed',
                        metavar='int',
                        type=int,
                        help='Random seed')

    parser.add_argument('-l',
                        '--l33t',
                        action='store_true',
                        help='Obsfuscate letters')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    for fh in args.file:
        for line in fh:
            for word in filter(lambda w: len(w) >= args.min_word_len,
                               map(clean,
                                   line.lower().split())):
                words.add(word.title())

    words = sorted(words)
    passwords = []
    for _ in range(args.num):
        passwords.append(''.join(random.sample(words, args.num_words)))

    for password in passwords:
        print(l33t(password) if args.l33t else password)


# --------------------------------------------------
def clean(word):
    """Remove non-word characters from word"""

    return re.sub('[^a-zA-Z]', '', word)


# --------------------------------------------------
def l33t(text):
    """l33t"""

    text = ransom(text)
    xform = str.maketrans({
        'a': '@', 'A': '4', 'O': '0', 't': '+', 'E': '3', 'I': '1', 'S': '5'
    })
    return text.translate(xform) + random.choice(string.punctuation)


# --------------------------------------------------
def ransom(text):
    """Randomly choose an upper or lowercase letter to return"""

    return ''.join(
        map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(), text))


# --------------------------------------------------
if __name__ == '__main__':
    main()
