#!/usr/bin/env python3
"""Adding things that don't belong"""

def add(a, b):
    """Add two numbers or two strings or, like, whatever...  """
    return a + b

for (x, y) in [(2, 3), ("2", "3"), ("2", 3), (2, "3")]:
    print("{} + {} = {}".format(x, y, add(x, y)))
