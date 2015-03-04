"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
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


def gen_max_prime_list_max_num(max_num):

    res = []
    current_num = 0

    while current_num < max_num:

        if isPrime(current_num):
            res.append(current_num)

        current_num += 1

    return res






if __name__ == '__main__':

    import random

    #print(gen_prime_list_length(6))
    #print(gen_prime_list_length(10001))
