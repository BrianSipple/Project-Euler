"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""


def fibonacci(n, memo=None):
    """
    Computes the nth number of a fibonacci sequence
    """
    if memo is None:
        memo = {}

    if n == 1 or n == 2:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)

    return memo[n]


def find_first_fib_of_length(n):

    walk = fibonacci(1)
    current_dig_length = 1
    first_with_n = {}
    first_with_n[current_dig_length] = walk

    i = 2
    while True:
        walk = fibonacci(i)
        if len(list(str(walk))) == n:
            break
        i += 1

    return i





if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10000)

    print(find_first_fib_of_length(1000))
