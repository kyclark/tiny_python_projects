#!/usr/bin/env python3
# Author: Ken Youens-Clark

import sys

def greet(name):
    return f'Hello, {name}!'

def test_greet():
    assert greet('World') == 'Hello, World!'
    assert greet('Terra Firma') == 'Hello, Terra Firma!'

def main():
    args = sys.argv[1:]
    name = args[0] if args else 'World'
    print(greet(name)) 

if __name__ == '__main__':
    main()
