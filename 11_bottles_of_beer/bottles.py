#!/usr/bin/env python3
"""
Author : Lee A. Congdon <lee@lcongdon.com>
Date   : 2021-07-27
Purpose: Tiny Python Projects bottles of beer exercise
"""

import argparse


def get_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description="Bottles of beer song",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--num",
        default=10,
        type=int,
        help="How many bottles",
        metavar="number",
    )

    parser.add_argument(
        "-s",
        "--step",
        default=1,
        type=int,
        help="Interval to step",
        metavar="step",
    )

    parser.add_argument("-r", "--reverse", action="store_true", help="Reverse order")

    args = parser.parse_args()

    if args.num <= 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    if args.step <= 0:
        parser.error(f'--step "{args.step}" must be greater than 0')

    return args


def number_to_words(number):
    """Convert a positive integer less than one thousand to english text"""
    assert number >= 0 and number < 1000
    table = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
    }

    if number <= 20:
        return table[number]
    if number <= 99:
        return table[number // 10 * 10] + (
            "" if (number % 10 == 0) else f"-{table[number % 10]}"
        )
    return (
        table[number // 100]
        + " hundred"
        + ("" if (number % 100 == 0) else f" {number_to_words(number % 100)}")
    )


def test_number_to_words():
    """Test cases for number_to_words"""

    assert number_to_words(1) == "one"
    assert number_to_words(5) == "five"
    assert number_to_words(10) == "ten"
    assert number_to_words(14) == "fourteen"
    assert number_to_words(19) == "nineteen"
    assert number_to_words(20) == "twenty"
    assert number_to_words(27) == "twenty-seven"
    assert number_to_words(70) == "seventy"
    assert number_to_words(82) == "eighty-two"
    assert number_to_words(99) == "ninety-nine"
    assert number_to_words(100) == "one hundred"
    assert number_to_words(106) == "one hundred six"
    assert number_to_words(119) == "one hundred nineteen"
    assert number_to_words(144) == "one hundred forty-four"
    assert number_to_words(160) == "one hundred sixty"
    assert number_to_words(199) == "one hundred ninety-nine"
    assert number_to_words(200) == "two hundred"
    assert number_to_words(320) == "three hundred twenty"
    assert number_to_words(777) == "seven hundred seventy-seven"
    assert number_to_words(999) == "nine hundred ninety-nine"


def phrase(count, reverse=False):
    """Return bottle count and pluralization"""
    if count == 0:
        return "No more bottles" if not reverse else "No bottles"
    string = f"{number_to_words(count)}"
    string = string[:1].upper() + string[1:]
    return f"{string} bottle" if count == 1 else f"{string} bottles"


def test_phrase():
    """Test phrase"""

    no_bottles = phrase(0)
    assert no_bottles == "No more bottles"

    one_bottle = phrase(1)
    assert one_bottle == "One bottle"

    two_bottles = phrase(2)
    assert two_bottles == "Two bottles"

    no_bottles_reverse = phrase(0, True)
    assert no_bottles_reverse == "No bottles"

    one_bottle_reverse = phrase(1, True)
    assert one_bottle_reverse == "One bottle"

    two_bottles_reverse = phrase(2, True)
    assert two_bottles_reverse == "Two bottles"


def verse(bottle, step=1, reverse=False):
    """Sing a verse"""

    return (
        "\n".join(
            [
                f"{phrase(bottle)} of beer on the wall,",
                f"{phrase(bottle)} of beer,",
                f"Take {number_to_words(step)} down, pass {'it' if step == 1 else 'them'} around,",
                f"{phrase(bottle - step)} of beer on the wall!",
            ]
        )
        if not reverse
        else "\n".join(
            [
                f"{phrase(bottle, reverse=True)} of beer on the wall,",
                f"{phrase(bottle, reverse=True)} of beer,",
                f"Reach in the case and put {number_to_words(step)} in place,",
                f"{phrase((bottle + step), reverse=True)} of beer on the wall!",
            ]
        )
    )


def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == "\n".join(
        [
            "One bottle of beer on the wall,",
            "One bottle of beer,",
            "Take one down, pass it around,",
            "No more bottles of beer on the wall!",
        ]
    )

    two_bottles = verse(2)
    assert two_bottles == "\n".join(
        [
            "Two bottles of beer on the wall,",
            "Two bottles of beer,",
            "Take one down, pass it around,",
            "One bottle of beer on the wall!",
        ]
    )

    five_step_two_bottles = verse(5, step=2)
    assert five_step_two_bottles == "\n".join(
        [
            "Five bottles of beer on the wall,",
            "Five bottles of beer,",
            "Take two down, pass them around,",
            "Three bottles of beer on the wall!",
        ]
    )

    first_verse_reverse = verse(0, reverse=True)
    assert first_verse_reverse == "\n".join(
        [
            "No bottles of beer on the wall,",
            "No bottles of beer,",
            "Reach in the case and put one in place,",
            "One bottle of beer on the wall!",
        ]
    )

    second_verse_reverse = verse(1, reverse=True)
    assert second_verse_reverse == "\n".join(
        [
            "One bottle of beer on the wall,",
            "One bottle of beer,",
            "Reach in the case and put one in place,",
            "Two bottles of beer on the wall!",
        ]
    )

    first_verse_four_bottles_reverse = verse(0, step=4, reverse=True)
    assert first_verse_four_bottles_reverse == "\n".join(
        [
            "No bottles of beer on the wall,",
            "No bottles of beer,",
            "Reach in the case and put four in place,",
            "Four bottles of beer on the wall!",
        ]
    )


def main():
    """Main program"""

    args = get_args()
    print(
        "\n\n".join(
            verse(bottle, min(bottle, args.step), args.reverse)
            for bottle in range(args.num, 0, -args.step)
        )
        if not args.reverse
        else "\n\n".join(
            verse(bottle, min(args.step, args.num - bottle), args.reverse)
            for bottle in range(0, args.num, args.step)
        )
    )


if __name__ == "__main__":
    main()
