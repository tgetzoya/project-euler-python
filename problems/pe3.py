import functools
from math import sqrt


# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# Answer: 6857


def run():
    return largest_prime_factor(600851475143)


def largest_prime_factor(num):
    prime_factors = []
    for factor in get_factors(num):
        if is_prime(factor):
            prime_factors.append(factor)
    return prime_factors[-1]


def get_factors(num):
    if is_prime(num):
        return []
    return sorted(set(
        functools.reduce(list.__add__,
                         ([i, num // i] for i in range(2, int(sqrt(num)) + 1) if num % i == 0))))


def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0 and num > 2:
        return False
    return all(num % i for i in range(3, int(sqrt(num)) + 1, 2))
