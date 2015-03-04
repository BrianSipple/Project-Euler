"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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



def sum_of_primes(limit):

    crosslimit = int(math.floor(limit**.5))
    print(crosslimit)

    sieve = [False] * limit  # Make a list of all numbers from 2 to N. (We'll need to account for the 0 and 1 in our iterations below)

    for i in range(3, len(sieve), 2):   # mark even numbers > 2 as True (composite)
        sieve[i] = True


    for i in range(2, crosslimit, 2):

        # If i is not marked, it's prime
        if not sieve[i]:
            for j in range(i**i, len(sieve), 2*i):
                sieve[j] = True


    primes_sum = 0
    for i in range(1, len(sieve)):
        if not sieve[i]:
            print("Hello: {}".format(i))
            primes_sum += (i+1)

    return primes_sum



if __name__ == '__main__':

    import random
    import math

    #print(gen_prime_list_length(6))
    #print(gen_prime_list_length(10001))
    #primes = gen_max_prime_list_max_num(2000000)

    #print(primes)

    #print(sum(primes))
    print(sum_of_primes(2000000))
