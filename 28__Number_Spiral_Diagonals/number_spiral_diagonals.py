"""
Starting with the number 1 and moving to the right in a
clockwise direction, a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
(Diagonals being the top-left-to-bottom-right and bottom-left-to-top-right
"X" that can be drawn throught the grid)

What is the sum of the numbers on the diagonals in a 1001 by 1001
spiral formed in the same way?
"""

def sum_spiral_diagonals(length):
    res = 1
    dimensions = range(3, length+1, 2)
    for distance_from_center in range(1, len(dimensions)+1):
        res += sum_corners(distance_from_center)

    return res


def sum_corners(distance_from_center):

    two_n = 2 * distance_from_center

    top_right = (two_n + 1)**2  # Algorithm for top-right

    # The rest of the corners just need to be decremented by successive 2n's, going counterclockwise
    top_left = top_right - two_n
    bottom_left = top_left - two_n
    bottom_right = bottom_left - two_n

    return top_right + top_left + bottom_left + bottom_right





if __name__ == '__main__':

    print(sum_spiral_diagonals(5))
    print(sum_spiral_diagonals(1001))
