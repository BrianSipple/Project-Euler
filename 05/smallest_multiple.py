"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""

def isMultiple(num, multiple_of):
    """
    is "num" a multiple of "multiple_of" ?
    """
    return num % multiple_of == 0





def find_smallest_multiple_from_1_to_range(range_num):
    from functools import reduce
    return reduce(lcm, range(1, range_num))



def lcm(a, b):
    """
    The lowest common multiple of any two numbers is
    their product divided by their Greatest Common Divisor
    """
    from fractions import gcd
    return (a * b) // gcd(a,b)




if __name__ == '__main__':

    print(find_smallest_multiple_from_1_to_range(20))
