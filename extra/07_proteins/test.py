#!/usr/bin/env python3
"""tests for translate.py"""

from subprocess import getstatusoutput
import os.path
import re
import string
import random

prg = './translate.py'
dna = 'gaactacaccgttctcctggt'
rna = 'UGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGAA'


# --------------------------------------------------
def random_filename():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


# --------------------------------------------------
def test_exists():
    """usage"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_no_args():
    """die on no args"""

    rv, out = getstatusoutput(prg)
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_missing_input():
    """die on missing input"""

    rv, out = getstatusoutput('{} -c codons.rna'.format(prg))
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_missing_codons():
    """die on missing codons"""

    rv, out = getstatusoutput('{} {}'.format(prg, dna))
    assert rv > 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_codon_file():
    """die on bad codon_file"""

    bad = random_filename()
    rv, out = getstatusoutput('{} --codons {} {}'.format(prg, bad, dna))
    assert rv > 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_good_input1():
    """runs on good input"""

    run(rna, 'codons.rna', 'WPWRPELRSIVPVLTGE')


# --------------------------------------------------
def test_good_input2():
    """runs on good input"""

    run(dna, 'codons.dna', 'ELHRSPG')


# --------------------------------------------------
def test_good_input3():
    """runs on good input"""

    run(rna, 'codons.dna', '-P-RPE-R---P--T-E')


# --------------------------------------------------
def test_good_input4():
    """runs on good input"""

    run(dna, 'codons.rna', 'E-H----')


# --------------------------------------------------
def run(input_seq, codons, expected):
    """runs ok"""

    random_file = random_filename()
    try:
        flip = random.randint(0, 1)
        out_file, out_arg = (random_file,
                             '-o ' + random_file) if flip == 1 else ('out.txt',
                                                                     '')
        print(f'{prg} -c {codons} {out_arg} {input_seq}')
        rv, output = getstatusoutput(f'{prg} -c {codons} {out_arg} {input_seq}')

        assert rv == 0
        assert output.rstrip() == f'Output written to "{out_file}".'
        assert os.path.isfile(out_file)
        assert open(out_file).read().strip() == expected
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)

