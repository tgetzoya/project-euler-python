from math import sqrt


def is_prime(num):
    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for idx in range(3, int(sqrt(num)) + 1, 2):
        if num % idx == 0:
            return False
    return True
