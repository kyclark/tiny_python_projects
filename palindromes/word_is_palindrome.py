#!/usr/bin/env python3
"""Report if the given word is a palindrome"""

import sys
import os


def main():
    """main"""
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} STR'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    word = args[0]
    rev = ''.join(reversed(word))

    print('"{}" is{} a palindrome.'.format(
        word, '' if word.lower() == rev.lower() else ' NOT'))


if __name__ == '__main__':
    main()
