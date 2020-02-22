#!/usr/bin/env python3
"""
Purpose: Say hello
Author:  Ken Youens-Clark
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('name', metavar='str', help='The name to greet')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start here"""

    args = get_args()
    print(greet(args.name))


# --------------------------------------------------
def greet(name):
    """Create a greeting"""

    return f'Hello, {name}!'


# --------------------------------------------------
def test_greet():
    """Test greet"""

    assert greet('World') == 'Hello, World!'
    assert greet('Terra Firma') == 'Hello, Terra Firma!'


# --------------------------------------------------
if __name__ == '__main__':
    main()
