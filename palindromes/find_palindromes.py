#!/usr/bin/env python3
"""Report if the given word is a palindrome"""

import sys
import os


def main():
    """main"""
    args = sys.argv[1:]
    min_length = 3

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]

    if not os.path.isfile(file):
        print('"{}" is not a file'.format(file))
        sys.exit(1)

    for line in open(file):
        for word in line.lower().split():
            # skip short words
            if len(word) >= min_length:
                rev = ''.join(reversed(word))
                if rev == word:
                    print(word)


if __name__ == '__main__':
    main()
