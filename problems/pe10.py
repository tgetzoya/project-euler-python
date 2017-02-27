from utils.primes import is_prime


# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# Answer: 142913828922

def run():
    sum = 2  # 2 is prime
    for idx in range(3, 2000001, 2):
        if is_prime(idx):
            sum += idx

    return sum
