"""
Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
import math



def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)



def compute_combinatorial(n, choose_k):
    return factorial(n) / \
        ( factorial(choose_k) * factorial(n - choose_k) )



def compute_possible_lattice_routes(n):

    # the solution for the number of paths through
    # an n x n grid will be found in the middle of the 2nth row in
    # Pascal's Triangle
    pascal_row = 2 * n

    # And that kth position of that nth row represents a combinatorial
    # of n choose k possiblities
    return compute_combinatorial(pascal_row, pascal_row/2)




if __name__ == '__main__':
    #print(factorial(10))
    print(compute_possible_lattice_routes(2))
    print(compute_possible_lattice_routes(20))
