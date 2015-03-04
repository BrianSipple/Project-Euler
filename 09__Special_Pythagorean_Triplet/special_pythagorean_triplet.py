"""
A Pythagorean triplet is a set of three natural numbers,
 a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def find_pythagorean_triplet(total):

    for a in range(1, total//3):
        for b in range(a+1, total//2):

            c = total - a - b  # Guarantee a, b, and c sum to the total

            if (a**2 + b**2) == c**2:
                print("Found triplet: ({}, {}, {})".format(a, b, c))
                print("Product of triplet: {}".format(a * b * c))
                return a * b * c



if __name__ == '__main__':

    print(find_pythagorean_triplet(25))
    print(find_pythagorean_triplet(1000))
