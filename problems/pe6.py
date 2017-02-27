# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#
# Answer: 25164150

def run():
    print(square_of_sums(100) - sum_of_squares(100))


def sum_of_squares(num):
    sum = 0
    for idx in range(1, num + 1):
        sum += idx ** 2
    return sum


def square_of_sums(num):
    sum = 0
    for idx in range(1, num + 1):
        sum += idx
    return sum ** 2
