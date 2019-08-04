#!/usr/bin/env python3
"""Convert text to Pig Latin"""

import argparse
import os
import re
import string
import textwrap


# --------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Convert to Pig Latin',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='str',
                        type=str,
                        default='out-yay')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")

    num_files = 0
    for i, fh in enumerate(args.file, start=1):
        basename = os.path.basename(fh.name)
        out_file = os.path.join(out_dir, basename)
        print('{:3}: {}'.format(i, basename))

        num_files += 1
        out_fh = open(out_file, 'wt')
        for line in fh:
            out_fh.write(''.join(map(pig, splitter.split(line))))
        out_fh.close()

    print('Done, wrote {} file{} to "{}".'.format(
        num_files, '' if num_files == 1 else 's', out_dir))


# --------------------------------------------------
def pig(word):
    """Create Pig Latin version of a word"""

    if re.match(r"^[\w']+$", word):
        vowels = 'aeiouAEIOU'
        consonants = re.sub('[' + vowels + ']', '', string.ascii_letters)
        match = re.match('^([' + consonants + ']+)(['+ vowels + '].*)', word)
        if match:
            word = '-'.join([match.group(2), match.group(1) + 'ay'])
        else:
            word = word + '-yay'
    return word

# --------------------------------------------------
def test_pig():
    """Test pig"""

    assert pig(' ') == ' '
    assert pig(', ') == ', '
    assert pig('\n') == '\n'
    assert pig('a') == 'a-yay'
    assert pig('i') == 'i-yay'
    assert pig('apple') == 'apple-yay'
    assert pig('cat') == 'at-cay'
    assert pig('chair') == 'air-chay'
    assert pig('the') == 'e-thay'
    assert list(map(pig, ['foo', '\n'])) == ['oo-fay', '\n']


# --------------------------------------------------
if __name__ == '__main__':
    main()
