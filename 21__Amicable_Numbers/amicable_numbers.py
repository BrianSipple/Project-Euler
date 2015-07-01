"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are
an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of
220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore,
d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so,
d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import math

def divisors(n):
    return [x for x in range(1, n // 2 + 1) if n % x == 0]



def sum_amicables(thresh):

    found_amicables = []
    found_sums = {}

    for n in range(thresh):

        if n in found_amicables: # we need not evaluate further
            continue

        divisor_sum = sum(divisors(n))

        if divisor_sum in found_sums and found_sums[divisor_sum] == n:
            found_amicables.extend([divisor_sum, found_sums[divisor_sum]])

        found_sums[n] = divisor_sum


    print(found_amicables)
    return sum(found_amicables)


if __name__ == '__main__':

    #print(sum_amicables(10))
    print(sum_amicables(10000))
