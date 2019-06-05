#!/usr/bin/env python3
"""tests for article.py"""

import re
import os
from subprocess import getstatusoutput, getoutput

prg = './article.py'
consonant_words = [
    'bear', 'cow', 'deer', 'frog', 'giraffe', 'horse', 'jackyl', 'kestrel',
    'lion', 'marmot', 'nutria', 'porpoise', 'quark', 'rooster', 'sturgeon',
    'turtle', 'vermin', 'walrus', 'xray', 'yoosy', 'zebra'
]
vowel_words = ['appaloosa', 'elephant', 'ingot', 'octopus', 'unicorn']


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
        assert re.match("usage", out, re.IGNORECASE)


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
