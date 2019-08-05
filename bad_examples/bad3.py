#!/usr/bin/env python3
"""Bad scoping"""

import sys

args = sys.argv[1:]

if args:
    var = "foo"

print("var = {}".format(var))
