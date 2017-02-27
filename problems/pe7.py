from utils.primes import is_prime


# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#
# Answer: 104743

def run():
    list = []
    idx = 1
    while len(list) < 10001:
        if is_prime(idx):
            list.append(idx)
        idx += 1
    return list[-1]
