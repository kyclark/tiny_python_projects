#!/usr/bin/env python3
# Author: Ken Youens-Clark

import argparse

def greet(name: str) -> str:
    return f'Hello, {name}!'

def test_greet() -> None:
    assert greet('World') == 'Hello, World!'
    assert greet('Terra Firma') == 'Hello, Terra Firma!'

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Say hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('name', metavar='str', help='The name to greet')
    return parser.parse_args()

def main() -> None:
    args = get_args()
    print(greet(args.name))

if __name__ == '__main__':
    main()
