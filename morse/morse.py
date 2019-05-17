#!/usr/bin/env python3
"""
Author :    Ken Youens-Clark <kyclark@gmail.com>
Date   :    2019-04-29
Purpose:    Morse en/decoder
Background: https://en.wikipedia.org/wiki/Morse_code,
            https://en.wikipedia.org/wiki/American_Morse_code

"""

import argparse
import logging
import random
import re
import string
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Encode and decode text/Morse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'input', metavar='FILE', help='Input file or "-" for stdin')

    parser.add_argument(
        '-c',
        '--coding',
        help='Coding version',
        metavar='str',
        type=str,
        choices=['itu', 'morse'],
        default='itu')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default=None)

    parser.add_argument(
        '-d',
        '--decode',
        help='Decode message from Morse to text',
        action='store_true')

    parser.add_argument('-D', '--debug', help='Debug', action='store_true')

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
def encode_word(word, table):
    """Encode word using given table"""

    coded = []
    for char in word.upper():
        logging.debug(char)
        if char != ' ' and char in table:
            coded.append(table[char])

    encoded = ' '.join(coded)
    logging.debug('endoding "{}" to "{}"'.format(word, encoded))

    return encoded


# --------------------------------------------------
def decode_word(encoded, table):
    """Decode word using given table"""

    decoded = []
    for code in encoded.split(' '):
        if code in table:
            decoded.append(table[code])

    word = ''.join(decoded)
    logging.debug('dedoding "{}" to "{}"'.format(encoded, word))

    return word


# --------------------------------------------------
def test_encode_word():
    """Test Encoding"""

    assert encode_word('sos', ENCODE_ITU) == '... --- ...'
    assert encode_word('sos', ENCODE_MORSE) == '... .,. ...'


# --------------------------------------------------
def test_decode_word():
    """Test Decoding"""

    assert decode_word('... --- ...', DECODE_ITU) == 'SOS'
    assert decode_word('... .,. ...', DECODE_MORSE) == 'SOS'


# --------------------------------------------------
def test_roundtrip():
    """Test En/decoding"""

    random_str = lambda: ''.join(random.sample(string.ascii_lowercase, k=10))
    for _ in range(10):
        word = random_str()
        for encode_tbl, decode_tbl in [(ENCODE_ITU, DECODE_ITU),
                                       (ENCODE_MORSE, DECODE_MORSE)]:

            assert word.upper() == decode_word(
                encode_word(word, encode_tbl), decode_tbl)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    action = 'decode' if args.decode else 'encode'
    output = open(args.outfile, 'wt') if args.outfile else sys.stdout
    source = sys.stdin if args.input == '-' else open(args.input)

    coding_table = ''
    if args.coding == 'itu':
        coding_table = ENCODE_ITU if action == 'encode' else DECODE_ITU
    else:
        coding_table = ENCODE_MORSE if action == 'encode' else DECODE_MORSE

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    word_split = r'\s+' if action == 'encode' else r'\s{2}'

    for line in source:
        for word in re.split(word_split, line):
            if action == 'encode':
                print(encode_word(word, coding_table), end='  ')
            else:
                print(decode_word(word, coding_table), end=' ')
        print()


# --------------------------------------------------
def invert_dict(d):
    """Invert a dictionary's key/value"""

    #return dict(map(lambda t: list(reversed(t)), d.items()))
    return dict([(v, k) for k, v in d.items()])


# --------------------------------------------------
# GLOBALS

ENCODE_ITU = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '!': '-.-.--',
    '&': '.-...',
    ';': '-.-.-.',
    ':': '---...',
    "'": '.----.',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
}

ENCODE_MORSE = {
    'A': '.-',
    'B': '-...',
    'C': '..,.',
    'D': '-..',
    'E': '.',
    'F': '.-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '-.-.',
    'K': '-.-',
    'L': '+',
    'M': '--',
    'N': '-.',
    'O': '.,.',
    'P': '.....',
    'Q': '..-.',
    'R': '.,..',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '.-..',
    'Y': '..,..',
    'Z': '...,.',
    '0': '+++++',
    '1': '.--.',
    '2': '..-..',
    '3': '...-.',
    '4': '....-',
    '5': '---',
    '6': '......',
    '7': '--..',
    '8': '-....',
    '9': '-..-',
    '.': '..--..',
    ',': '.-.-',
    '?': '-..-.',
    '!': '---.',
    '&': '.,...',
    ';': '...,..',
    ':': '-.-,.,.',
    "'": '..-.,.-..',
    '/': '..-,-',
    '-': '....,.-..',
    '(': '.....,.-..',
    ')': '.....,..,..',
}

DECODE_ITU = invert_dict(ENCODE_ITU)
DECODE_MORSE = invert_dict(ENCODE_MORSE)

# --------------------------------------------------
if __name__ == '__main__':
    main()
