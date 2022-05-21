#!/usr/bin/env python3
"""
Author : haoruic <haorui1997@gmail.com>
Date   : 2022-05-21
Purpose: Chapter 02 - Crow's Nest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest - choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("object", metavar="object", help="Object sighted", type=str)

    parser.add_argument(
        "--side",
        metavar="side",
        help="Side object sighted on",
        type=str,
        default="larboard",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    obj_arg = args.object
    side_arg = args.side

    # Check if side is valid
    side_valid = side_arg in ["larboard", "starboard"]

    if side_valid:
        # Select article based on first letter of word
        first_char = obj_arg[0].lower()
        article = "an" if first_char in "aeiou" else "a"

        print(f"Ahoy, Captain, {article} {obj_arg} off the {side_arg} bow!")

    else:
        print(
            f"'{side_arg}' is not a valid side. Please input one of 'larboard' of 'starboard'."
        )


# --------------------------------------------------
if __name__ == "__main__":
    main()
