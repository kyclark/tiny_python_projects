#!/usr/bin/env python3
# Purpose: Say hello

import os
import sys

def greet(name: str) -> str:
    return f'Hello, {name}!'

def test_greet() -> None:
    assert greet('World') == 'Hello, World!'
    assert greet('Terra Firma') == 'Hello, Terra Firma!'

def main() -> None:
    args = sys.argv[1:]
    if len(args) != 1:                           # must have 1 element
        prg_name = os.path.basename(sys.argv[0]) # get program name
        print(f'usage: {prg_name} NAME')         # print usage
        sys.exit(1)                              # exit with error
    else:
        print(greet(args[0]))

if __name__ == '__main__':
    main()
