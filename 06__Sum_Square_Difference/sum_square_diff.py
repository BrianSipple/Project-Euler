"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""

def sum_list(num_list):

    if len(num_list) == 1:
        return num_list[0]

    return sum_list(num_list[0:-1]) + num_list[-1]



def find_sum_square_diff(num_list):

    sum_of_list_squared = sum_list(num_list)**2
    sum_of_squares_in_list = sum_list([num**2 for num in num_list])

    return abs(sum_of_squares_in_list - sum_of_list_squared)


if __name__ == '__main__':

    num_list = range(101)

    print(find_sum_square_diff(num_list))
