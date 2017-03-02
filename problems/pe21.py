from utils.factors import get_factors
from utils.primes import is_prime


# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

def run():
    map = {}
    items = set()
    for idx in range(4, 10000):
        if not is_prime(idx):
            map[idx] = d(idx)

    for idx in map.keys():
        if map[idx] in map:
            right_side = map[map[idx]]
        else:
            right_side = -1

        if right_side == idx and not idx == map[idx]:
            items.add(idx)
            items.add(map[idx])

    return sum(items)


def d(n):
    return sum(get_factors(n)) + 1
