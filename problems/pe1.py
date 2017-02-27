# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# Answer: 233168

def run():
    sum = 0
    for idx in range(1, 1000):
        if idx % 5 == 0:
            sum += idx
        elif idx % 3 == 0:
            sum += idx
    return sum
