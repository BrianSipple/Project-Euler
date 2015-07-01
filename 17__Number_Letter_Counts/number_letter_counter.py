"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand)
inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters.

The use of "and" when writing out numbers is in
compliance with British usage.
"""


def one_to_nine():
    return 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4   # 36

def ten_to_nineteen():
    return 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8   # 70


def twenty_to_ninety_nine():
    return 10* (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + (8 * one_to_nine())


def one_to_ninety_nine():
    return twenty_to_ninety_nine() + ten_to_nineteen() + one_to_nine()


def one_hundred_to_999():
    return (7 * 9) + \
                (100 * (one_to_nine())) + \
                (9 * one_to_ninety_nine()) + \
                (10 * 9 * 99)  # "and"


def letters_in_numbers_to_one_thousand():
    return 11 + \
           one_to_ninety_nine() + \
           one_hundred_to_999()



if __name__ == '__main__':
    print(letters_in_numbers_to_one_thousand())
