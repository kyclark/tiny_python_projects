#!/usr/bin/env python3
# Author: Ken Youens-Clark

import os, sys

def greet(name: str) -> str:
    return f'Hello, {name}!'

def test_greet() -> None:
    assert greet('World') == 'Hello, World!'
    assert greet('Terra Firma') == 'Hello, Terra Firma!'

def main() -> None:
    args = sys.argv[1:]
    if len(args) != 1:
        prg_name = os.path.basename(sys.argv[0])
        print(f'usage: {prg_name} NAME')
        sys.exit(1)
    else:
        print(greet(args[0]))

if __name__ == '__main__':
    main()
