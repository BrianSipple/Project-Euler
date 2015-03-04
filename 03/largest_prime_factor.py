"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
import random
from itertools import chain



def quadraticIsPrime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


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



def isPrime(n):

    if n < 2:
        return False

    # About 1/3 of the time we can quickly determine if num is not prime
    # by dividing by the first few dozen prime numbers. This is quicker
    # than rabinMiller(), but unlike rabinMiller() is not guaranteed to
    # prove that a number is prime.
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
                 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
                 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
                 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
                 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
                 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521,
                 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
                 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683,
                 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
                 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
                 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967,
                 971, 977, 983, 991, 997]

    if n in lowPrimes:
        return True

    for num in lowPrimes:
        if n % num == 0:
            return False

    return rabinMillerIsPrime(n)


def generate_large_prime(keysize=1024):
    """
    Return a random prime number of bit size == keysize
    """
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num



def first(gen):
    """
    A function which just takes the first value from a generator
    and ignores the rest
    """
    try:
        return next(gen)
    except StopIteration:
        return None




def generate_prime_factor(n):
    """
    A generator to return the prime factors of a number
    """
    if not isPrime(n):

        n_sqrt = n**0.5

        while n > n_sqrt:

            ff = first(val for val in chain(
                range(2, int(n**0.5 + 1.0)), [n]) if n % val == 0)

            yield ff
            n = n / ff



def quadratic_sieve(n):
    """
    The quadratic sieve consists of computing a^2 mod n for several a,
    then finding a subset of these whose product is a square
    """

    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False    # 0 and 1 are not prime numbers

    # Create the seive
    for i in range(2, int(math.sqrt(n)) + 1):
        pointer = i * 2
        while pointer < n:
            sieve[pointer] = False
            pointer += i

    primes = []

    for i in range(n):
        if sieve[i] == True:
            primes.append(i)
            print("Found prime: {}".format(i))

    return primes


if __name__ == '__main__':

    print(isPrime(69))
    print(isPrime(690))
    print(isPrime(6900000))
    print(isPrime(7))
    #print(quadratic_sieve(600851475143))

    print(generate_large_prime())
    print(max(generate_prime_factor(40)))
    print(max(generate_prime_factor(600851475143)))
    print(max(generate_prime_factor(14)))
