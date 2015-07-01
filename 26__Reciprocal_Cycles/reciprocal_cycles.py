"""
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators
2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
"""

from decimal import Decimal
from math import log
import random


def rabinMillerIsPrime(n):
    """
    If rabinMiller returns true, the number is EXTREEEEEMLY likely
    to be prime. If it returns false, it's GUARANTEED to be composite
    """

    NUM_TRIALS = 5

    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    # test the base a to see whether it is a witness for the compositeness of n
    def is_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite

    for i in range(NUM_TRIALS):
        a = random.randrange(2, n)
        if is_composite(a):
            return False

    return True # no base being tested showed n as composite




def isPrime(num):
    if num < 2:
        return False

    return rabinMillerIsPrime(num)


def gen_prime_list_length(length):

    res = []
    current_num = 0
    primes_found = 0

    while primes_found < length:

        if isPrime(current_num):
            res.append(current_num)
            primes_found += 1

        current_num += 1

    return res


def gcd(x, y):
    """
    Euclid: if r is the remainder when a is divided by b,
    then gcd(a, b) = gcd(b, r).

    As a base case, we can use gcd(a, 0) = a.
    """
    if y == 0:
        return x

    remainder = x % y

    if remainder == 0:
        return y
    else:
        return gcd(y, remainder)


def is_coprime_to_ten(n):
    """
    Two numbers are co-primes if their gcd is 1. Therfore, a number is
    co-prime to 10 if the number and 10 have a gcd of 1
    """
    return gcd(n, 10) == 1


def longest_recurring_cycle(thresh):
    """
    Find the number, n, where 1 < n < thresh, whose decimal representation
    of its reciprical has the longest recurring cycle.

    KEY: To find the longest cycle, it's sufficient to look just
    at the primes -- because other numbers will only, merely,
    have the same cycles after some initial non-repetitive section.
    """

    primes = []

    for i in range(1, thresh):
        if isPrime(i):
            primes.append(i)


    for d in primes[::-1]:

        period = 1
        while pow(10, period, d) != 1:
            period += 1

        if d-1 == period:
            break
    print("Longest recurring cycle found for 1/d, d = {}".format(d))






if __name__ == '__main__':

    print(longest_recurring_cycle(1000))
