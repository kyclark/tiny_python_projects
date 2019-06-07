#!/usr/bin/env python3
"""Word Search"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='The puzzle')

    return parser.parse_args()


# --------------------------------------------------
def read_puzzle(fh):
    """Read the puzzle file"""

    puzzle, words = [], []

    read = 'puzzle'
    for line in map(str.rstrip, fh):
        if line == '':
            read = 'words'
            continue

        if read == 'puzzle':
            puzzle.append(list(line))
        else:
            words.append(line)

    return puzzle, words


# --------------------------------------------------
def all_strings(puzzle):
    """Find all strings in puzzle"""

    num_rows = len(puzzle)
    num_cols = len(puzzle[0])
    strings = []

    # Horizontal
    for row in puzzle:
        strings.append(''.join(row))

    # Vertical
    for col_num in range(num_cols):
        col = [puzzle[row_num][col_num] for row_num in range(num_rows)]
        strings.append(''.join(col))

    # Diagonals
    for row_i in range(1, num_rows):
        diag = []
        col_num = 0
        for row_j in range(row_i, -1, -1):
            diag.append(puzzle[row_j][col_num])
            col_num += 1

        if diag:
            strings.append(''.join(diag))

    for col_i in range(1, num_cols - 1):
        diag = []

        col_num = col_i
        for row_num in range(num_rows - 1, -1, -1):
            diag.append(puzzle[row_num][col_num])
            col_num += 1
            if col_num == num_cols:
                break

        if diag:
            strings.append(''.join(diag))

    strings.extend([''.join(reversed(s)) for s in strings])
    return strings


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    puzzle, words = read_puzzle(args.file)
    strings = all_strings(puzzle)
    found = set()

    for word in words:
        if filter(lambda s: word in s, strings):
            print('Found "{}"'.format(word))
            found.add(word)

    missing = [w for w in words if not w in found]
    if missing:
        print('Failed to find {}: {}'.format(len(missing), ', '.join(missing)))
    else:
        print('Found all!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
