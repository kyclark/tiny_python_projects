#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
invalid_words = ['1one', '#hash', '1#both']
side = 'larboard'
template = 'Ahoy, Captain, {} {} off the {} bow!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_word_alpha():
    """sighting must start with alpha character"""

    for word in invalid_words:
        rv, out = getstatusoutput(f'{prg} {word}')
        assert rv == 2
        assert out.lower().startswith('usage')

# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word, 'larboard', side)


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> A Brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('A', word.title(), 'larboard', side)


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word, 'larboard', side)


# --------------------------------------------------
def test_vowel_upper():
    """Octopus -> An Octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == template.format('An', word.upper(), 'larboard', side)

# --------------------------------------------------
def test_starboard():
    """--side starboard -> starboard"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word} --side starboard')
        assert out.strip() == template.format('a', word, 'starboard', side)