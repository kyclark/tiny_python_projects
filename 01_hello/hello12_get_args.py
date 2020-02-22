#!/usr/bin/env python3
# Purpose: Say hello

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('name', metavar='str', help='The name to greet')
    return parser.parse_args()

def main():
    args = get_args()
    print(greet(args.name))

def greet(name):
    return f'Hello, {name}!'

def test_greet():
    assert greet('World') == 'Hello, World!'
    assert greet('Terra Firma') == 'Hello, Terra Firma!'

if __name__ == '__main__':
    main()
