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


def get_fibonacci(num):
    if num == 1 or num == 2:
        return 1

    if num == 3:
        return 2

    f1 = 1
    f2 = 2
    num -= 3

    while num > 0:
        hold = f2
        f2 = hold + f1
        f1 = hold
        num -= 1

    return f2
