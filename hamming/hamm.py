#!/usr/bin/env python3
"""Hamming distance"""

import argparse
import logging
import os
from dire import die


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files', metavar='FILE', nargs=2, help='File inputs')

    parser.add_argument('-d', '--debug', help='Debug', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def read_file(file):
    """Return the contents of a file"""

    if not os.path.isfile(file):
        die('"{}" is not a file'.format(file))

    return open(file).read().split()


# --------------------------------------------------
def dist(s1, s2):
    """Given two strings, return the Hamming distance (int)"""

    d = abs(len(s1) - len(s2)) + sum(
        map(lambda p: 0 if p[0] == p[1] else 1, zip(s1, s2)))

    logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1, s2, d))

    return d

    # hamm = abs(len(s1) - len(s2))

    # for c1, c2 in zip(s1, s2):
    #     if c1 != c2:
    #         hamm += 1

    # hamm += sum(map(lambda p: 0 if p[0] == p[1] else 1, zip(s1, s2)))

    # return hamm


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file1, file2 = args.files

    logging.basicConfig(
        filename='.log',
        filemode='w',
        style='{',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    logging.debug('file1 = {}, file2 = {}'.format(file1, file2))

    words1 = read_file(file1)
    words2 = read_file(file2)

    distance = sum(map(lambda t: dist(*t), zip(words1, words2)))

    #distance = sum(map(dist, zip(words1, words2)))

    # distance = 0
    # for w1, w2 in zip(words1, words2):
    #     distance += dist(w1, w2)

    print(distance)


# --------------------------------------------------
def test_dist():
    """dist ok"""

    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC', 9),
             ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n


# --------------------------------------------------
if __name__ == '__main__':
    main()
