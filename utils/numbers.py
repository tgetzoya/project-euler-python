from utils.factors import get_factors


def get_triangle_number(num):
    sum = 0
    for idx in range(1, num + 1):
        sum += idx
    return sum


def is_perfect_number(num, factors=None):
    if factors is None:
        factors = get_factors(num);

    return sum(factors) + 1 == num
