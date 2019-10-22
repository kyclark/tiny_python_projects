#!/usr/bin/env python3
# Author: Ken Youens-Clark

import argparse
import os
import sys
from typing import List

def greet(name: str) -> str:
    return f'Hello, {name}!'

def test_greet() -> None:
    assert greet('World') == 'Hello, World!'
    assert greet('Terra Firma') == 'Hello, Terra Firma!'

def main() -> None:
    parser = argparse.ArgumentParser(
        description='Say hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('name', metavar='str', help='The name to greet')
    args = parser.parse_args()
    print(greet(args.name))

if __name__ == '__main__':
    main()
