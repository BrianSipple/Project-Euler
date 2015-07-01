"""
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40,
402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and
certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79.

The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n, (e.g. |11| = 11 and |−4| = 4)

Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum
number of primes for consecutive values of n, starting with n = 0.
"""

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


def make_prime_list(thresh, return_indices=False):
    """
    Generate a list of prime numbers from 2 two a specified threshold
    """
    if thresh <= 1:
        return []

    primes = [True] * thresh
    primes[0], primes[1] = [False] * 2

    L = []
    for i, val in enumerate(primes):

        if val is True:  # start at 2
            primes[i*2::i] = [False] * (( (thresh - 1) // i) - 1 )
            L.append(i)

    # Default to returning the primes, but allow option of
    # returning a boolean list of indices
    if return_indices:
        return primes

    return L


def isPrime(n):
    if n <= 1:
        return False
    return rabinMillerIsPrime(n)


def find_quadratic_coefficients():
    """
    We can refine a lower bound on b as follows: If a given combination (a, b)
    results in m consecutive primes,
    then clearly b > m, since otherwise we would obtain a
    factor of m in the given polynomial.

    Also, when a is negative, we must have b > -(n^2 + an),
    since the prime values n^2 + an + b must be positive.

    Since we know that  n^2 + n + 41 returns 40 primes,
    we know that any interesting values for a and b must then
    satisfy b > -(40^2 + 40a).
    """

    max_found = 0
    max_a_coeff = 0
    max_b_coeff = 0

    primes_list = make_prime_list(751000, return_indices=True)

    for a in range(-1000, 1000):
        for b in range(2, 1000):

            if primes_list[b] is False:
                continue

            if b < ((-1 * 1600) - (40 * a)) or b < max_found:
                continue

            consec_prime_count = 0
            n = 0

            while isPrime(int( (n**2) + (a * n) + b)):

                n += 1
                print("n: {}".format(n))

                # We're done for this pair -- check if we found a new max
                if n > max_found:
                    max_found = n
                    max_a_coeff = a
                    max_b_coeff = b




    print("Number of primes found: {}".format(max_found))
    print("Max Coefficient Product Found: {}".format(max_a_coeff * max_b_coeff))
    print("a coefficient: {}".format(max_a_coeff))
    print("b coefficient: {}".format(max_b_coeff))


if __name__ == '__main__':

    import random

    find_quadratic_coefficients()
