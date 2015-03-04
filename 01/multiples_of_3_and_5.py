"""
If we list all the natural numbers below 10 that
are multiples of 3 or 5, we get 3, 5, 6 and 9.

The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_of_mults(a, b, thresh):

    mults = []

    mults.extend([mult for mult in range(a, thresh, a)])
    mults.extend([mult for mult in range(b, thresh, b) if mult not in mults])

    print(mults)
    return sum(mults)


if __name__ == '__main__':

    print(sum_of_mults(3, 5, 1000))
    print(sum_of_mults(3, 5, 10))
    print(sum_of_mults(3, 5, 1000000000000000000))
