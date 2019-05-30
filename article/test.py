#!/usr/bin/env python3
"""tests for article.py"""

import re
import os
import random
from subprocess import getstatusoutput, getoutput

prg = './article.py'


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

    out = getoutput('{} bear'.format(prg))
    assert out.strip() == 'a bear'


# --------------------------------------------------
def test_02():
    """ Bear -> a Bear """

    out = getoutput('{} Bear'.format(prg))
    assert out.strip() == 'a Bear'


# --------------------------------------------------
def test_03():
    """ octopus -> an octopus """

    out = getoutput('{} octopus'.format(prg))
    assert out.strip() == 'an octopus'


# --------------------------------------------------
def test_04():
    """ Octopus -> an Octopus """

    out = getoutput('{} Octopus'.format(prg))
    assert out.strip() == 'an Octopus'
