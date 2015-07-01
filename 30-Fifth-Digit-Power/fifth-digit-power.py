"""
Surprisingly there are only three numbers that can be written
as the sum of fourth powers of their digits:

1634 = 1 ^ 4 + 6 ^ 4 + 3 ^ 4 + 4 ^ 4
8208 = 8 ^ 4 + 2 ^ 4 + 0 ^ 4 + 8 ^ 4
9474 = 9 ^ 4 + 4 ^ 4 + 7 ^ 4 + 4 ^ 4
As 1 = 1 ^ 4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be
written as the sum of fifth powers of their digits.
"""

def sum_of_powers (n, p):

    res = 0
    digits = list(str(n))

    for d in digits:
        res += int(d)**p

    return res


def find_nums_matching_sum_of_power(p):

    matches = []
    range_min = 10  # Any single digit to a power is not a sum of digit powers
    range_max = (9**p) * (p-1)  # The number of digits for the sum must have the same number of digits as a candidate, see the table below:

    for num in range(range_min, range_max):
        sum_of_p = sum_of_powers(num, p)
        if sum_of_p == num:
            matches.append(num)


    print('Matches computed for sum of digits to the power of ' + str(p) + ':...')
    print(matches)

    sum_of_matches = sum(matches)
    print("Sum of matches: " + str(sum_of_matches))

    return sum_of_matches



if __name__ == '__main__':

    power = 4
    sum_of_matches = find_nums_matching_sum_of_power(power)

    power = 5
    sum_of_matches = find_nums_matching_sum_of_power(power)
