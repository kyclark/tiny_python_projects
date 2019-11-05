#!/usr/bin/env python3
# Purpose: Say hello

import sys

def greet(name: str) -> str:  # "name" is a str, function returns a str
    return f'Hello, {name}!'

def test_greet() -> None:     # function returns None
    assert greet('World') == 'Hello, World!'
    assert greet('Terra Firma') == 'Hello, Terra Firma!'

def main() -> None:           # function returns None
    args = sys.argv[1:]
    print(greet(args))

if __name__ == '__main__':
    main()
