"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(n, fac_memo=None):

    if fac_memo is None:
        fac_memo = {}

    if n <= 1:
        return n

    if n in fac_memo:
        return fac_memo[n]

    prev_val = factorial(n-1, fac_memo)
    fac_memo[n-1] = prev_val

    return n * prev_val


def sum_of_factorial_digits(n):
    fac_digits = list(str(factorial(n)))
    print(fac_digits)

    res = 0
    for digit in fac_digits:
        res += int(digit)

    return res



if __name__ == '__main__':
    print(sum_of_factorial_digits(10))
    print(sum_of_factorial_digits(100))
