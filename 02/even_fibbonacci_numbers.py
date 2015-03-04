"""
Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose
values do not exceed four million, find the sum of the even-valued terms.
"""


def fibonacci(n):
    """
    A fibonacci function... just because it's cool
    """
    if n == 1 or n == 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


def make_fibonacci_sequence(n):
    res = []

    i = 1
    j = 2

    while i < n:

        res.append(i)
        if j < n:
            res.append(j)

        old_j = j

        i += old_j
        j += i

    return res




if __name__ == '__main__':
    print(fibonacci(10))


    nums = make_fibonacci_sequence(4000000)
    nums = [n for n in nums if n % 2 == 0]
    print(sum(nums))
