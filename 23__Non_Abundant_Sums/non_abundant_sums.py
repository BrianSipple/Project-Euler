"""
A perfect number is a number for which the sum of
its proper divisors is exactly equal to the number.

For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
is a perfect number.

A number n is called deficient if the sum of
its proper divisors is less than n and it is called
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of
two abundant numbers is 24.

By mathematical analysis, it can be shown that all
integers greater than 28123 can be written as the sum
of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as
the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers
which cannot be written as the sum of two abundant numbers.
"""
import math


def divisors(n):
    """
    Returns all nontrivial divisors of an integer, but makes no guarantees on the order.
    """
    yield 1

    largest = int(math.sqrt(n))

    # Special case where largest is the square-root of n
    if largest * largest == n:
        yield largest
    else:
        largest += 1

    for i in range(2, largest):
        if n % i == 0:
            yield int(i)
            yield int(n / i)


def is_abundant(n):
    return n >= 12 and sum(divisors(n)) > n


ABUNDANTS = [n for n in range(1, 28123+1) if is_abundant(n)]



def is_abundant_sum(n):
    """
    Can a number n can be written as a sum of abundant numbers i and k?

    We'll use the fact that if there exists any abundant number i
    with the constraint i < n, and another abundant number
    with the constraints k < n and n - i == k, n IS AN ABUNDANT SUM!
    """

    ###
    # 'abundants' is a list, which is an ordered data structure.
    # If we search for an element that is not contained
    # in the list, all elements would have to be searched.
    # The set() data structure is faster.
    abundants_set = set(ABUNDANTS)

    for i in ABUNDANTS:
        if i > n:
            # We know we can bail out here
            return False

        if (n - i) in abundants_set:
            return True

    # The serach is over. If we're still here, return False
    return False


def sum_non_abundants():
    return sum([x for x in range(1, 28123+1) if not is_abundant_sum(x)])


if __name__ == '__main__':
    #print(divisors(12))
    #print(abundant_number_series(100))
    print(sum_non_abundants())
    #print([d for d in divisors(120)])
