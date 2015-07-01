"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the
digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic
permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation
of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import math



def find_nth_lex_permuation(n, sequence):

    num_perms = math.factorial(n)

    N = len(sequence)
    res_permutation = ''
    remaining_perms = n - 1
    digits_available = sequence


    for i in range(1, N):
        j = remaining_perms // math.factorial(N - i)
        remaining_perms = remaining_perms % math.factorial(N - i)

        res_permutation += str(digits_available[j])
        digits_available.pop(j)

        if remaining_perms == 0:
            break


    # Cleanup by adding the remaining unchanged digits to the sequence
    for i in range(len(digits_available)):
        res_permutation += str(digits_available[i])

    return res_permutation


if __name__ == '__main__':


    print(find_nth_lex_permuation(1000000, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
