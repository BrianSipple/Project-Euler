"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def sum_of_digits_in_power(num, pow):

     value = str(num**pow)
     digits = [int(x) for x in value]

     return sum(digits)


if __name__ == '__main__':

    print(sum_of_digits_in_power(2, 1000))
