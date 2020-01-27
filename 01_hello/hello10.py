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
    val = args[0] if args else ''
    if len(args) != 1 or val == '-h' or val == '--help':
        prg_name = os.path.basename(sys.argv[0])
        print(f'usage: {prg_name} NAME')
    else:
        print(greet(val))

if __name__ == '__main__':
    main()
