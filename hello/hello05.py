#!/usr/bin/env python3
# Purpose: Say hello

import sys

def greet(name):                    # a function to create a greeting
    return f'Hello, {name}!'

def test_greet():                   # a function to test the "greet" function
    assert greet('World') == 'Hello, World!'
    assert greet('Terra Firma') == 'Hello, Terra Firma!'

args = sys.argv[1:]                 # program starts here
name = args[0] if args else 'World' # if expression
print(greet(name))                  # "print" and "greet" are separated
