#!/usr/bin/env python3
"""tests for article.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './article.py'
consonant_words = [
    'bear', 'cow', 'dragon', 'frog', 'giraffe', 'horse', 'jackyl', 'kestrel',
    'lion', 'marmot', 'nutria', 'porpoise', 'quark', 'rooster', 'sturgeon',
    'turtle', 'vermin', 'walrus', 'xolo', 'yak', 'zebra'
]
vowel_words = ['appaloosa', 'elephant', 'ingot', 'octopus', 'ungulate']


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """ bear -> a bear """

    for word in consonant_words:
        out = getoutput('{} {}'.format(prg, word))
        assert out.strip() == 'a ' + word


# --------------------------------------------------
def test_02():
    """ Bear -> a Bear """

    for word in consonant_words:
        out = getoutput('{} {}'.format(prg, word.title()))
        assert out.strip() == 'a ' + word.title()


# --------------------------------------------------
def test_03():
    """ octopus -> an octopus """

    for word in vowel_words:
        out = getoutput('{} {}'.format(prg, word))
        assert out.strip() == 'an ' + word


# --------------------------------------------------
def test_04():
    """ Octopus -> an Octopus """

    for word in vowel_words:
        out = getoutput('{} {}'.format(prg, word.title()))
        assert out.strip() == 'an ' + word.title()
