import functools
from math import sqrt

from utils.primes import is_prime


def get_factors(num, include_one_and_num=False):
    if is_prime(num) or num < 3:
        factors = []
    else:
        factors = sorted(
            set(functools.reduce(list.__add__, ([i, num // i] for i in range(2, int(sqrt(num)) + 1) if num % i == 0))))

    if (include_one_and_num):
        factors.insert(0, 1)
        factors.append(num)

    return factors
