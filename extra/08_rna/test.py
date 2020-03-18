#!/usr/bin/env python3
"""tests for transcribe.py"""

from subprocess import getstatusoutput
import os.path
import re
import string
import random
from shutil import rmtree

prg = './transcribe.py'
input1 = './inputs/input1.txt'
input2 = './inputs/input2.txt'


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
def test_bad_file():
    """die on missing input"""

    bad = random_filename()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.match('usage:', out, re.I)
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_good_input1():
    """runs on good input"""

    out_dir = 'out'
    try:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

        rv, out = getstatusoutput(f'{prg} {input1}')
        assert rv == 0
        assert out == 'Done, wrote 1 sequence in 1 file to directory "out".'
        assert os.path.isdir(out_dir)
        out_file = os.path.join(out_dir, 'input1.txt')
        assert os.path.isfile(out_file)
        assert open(out_file).read().rstrip() == 'GAUGGAACUUGACUACGUAAAUU'

    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

# --------------------------------------------------
def test_good_input2():
    """runs on good input"""

    out_dir = random_filename()
    try:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

        rv, out = getstatusoutput(f'{prg} -o {out_dir} {input2}')
        assert rv == 0
        assert out == f'Done, wrote 2 sequences in 1 file to directory "{out_dir}".'
        assert os.path.isdir(out_dir)
        out_file = os.path.join(out_dir, 'input2.txt')
        assert os.path.isfile(out_file)
        assert open(out_file).read().rstrip() == output2().rstrip()

    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

# --------------------------------------------------
def test_good_multiple_inputs():
    """runs on good input"""

    out_dir = random_filename()
    try:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

        rv, out = getstatusoutput(f'{prg} --outdir {out_dir} {input1} {input2}')
        assert rv == 0
        assert out == f'Done, wrote 3 sequences in 2 files to directory "{out_dir}".'
        assert os.path.isdir(out_dir)
        out_file1 = os.path.join(out_dir, 'input1.txt')
        out_file2 = os.path.join(out_dir, 'input2.txt')
        assert os.path.isfile(out_file1)
        assert os.path.isfile(out_file2)
        assert open(out_file1).read().rstrip() == 'GAUGGAACUUGACUACGUAAAUU'
        assert open(out_file2).read().rstrip() == output2().rstrip()

    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

# --------------------------------------------------
def output2():
    return """CUUAGGUCAGUGGUCUCUAAACUUUCGGUUCUGUCGUCUUCAUAGGCAAAUUUUUGAACCGGCAGACAAGCUAAUCCCUGUGCGGUUAGCUCAAGCAACAGAAUGUCCGAUCUUUGAACUUCCUAACGAACCGAACCUACUAUAAUUACAUACGAAUAAUGUAUGGGCUAGCGUUGGCUCAUCAUCAAGUCUGCGGUGAAAUGGGAACAUAUUCGCAUUGCAUAUAGGGCGUAUCUGACGAUCGAUUCGAGUUGGCUAGUCGUACCAAAUGAUUAUGGGCUGGAGGGCCAAUGUAUACGUCAGCCAGGCUAAACCACUGGACCGCUUGCAAUCCAUAGGAAGUAAAAUUACCCUUUUUAAACUCUCUAAGAUGUGGCGUCUCGUUCUUAAGGAGUAAUGAGACUGUGACAACAUUGGCAAGCACAGCCUCAGUAUAGCUACAGCACCGGUGCUAAUAGUAAAUGCAAACACCGUUUCAAGAGCCGAGCCUUUUUUUAAUGCAAGGUGACUUCAGAGGGAGUAAAUCGUGGCCGGGGACUGUCCAGAGCAAUGCAUUCCCGAGUGCGGGUACCCGUGGUGUGAGAGGAAUCGAUUUCGCGUGUGAUACCAUUAAUGGUCCUGUACUACUGUCAGUCAGCUUGAUUUGAAGUCGGCCGACAAGGUUGGUACAUAAUGGGCUUACUGGGAGCUUAGGUUAGCCUCUGGAAAACUUUAGAAUUUAUAUGGGUGUUUCUGUGUUCGUACAGGCCCCAGUCGGGCCAUCGUUGUUGAGCAUAGACCGGUGUAACCUUAAUUAUUCACAGGCCAAUCCCCGUAUACGCAUCUGAAAGGCACACCGCCUAUUACCAAUUUGCGCUUCCUUACAUAGGAGGACCUGUUAUCGUCUUCUCAAUCGCUGAGUUACCUUAAAACUAGGAUC
ACCGAGUAAAAGGCGACGGUUCGUUUCCGAACCUAUUUGCUCUUAUUUCUACGGGCUGCUAGUGUUGUAGGCUGCAAAACCUACGUAGUCCCAUCUAUCAUGCUCGACCCUACGAGGCUAAUGUCUUGUCAGAGGCCCGUCAUGUGCCACGUACAUACACCAAUGUAUACCGCUCUAGCGGUUUGGUGUAGUAGGACUUGUGUAUGCACGCUACAGCGAACAACGUUGAUCCCUAACUGAAGUCGGGCUCCGCAGGCCUACUCACGCCGUUUCUAUAGGUUGAGCCGCAUCAAACAUUGGGUUGAGUCUCGAGUAUAGAGGAAGGCUCUGGUGGCAGGCGCGACGUUGAUCGGGAGGAGUAUGGAUGGUGAUCAAUCCCCGUGCCAAUCGCGAGUACUACAGGAGGAGGGGGCGGCUCUGUUCAAUCAUCACCCGUUCCAUCACACGGGCAGCACAGUUGACCUCCCGAGCCGUCUCACGGACCUAGUGGCAACAGGUGUAUUGAAGCGCCGGGAAUAGUCAUACCCGUGGGCUUGAUUGAGAGACCGAAAUUCCGACCGCCAAAACUGCUGAUAUCGUACGCCUUACUACAAAACAAAUGACGUCACUACCGGCCAGGGACAAGCUUAUUAAUUAAGUAGGAACCCUAUACCUUGCACAUCCUAAAUCUAGCAGCGGGUCCAGGAUUGGUUCCAGUCCAACGCGCGAUGCGCGUCAAGCUAGGCGAAUGACCACGGUCGAAACACCACUUAUGUGACCCACCUUGGCCAACUCUCCCGAUUCUCCUCGCUACUAUCUUGAAGGUCACUGAGAAUAUCCCUUAUGGGUCGCAUACGGAGACAGCCGCAGGAGCCUUAACGGAGAAUACGCCAAUACUAUGUUCUGGGUCGGUGGGUGUAAUGCGAUGCAAUCCGAUCGUGCGAACGUUCCCUUUGAUGACUAUAGGGUCUAGUGAUCGUACAUGUGC
    """
