#!/usr/bin/env python3
"""
Hello, World! from Tiny Python Projects
Lee A. Congdon <lee@lcongdon.com>
Created: 9 July 2021
"""

import argparse


def get_args():
    """Get command line arguments"""
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )
    return parser.parse_args()


def main():
    """Display output"""
    args = get_args()
    print("Hello, " + args.name + "!")


if __name__ == "__main__":
    main()
