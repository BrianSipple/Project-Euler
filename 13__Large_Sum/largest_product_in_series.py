"""
Work out the first ten digits
of the sum of the one-hundred
50-digit numbers in large_nums.txt
"""


def main():

    nums = []
    with open('large_nums.txt', 'rb') as f:
        for line in f.readlines():
            nums.append(line.strip())


    """
    Since the required answer to this problem only
    requires the first 10 digits of the sum, there is
    absolutely no need to add more than the first 11 digits
    of each of the 100 numbers, yielding a 13-digit number.

    Adding the 12th++ digits could never affect more than the 11th
    digit of the sum.
    """

    sum_of_first_11 = sum([int(num[:13]) for num in nums])

    print(sum_of_first_11)

    first_10_of_sum = str(sum_of_first_11)[:10]
    print(first_10_of_sum)


if __name__ == '__main__':
    main()
