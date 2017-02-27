# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
# Answer: 837799


def run():
    max_length = -1
    max_value = -1
    stored = {}
    for idx in range(1, 1000000):
        list = []
        val = idx
        while val != 1:
            if val in stored:
                list = list + stored[val]
                val = 1
            else:
                if val % 2 == 0:
                    val //= 2
                else:
                    val = 3 * val + 1
                list.append(val)
        stored[idx] = list
        if len(list) > max_length:
            max_length = len(list)
            max_value = idx
    return max_value
