#!/usr/bin/env python3
"""Twelve Days of Christmas"""

import argparse
import emoji
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    if args.num not in range(1, 13):
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    verses = map(verse, range(1, args.num + 1))
    print(emoji.emojize('\n\n'.join(verses)), file=args.outfile)


# --------------------------------------------------
def verse(day):
    """Create a verse"""

    ordinal = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
    ]

    gifts = [
        'A :bird: in a pear tree.',
        'Two turtle :bird:s,',
        'Three French :bird:s,',
        'Four calling :bird:s,',
        'Five gold :ring:s,',
        'Six :bird:s a laying,',
        'Seven :bird:s a swimming,',
        'Eight :woman:s a milking,',
        'Nine :woman:s dancing,',
        'Ten :man:s a leaping,',
        'Eleven :man:s piping,',
        'Twelve :drum:s drumming,',
    ]

    lines = [
        f'On the {ordinal[day - 1]} day of Christmas,',
        'My true love gave to me,'
    ]

    lines.extend(reversed(gifts[:day]))

    if day > 1:
        lines[-1] = 'And ' + lines[-1].lower()

    return '\n'.join(lines)


# --------------------------------------------------
def test_verse():
    """Test verse"""

    assert verse(1) == '\n'.join([
        'On the first day of Christmas,', 'My true love gave to me,',
        'A :bird: in a pear tree.'
    ])

    assert verse(2) == '\n'.join([
        'On the second day of Christmas,', 'My true love gave to me,',
        'Two turtle :bird:s,', 'And a :bird: in a pear tree.'
    ])


# --------------------------------------------------
if __name__ == '__main__':
    main()
