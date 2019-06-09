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
    cell = 0
    for line in map(str.rstrip, fh):
        if line == '':
            read = 'words'
            continue

        if read == 'puzzle':
            row = []
            for char in list(line):
                cell += 1
                row.append((char, cell))

            puzzle.append(row)
        else:
            words.append(line.replace(' ', ''))

    return puzzle, words


# --------------------------------------------------
def all_combos(puzzle):
    """Find all combos in puzzle"""

    num_rows = len(puzzle)
    num_cols = len(puzzle[0])
    combos = []

    # Horizontal
    for row in puzzle:
        combos.append(row)

    # Vertical
    for col_num in range(num_cols):
        col = [puzzle[row_num][col_num] for row_num in range(num_rows)]
        combos.append(col)

    # Diagonals Up
    for row_i in range(1, num_rows):
        diag = []
        col_num = 0
        for row_j in range(row_i, -1, -1):
            diag.append(puzzle[row_j][col_num])
            col_num += 1

        if diag:
            combos.append(diag)

    for col_i in range(1, num_cols):
        diag = []

        col_num = col_i
        for row_num in range(num_rows - 1, -1, -1):
            diag.append(puzzle[row_num][col_num])
            col_num += 1
            if col_num == num_cols:
                break

        if diag:
            combos.append(diag)

    # Diagonals Down
    for row_i in range(0, num_rows):
        diag = []
        col_num = 0
        for row_j in range(row_i, num_rows):
            diag.append(puzzle[row_j][col_num])
            col_num += 1
            if col_num == num_cols:
                break

        if diag:
            combos.append(diag)

    for col_i in range(1, num_cols):
        diag = []

        col_num = col_i
        for row_num in range(0, num_rows):
            diag.append(puzzle[row_num][col_num])
            col_num += 1
            if col_num == num_cols:
                break

        if diag:
            combos.append(diag)

    combos.extend([list(reversed(c)) for c in combos])
    return combos


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    puzzle, words = read_puzzle(args.file)
    combos = all_combos(puzzle)
    found = set()

    def fst(t):
        return t[0]

    def snd(t):
        return t[1]

    reveal = set()
    for word in words:
        for combo in combos:
            test = ''.join(map(fst, combo))
            if word in test:
                start = test.index(word)
                end = start + len(word)
                for cell in map(snd, combo[start:end]):
                    reveal.add(cell)
                found.add(word)

    for row in puzzle:
        cells = [c[0] if c[1] in reveal else '.' for c in row]
        print(''.join(cells))

    missing = [w for w in words if not w in found]
    if missing:
        print('Failed to find:')
        for i, word in enumerate(missing, 1):
            print('{:3}: {}'.format(i, word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
