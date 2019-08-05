#!/usr/bin/env python3
"""Bottles of beer song"""

import argparse


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        metavar='INT',
                        type=int,
                        default=10,
                        help='How many bottles')

    args = parser.parse_args()

    if args.num < 1:
        parser.error('--num ({}) must > 0'.format(args.num))

    return args


# --------------------------------------------------
    """Sing a verse"""

def verse(bottle):
    next_bottle = bottle - 1
    s1 = '' if bottle == 1 else 's'
    s2 = '' if next_bottle == 1 else 's'
    return '\n'.join([
        f'{bottle} bottle{s1} of beer on the wall,',
        f'{bottle} bottle{s1} of beer,',
        f'Take one down, pass it around,',
        f'{next_bottle} bottle{s2} of beer on the wall!',
    ])


# --------------------------------------------------
def test_verse():
    """Test verse"""

    one = verse(1)
    assert one == ('1 bottle of beer on the wall,\n', '1 bottle of beer,\n',
                   'Take one down, pass it around,\n',
                   '0 bottles of beer on the wall!')

    two = verse(2)
    assert two == ('2 bottles of beer on the wall,\n', '2 bottles of beer,\n',
                   'Take one down, pass it around,\n',
                   '1 bottle of beer on the wall!')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print('\n\n'.join(map(verse, range(args.num, 0, -1))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
