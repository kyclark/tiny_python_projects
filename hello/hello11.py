#!/usr/bin/env python3
# Purpose: Say hello

import argparse, os, sys

def greet(name: str) -> str:
    return f'Hello, {name}!'

def test_greet() -> None:
    assert greet('World') == 'Hello, World!'
    assert greet('Terra Firma') == 'Hello, Terra Firma!'

def main() -> None:
    # create argument parser
    parser = argparse.ArgumentParser(
        description='Say hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # add "name" parameter
    parser.add_argument('name', help='Name to greet')

    # get the parsed arguments
    args = parser.parse_args()

    # greet the "name" value inside "args"
    print(greet(args.name))

if __name__ == '__main__':
    main()
