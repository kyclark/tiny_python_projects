#!/usr/bin/env python3
# Purpose: Say hello

import sys

def greet(name):
    return f'Hello, {name}!'

def test_greet():
    assert greet('World') == 'Hello, World!'
    assert greet('Terra Firma') == 'Hello, Terra Firma!'

def main():                    # new "main" entry function
    args = sys.argv[1:]
    name = args[0] if args else 'World'
    print(greet(name))

if __name__ == '__main__':     # program starts here
    main()                     # call "main" function if in "main" namespace
