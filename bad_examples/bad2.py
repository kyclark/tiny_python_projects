#!/usr/bin/env python3
"""Misspelled variable"""

import sys

args = sys.argv[1:]
name = "World"

if args:
    nmae = args[0]

print("Hello, {}!".format(name))
