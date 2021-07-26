#!/usr/bin/env python3
"""tests for telephone.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re
import string

prg = "./telephone.py"
fox = "../inputs/fox.txt"
now = "../inputs/now.txt"


# --------------------------------------------------
def seed_parameter():
    """Either -s or --seed"""

    return "-s" if random.randint(0, 1) else "--seed"


# --------------------------------------------------
def mutations_parameter():
    """Either -m or --mutations"""

    return "-m" if random.randint(0, 1) else "--mutations"


# --------------------------------------------------


def insertions_parameter():
    """Either -i or --insertions"""

    return "-i" if random.randint(0, 1) else "--insertions"


# --------------------------------------------------
def deletions_parameter():
    """Either -d or --deletions"""

    return "-d" if random.randint(0, 1) else "--deletions"


# --------------------------------------------------
def words_parameter():
    """Either -w or --words"""

    return "-w" if random.randint(0, 1) else "--words"


# --------------------------------------------------
def characters_parameter():
    """Either -c or --characters"""

    return "-c" if random.randint(0, 1) else "--characters"


# --------------------------------------------------
def output_parameter():
    """Either -o or --output"""

    return "-o" if random.randint(0, 1) else "--output"


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return "".join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["", "-h", "--help"]:
        out = getoutput(f"{prg} {flag}")
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_seed_str():
    """bad seed str value"""

    bad = random_string()
    rv, out = getstatusoutput(f"{prg} {seed_parameter()} {bad} {fox}")
    assert rv > 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_mutations_str():
    """bad mutations str value"""

    bad = random_string()
    rv, out = getstatusoutput(f"{prg} {mutations_parameter()} {bad} {fox}")
    assert rv > 0
    assert re.search(f"invalid float value: '{bad}'", out)


# --------------------------------------------------
def test_bad_insertions_str():
    """bad insertions str value"""

    bad = random_string()
    rv, out = getstatusoutput(f"{prg} {insertions_parameter()} {bad} {fox}")
    assert rv > 0
    assert re.search(f"invalid float value: '{bad}'", out)


# --------------------------------------------------
def test_bad_deletions_str():
    """bad deletions str value"""

    bad = random_string()
    rv, out = getstatusoutput(f"{prg} {deletions_parameter()} {bad} {fox}")
    assert rv > 0
    assert re.search(f"invalid float value: '{bad}'", out)


# --------------------------------------------------
def test_bad_words_str():
    """bad words str value"""

    bad = random_string()
    rv, out = getstatusoutput(f"{prg} {words_parameter()} {bad} {fox}")
    assert rv > 0
    assert re.search(f"invalid float value: '{bad}'", out)


# --------------------------------------------------
def test_bad_mutations():
    """bad mutations values"""

    for val in ["-1.0", "10.0"]:
        rv, out = getstatusoutput(f"{prg} {mutations_parameter()} {val} {fox}")
        assert rv > 0
        assert re.search(f'--mutations "{val}" must be between 0 and 1', out)


# --------------------------------------------------
def test_bad_insertions():
    """bad insertions values"""

    for val in ["-1.0", "10.0"]:
        rv, out = getstatusoutput(f"{prg} {insertions_parameter()} {val} {fox}")
        assert rv > 0
        assert re.search(f'--insertions "{val}" must be between 0 and 1', out)


# --------------------------------------------------
def test_bad_deletions():
    """bad deletions values"""

    for val in ["-1.0", "10.0"]:
        rv, out = getstatusoutput(f"{prg} {deletions_parameter()} {val} {fox}")
        assert rv > 0
        assert re.search(f'--deletions "{val}" must be between 0 and 1', out)


# --------------------------------------------------
def test_bad_words():
    """bad words values"""

    for val in ["-1.0", "10.0"]:
        rv, out = getstatusoutput(f"{prg} {words_parameter()} {val} {fox}")
        assert rv > 0
        assert re.search(f'--words "{val}" must be between 0 and 1', out)


# --------------------------------------------------
def test_for_mutation_echo():
    """test mutation echo"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(f'{prg} {mutations_parameter()} 0 "{txt}"')
    assert rv == 0
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{txt}"'


# --------------------------------------------------
def test_for_insertion_echo():
    """test insertion echo"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(
        f'{prg} {mutations_parameter()} 0 {insertions_parameter()} 0 "{txt}"'
    )
    assert rv == 0
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{txt}"'


# --------------------------------------------------
def test_for_deletion_echo():
    """test deletion echo"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(
        f'{prg} {mutations_parameter()} 0 {deletions_parameter()} 0 "{txt}"'
    )
    assert rv == 0
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{txt}"'


# --------------------------------------------------
def test_for_words_echo():
    """test word echo"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(
        f'{prg} {mutations_parameter()} 0 {words_parameter()} 0 "{txt}"'
    )
    assert rv == 0
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{txt}"'


# --------------------------------------------------
def test_o():
    """test output parameter"""

    txt = open(now).read().rstrip()
    out_name = random_string() + ".txt"
    rv, out = getstatusoutput(
        f'{prg} {mutations_parameter()} 0 "{txt}" {output_parameter()} {out_name}'
    )
    assert rv == 0
    expected = open(out_name).read().rstrip()
    assert expected.rstrip() == f'You said: "{txt}"\nI heard : "{txt}"'
    os.remove(out_name)


# --------------------------------------------------
def test_now_cmd_s1():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(f'{prg} {seed_parameter()} 1 "{txt}"')
    assert rv == 0
    expected = """
    Now is the time for all good men to come to the aid of the party$
    """.strip()
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_now_cmd_s1_insertion():
    """test insertion"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(
        f'{prg} {seed_parameter()} 1 {mutations_parameter()} 0 {insertions_parameter()} 0.1 "{txt}"'
    )
    assert rv == 0
    expected = """
    Now is the time for all good men to come to the aid of the party$.
    """.strip()
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_now_cmd_s1_deletion():
    """test deletion"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(
        f'{prg} {seed_parameter()} 1 {mutations_parameter()} 0 {deletions_parameter()} 0.1 "{txt}"'
    )
    assert rv == 0
    expected = """
    Now is the time for all good men to come to the aid of the party
    """.strip()
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_now_cmd_s1_word():
    """test word no changes"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(
        f'{prg} {seed_parameter()} 1 {mutations_parameter()} 0 {words_parameter()} 0.1 "{txt}"'
    )
    assert rv == 0
    expected = """
    Now is the time for all good men to come to the aid of the party.
    """.strip()
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_c():
    """test characters flag"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(
        f'{prg} {seed_parameter()} 1 {mutations_parameter()} 0.5 {characters_parameter()} "{txt}"'
    )
    assert rv == 0
    expected = """
    Poh if OhW tSmB pLr awH gouh STn tg coeC wo trL aFc yf Xfe TaruyC
    """.strip()
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_c_insertion():
    """test insertion"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(
        f'{prg} {seed_parameter()} 1 {mutations_parameter()} 0 {insertions_parameter()} 0.5 {(characters_parameter())} "{txt}"'
    )
    assert rv == 0
    expected = """
    ONoww ifs tOher tSimBe foprG aulSl ugotod meqnM tSo comgeZ toC vthez aqidL ojf cthqe hpZartXy.
    """.strip()
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_now_cmd_s2_m4():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(
        f'{prg} {seed_parameter()} 2 {mutations_parameter()} .4 "{txt}"'
    )
    assert rv == 0
    expected = """
    No@ Is $he tAm< fol aml g`oo mwn tY gom^ io tke aim oe tWe partej
    """.strip()
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_fox_file_s1():
    """test"""

    rv, out = getstatusoutput(f"{prg} {seed_parameter()} 1 {fox}")
    assert rv == 0
    txt = open(fox).read().rstrip()
    expected = "The quick brown fox jumps over the lazy dog."
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


# --------------------------------------------------
def test_fox_file_s2_m6():
    """test"""

    rv, out = getstatusoutput(
        f"{prg} {seed_parameter()} 2 {mutations_parameter()} .6 {fox}"
    )
    assert rv == 0
    txt = open(fox).read().rstrip()
    expected = "TMl$qn[akrT$owA<fsldjuYXd^ovJnNtegslTzGydQR."
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'
