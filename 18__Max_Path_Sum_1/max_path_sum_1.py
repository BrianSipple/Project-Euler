"""
By starting at the top of the triangle below and moving to
adjacent numbers on the row below, the maximum total
from top to bottom is 23.

    3
   7 4
  2 4 6
 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                        75
                       95 64
                      17 47 82
                     18 35 87 10
                    20 04 82 47 65
                  19 01 23 75 03 34
                 88 02 77 73 07 63 67
                99 65 04 28 06 16 70 92
              41 41 26 56 83 40 80 70 33
             41 48 72 33 47 32 37 16 94 29
            53 71 44 65 25 43 91 52 97 51 14
           70 11 33 28 77 73 17 78 39 68 17 57
          91 71 52 38 17 14 91 43 58 50 27 29 48
         63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

"""

import math

def left_child_pos(list_pos, length):
    if list_pos < length / 2:
        return list_pos * 2
    return None

def right_child_pos(list_pos, length):
    if list_pos < length / 2:
        return list_pos * 2 + 1


def max_triangle_sum_brute_force(num_list):

    depth = len(num_list)
    possible_paths = int((depth - 1)**2)
    largest_sum = 0

    for i in range(possible_paths+1):

        temp_sum = num_list[0][0]
        index = 0

        for j in range(depth - 1):
            index += (i >> j & 1)
            print(j, index)
            temp_sum += num_list[j+1][index]

        if temp_sum > largest_sum:
            largest_sum = temp_sum

    return largest_sum


def max_triangle_sum_dp(num_triangle):

    res = 0
    new_triangle = []

    for i in range(len(num_triangle)-2, 0, -1):

        for j in range(len(num_triangle[i])-1):
            num_triangle[i][j] += max(num_triangle[i+1][j], num_triangle[i+1][j+1])

    #print(num_triangle)
    return num_triangle[0][0] + max(num_triangle[1][0], num_triangle[1][1])






if __name__ == '__main__':

    ####
    # Represent the data as a list of list such that the
    # longest list element is full,
    # and the shorter list elements are padded with 0
    #
    #[ [1, 0, 0, 0], [1, 2, 0, 0], [23, 23, 9, 0], [4, 2, 5, 1] ]
    #
    ####

    file_path = 'triangle2.txt'
    initial_data = []
    num_lines = 0

    with open(file_path, 'r') as f:
        for line in f.readlines():
            num_lines += 1


    final_data_struct = []
    for i in range(num_lines):
        final_data_struct.append([0] * num_lines)


    line_num = 0
    with open(file_path, 'r') as f2:
        for line in f2.readlines():

            nums = [int(n) for n in line.strip().split()]
            for i in range(len(nums)):

                final_data_struct[line_num][i] = nums[i]
            line_num += 1


    #print(final_data_struct)
    print(max_triangle_sum_dp(final_data_struct))
    #print(max_triangle_sum_brute_force(final_data_struct))
