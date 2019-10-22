#!/usr/bin/env python3
# Author: Ken Youens-Clark

import sys

def greet(name: str) -> str:
    return f'Hello, {name}!'

def test_greet() -> None:
    assert greet('World') == 'Hello, World!'
    assert greet('Terra Firma') == 'Hello, Terra Firma!'

def main() -> None:
    args = sys.argv[1:]
    print(greet(args))

if __name__ == '__main__':
    main()
