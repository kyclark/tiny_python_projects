#!/usr/bin/env python3
"""
Author : Kerim Yurtbay
Purpose: Say hello
"""

import argparse


# -------------------------------------------------
def get_args():
    """Get the command-line argument"""

    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )
    return parser.parse_args()


# -------------------------------------------------
def main():
    """Make jazz noice here """

    args = get_args()
    print("Hello, " + args.name + "!")


# -------------------------------------------------
if __name__ == "__main__":
    main()
