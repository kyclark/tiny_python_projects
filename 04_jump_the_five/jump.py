#!/usr/bin/env python3
"""
Author : J
Date   : 08/05/21
Purpose: In an episode of the television show The Wire, 
    drug dealers assume the police are intercepting their text messages. 
    Whenever a phone number needs to be texted in the course of a criminal conspiracy,
    the dealers will obfuscate the number.
    They use an algorithm we’ll call “Jump the Five” because each number is changed 
    to its mate on the opposite of a US telephone pad if you jump over the 5.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jumper',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('inputString',
                        metavar='Input string',
                        help='A positional string argument',
                        type=str)

    parser.add_argument('-s',
                        '--string',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Comvert the numbers in an input string to there 'jump the 5' equivalents."""

    args = get_args()
    str_arg = args.inputString

    jump_map:dict = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
                     '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    new_str:str = ''
    for letter in str_arg:
        val = jump_map.get(letter, letter)
        new_str = new_str + val

    print(new_str)


# --------------------------------------------------
if __name__ == '__main__':
    main()
