"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence
(starting at 13 and finishing at 1) contains 10 terms.

Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

def find_collatz_seq(thresh):
    seq = [thresh]
    while thresh > 1:
        next_num = compute_next_collatz(thresh)
        seq.append(next_num)
        thresh = next_num

    return seq


def compute_odd(n):
    return 3 * n + 1


def compute_even(n):
    return n / 2


def compute_next_collatz(n):
    if n % 2 == 0:
        return compute_even(n)
    else:
        return compute_odd(n)


def find_largest_collatz_generator(max_num):

    current_max_gen = None
    current_max_seq_len = 0

    for i in range(max_num, int(max_num * .75), -1):
        seq_length = len(find_collatz_seq(i))
        if seq_length > current_max_seq_len:
            current_max_gen = i
            current_max_seq_len = seq_length


    print("Max collatz seq len: {}".format(current_max_seq_len))
    print("Number responsible: {}".format(current_max_gen))
    return current_max_gen



if __name__ == '__main__':
    print(find_largest_collatz_generator(1000000))

    # current result: 837799
    #print(find_collatz_seq(9))
