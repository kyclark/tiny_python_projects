#!/usr/bin/env python3

import random
import re
from itertools import chain

# --------------------------------------------------
def scramble(word):
    """For words over 3 characters, shuffle the letters in the middle"""

    if re.match(r"^[\w']+$", word):
        if len(word) > 3:
            orig = list(word[1:-1])
            middle = orig.copy()
            while middle == orig:
                random.shuffle(middle)
            word = word[0] + ''.join(middle) + word[-1]

    return word

def splitter(s, regex):
    spans = [m.span() for m in regex.finditer(s)]
    gaps = list(chain(*spans))
    if gaps[0] != 0: gaps.insert(0, 0)
    if gaps[-1] != len(s):
        gaps.append(len(s))

    return [s[gaps[i]:gaps[i+1]] for i in range(0, len(gaps) - 1)]
    # bits = []
    # for i in range(0, len(gaps) - 1):
    #     bits.append(s[gaps[i]:gaps[i+1]])

    # return bits

def main():
    s = """
    He said, "Please, leave me alone!" I wasn't sure if
    he was crazy. What could happen? Where would he go?
    """

    #for x in re.findall(r"[\w']+|[^\w\s]", s, re.UNICODE):
    #    if re.match(r"^[\w']+$", x):
    #        print('word = "{}"'.format(x))
    #    else:
    #        print('punc = "{}"'.format(x))

    regex = re.compile(r"([a-zA-Z']+)")
    print(''.join(map(scramble, splitter(s, regex))))

main()
